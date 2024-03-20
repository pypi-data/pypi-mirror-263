# -*- coding: utf-8 -*-
# Copyright (2019) Cardiff University
# Licensed under GPLv3+ - see LICENSE

"""Utilities for the GWDataFind Server
"""

import re
import threading
import time
from collections import defaultdict
from contextlib import contextmanager
from io import StringIO
from os.path import getmtime
from shutil import which
from subprocess import check_output

from ligo.segments import (segment, segmentlist)

__author__ = 'Duncan Macleod <duncan.macleod@ligo.org>'


class CacheManager(threading.Thread):
    """Thread for managing a cache of some data in memory.
    """
    def __init__(
       self,
       source,
       parent,
       name=None,
       sleeptime=60,
    ):
        # init the thread
        super().__init__(name=name or type(self).__name__)

        #: Path to read
        self.source = source

        #: Time of last source modification
        self.last = 0

        #: Logger to use
        self.logger = parent.logger

        # create lock and flags
        self.lock = threading.Lock()
        self.shutdown = False
        self.ready = False

        # time between iterations
        self.sleeptime = sleeptime

    def sleep(self):
        """Wait until next iteration
        """
        self.logger.debug(f"sleeping for {self.sleeptime} seconds")
        start = time.time()
        while time.time() - start < self.sleeptime:
            time.sleep(.5)
            if self.shutdown:
                self.state = 'SHUTDOWN'
                return

    def source_modified(self):
        """Return `True` if the source has been modified
        and should be re-parsed.
        """
        try:
            mod = getmtime(self.source)
        except OSError as exc:
            self.logger.error(
                "unable to determine modification time of "
                f"{self.source}: {exc}",
            )
            mod = 0

        if self.last < mod:  # file changed since last iteration
            return True

    def run(self):
        """Continuously read and update the cache.

        This calls out to the `parse()` method, which should update the
        ``self.cache`` attribute with new information.
        """
        while True:
            if self.shutdown:
                return

            if self.source_modified():
                try:
                    self.parse()
                except (TypeError, ValueError) as exc:
                    self.logger.error(f"error parsing {self.source}: {exc}")
                else:
                    self.last = time.time()
            else:
                self.logger.debug('cache file unchanged since last iteration')
            self.sleep()


class DiskcacheManager(CacheManager):
    """Thread to continuously update the diskcache in memory
    """
    def __init__(
        self,
        parent,
        path,
        sleeptime=60,
        site_exclude=None,
        site_include=None,
        frametype_exclude=None,
        frametype_include=None,
    ):
        super().__init__(
            path,
            parent,
            name=type(self).__name__,
            sleeptime=sleeptime,
        )

        # create cache
        self.cache = defaultdict(dict)

        # record exclusion filters
        self.patterns = {key: self._parse_pattern(value) for key, value in [
             ('site_exclude', site_exclude),
             ('site_include', site_include),
             ('frametype_exclude', frametype_exclude),
             ('frametype_include', frametype_include),
        ]}

    @staticmethod
    def _parse_pattern(pattern):
        if pattern is None:
            pattern = []
        if not isinstance(pattern, list):
            pattern = [pattern]
        return [re.compile(reg) for reg in pattern]

    def _update(self, cache):
        self.logger.debug('updating frame cache')
        with self.lock:
            self.cache = cache
        self.logger.debug(f'updated frame cache with {len(cache)} entries')
        # print what we got
        for a, suba in cache.items():  # filetype
            for b, subb in suba.items():  # observatory
                for c, subc in subb.items():  # dataset
                    self.logger.debug(
                        f"  {a}/{b}/{c}: {len(subc)} entries",
                    )

    def exclude(self, site, tag):
        """Return `True` if this site and tag combination should be excluded
        """
        for var, key in ((site, 'site'), (tag, 'frametype')):
            pat = f"{key}_exclude"
            for regex in self.patterns[pat]:
                if regex.search(var):  # positive match
                    return pat
            pat = f"{key}_include"
            for regex in self.patterns[pat]:
                if not regex.search(var):  # negative match
                    return pat

    @contextmanager
    def _diskcache_file(self):
        with open(self.source, "r", encoding="utf-8") as fobj:
            cache_version = self._parse_cache_format(fobj)
            yield fobj, cache_version

    @contextmanager
    def _diskcache_dump(self, version="0x0101"):
        host, port = self.source
        cmd = [
            which("diskcache") or "diskcache",
            "--host", str(host),
            "--port", str(port),
            "dump",
            "--output-ascii", "-",
            "--version-ascii", str(version),
        ]
        proc = check_output(cmd, encoding="utf-8").strip()
        yield StringIO(proc), version

    def parse(self):
        """Read the frame cache from the path
        """
        self.logger.info(f'parsing frame cache from {self.source}')
        exclusions = {key: 0 for key in self.patterns}
        nlines = 0
        cache = {}

        if isinstance(self.source, (list, tuple)):
            diskcache = self._diskcache_dump
        else:
            diskcache = self._diskcache_file

        with diskcache() as ctx:
            fobj, cache_version = ctx
            cache_version = self._parse_cache_format(fobj)
            self.logger.info(f"parsed cache format as version {cache_version}")
            try:
                parse_line = getattr(self, f"_parse_diskcache_{cache_version}")
            except AttributeError:
                raise TypeError(
                    "cannot parse diskcache files with version "
                    f"'{cache_version}'",
                )

            for line in fobj:
                if line.startswith("#") or not line:
                    continue
                # parse line
                site, tag, path, dur, ext, segments = parse_line(line)
                # determine exclusion
                exclude = self.exclude(site, tag)
                if exclude:  # record why excluded
                    exclusions[exclude] += 1
                    continue
                # store this line in the cache
                subcache = cache
                for key in (
                    ext,
                    site,
                    tag,
                ):
                    subcache = subcache.setdefault(key, {})
                subcache[(path, int(dur))] = segments
                nlines += 1

        self.logger.info(f'parsed {nlines} lines from frame cache file')
        for key, count in exclusions.items():
            self.logger.debug(f'excluded {count} lines with {key}')

        # store new cache
        self._update(cache)
        self.ready = True  # can now be used

    @staticmethod
    def _parse_cache_format(fobj):
        """Parse the diskcache file format and return the appropriate parser.
        """
        pos = fobj.tell()
        try:
            fobj.seek(0)
            line = fobj.readline().strip()
            if line.startswith("# version: "):  # version header
                return line[11:]
            # no version header
            return "0x00ff"
        finally:
            # always return the stream to where it was
            fobj.seek(pos)

    @staticmethod
    def _parse_diskcache_times(times):
        """Parse a diskcache-format list of times as a segmentlist.
        """
        times = list(map(int, times.strip("{}").strip().split(' ')))
        return segmentlist(map(
            segment,
            (times[i:i+2] for i in range(0, len(times), 2)),
        ))

    @classmethod
    def _parse_diskcache_0x00ff(cls, line):
        """Parse a line as a diskcache entry in the 0x00ff format:

            /path/to/dir,SITE,TAG,_,DUR MODT COUNT {TIMES}

        This format _only_ supports GWF extensions.
        """
        # parse line
        header, modt, count, times = line.strip().split(' ', 3)
        hdr_list = header.split(',')

        # parse header list
        path, site, tag, _, dur = tuple(hdr_list)
        dur = float(dur)

        # format times
        segments = cls._parse_diskcache_times(times)

        return site, tag, path, dur, "gwf", segments

    @classmethod
    def _parse_diskcache_0x0101(cls, line):
        """Parse a line as a diskcache entry in the 0x0101 format:

            /path/to/dir,SITE,TAG,EXT,_,DUR MODT COUNT {TIMES}
        """
        # parse line
        header, modt, count, times = line.strip().split(' ', 3)
        path, site, tag, ext, _, dur = header.split(',')

        # format entries
        dur = float(dur)
        ext = ext.lstrip(".")

        # format times
        segments = cls._parse_diskcache_times(times)

        return site, tag, path, dur, ext, segments

    def source_modified(self):
        """Return `True` if the source has been modified.
        Always returns `True` if the source points at a ``(host, port)`` pair.
        """
        if isinstance(self.source, (list, tuple)):
            return True
        return super().source_modified()


class GridmapManager(CacheManager):
    """Thread to continuously update the grid-mapfile in memory
    """
    def __init__(self, parent, path, sleeptime=600):
        super().__init__(
            path,
            parent,
            name=type(self).__name__,
            sleeptime=sleeptime,
        )

        # create cache
        self.cache = []

    def _update(self, cache):
        self.logger.debug('updating grid map cache with lock...')
        with self.lock:
            self.cache = cache
        self.logger.debug(f'updated grid map cache with {len(cache)} entries')
        # self.logger.debug(str(cache))
        self.logger.debug('lock released')

    def parse(self):
        """Read the grid-map file from the path
        """
        self.logger.info(f'parsing grid map file from {self.source}')
        nlines = 0
        cache = []

        with open(self.source, 'r') as fobj:
            for line in fobj:
                subject = self._parse_line(line)
                cache.append(subject)
                nlines += 1

        self.logger.info(f'parsed {nlines} lines from grid map file')

        # store new cache
        self._update(cache)
        self.ready = True  # can now be used

    @staticmethod
    def _parse_line(line):
        """Parse one line from the grid map file
        """
        parts = line.strip().split('"')
        if len(parts) in {2, 3}:
            return parts[1]
        if len(parts) == 1:
            return parts[0]
        raise RuntimeError(f"error parsing grid map file line: '{line}'")
