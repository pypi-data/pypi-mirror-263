---
title: ldr
author: Duncan Macleod <duncan.macleod@ligo.org>
---

# GWDataFind legacy 'LDR' API

The GWDataFind legacy 'LDR' API presents the legacy interface
that uses JSON to serialise data.

The root of the legacy LDR API is

```text
/services/data/v1
```

!!! warning "The LDR API is deprecated"

    The legacy LDR API is deprecated and will be removed as soon as
    a 'v2' API is released.

!!! info "The `/LDR` subpath is also supported"

    To maintain compatibility with older GWDataFind client versions,
    the legacy LDR API also supports accessing data with an extra
    `/LDR` path prefix, e.g. from `/LDR/services/data/v1/...`.

## Observatories API

Returns the list of known observatories.

### Format

```
GET /{ext}.json
```

### Parameters

| Name | Type | In | Description |
| ---- | ---- | -- | ----------- |
| `ext` | string | path | Return observatories with data matching this filetype (file extension) |

### Example

```shell
curl https://gwdatafind.example.com/services/data/v1/gwf.json
```

Response:

```
Status: 200 OK
```

```json
[
  "G",
  "GK",
  "H",
  "HL",
  "L",
  "K",
  "V"
]
```

### Error codes

#### `404 Not Found`

A request that includes an `{ext}` value that doesn't correspond to any known
data files will result in a `404 Not Found` error response.

## Datasets API

Returns the list of known datasets (frametypes).

### Format

```text
GET /{ext}/{observatory}.json
```

### Parameters

| Name | Type | In | Description |
| ---- | ---- | -- | ----------- |
| `ext` | string | path | Return datasets with data matching this filetype (file extension) |
| `observatory` | string | path | Return datasets with data matching this observatory ID (single-character prefix) |

### Examples

```shell
curl https://gwdatafind.example.com/services/data/v1/gwf/H.json
```

Response:

```text
Status: 200 OK
```

```json
[
  "H1_HOFT_C00",
  "H1_HOFT_C01",
]
```

### Error codes

#### `400 Bad Request`

A request that includes a `{observatory}` value that doesn't correspond to any
known data files will result in a `400 Bad Request` error response.

#### `404 Not Found`

A request that includes an `{ext}` value that doesn't correspond to any known
data files will result in a `404 Not Found` error response.

## Segments API

Returns the list of `[start, stop)` GPS segments for which data are available
for a dataset.

### Format

```text
GET /{ext}/{observatory}/{dataset}/segments.json
GET /{ext}/{observatory}/{dataset}/segments/{start},{end}.json
```

### Parameters

| Name | Type | In | Description |
| ---- | ---- | -- | ----------- |
| `ext` | string | path | Return data segments matching this filetype (file extension) |
| `observatory` | string | path | Return data segments matching this observatory |
| `dataset` | string | path | Return data segments for this dataset (frametype) |
| `start`/`end` | integer | path | Return data segments within the GPS `[start, end)` interval |

### Examples

```shell
curl https://gwdatafind.example.com/services/data/v1/gwf/H/H1_HOFT_C00/segments.json
```

Response:

```text
Status: 200 OK
```

```json
[
  [
    1000000000,
    1000000008
  ],
  [
    1000000100,
    1000000200
  ]
]
```

### Error codes

#### `400 Bad Request`

A request that includes a `{observatory}` value that doesn't correspond to any
known data files will result in a `400 Bad Request` error response.

#### `404 Not Found`

A request that includes an `{ext}` value that doesn't correspond to any known
data files will result in a `404 Not Found` error response.

## Filename API

Returns all fully-qualified URL(s) for a given filename (basename).

### Format

```text
GET /{ext}/{observatory}/{dataset}/{filename}.json
```

### Parameters

| Name | Type | In | Description |
| ---- | ---- | -- | ----------- |
| `ext` | string | path | Return URLs matching this filetype (file extension) |
| `observatory` | string | path | Return URLs matching this observatory |
| `dataset` | string | path | Return URLs matching this dataset (frametype) |
| `filename` | string | path | Return URLs matching this base filename |

### Examples

```shell
curl https://gwdatafind.example.com/services/data/v1/gwf/H/H1_HOFT_C00/H-H1_HOFT_C00-0-1.gwf.json
```

Response:

```text
Status: 200 OK
```

```json
[
  "file://localhost/path/to/H-H1_HOFT_C00-0-1.gwf.json",
  "file://localhost/backup/path/to/H-H1_HOFT_C00-0-1.gwf.json",
  "gsiftp://gsiftphost.example.com:15000/path/to/H-H1_HOFT_C00-0-1.gwf.json",
  "gsiftp://gsiftphost.example.com:15000/backup/path/to/H-H1_HOFT_C00-0-1.gwf.json",
]
```

### Error codes

#### `400 Bad Request`

A request that includes a `{observatory}` value that doesn't correspond to any
known data files will result in a `400 Bad Request` error response.

#### `404 Not Found`

A request that includes an `{ext}` value that doesn't correspond to any known
data files will result in a `404 Not Found` error response.


## URLs API

Returns the fully-qualified URL(s) for all data files matching the
request parameters.

When `{scheme}` is not given, URLs for all instances of the same filename
are returned.
However, when `{scheme}` is specified, the server configuration may optionally
dictate that only a single, _preferred_ URL is returned.

### Format

```text
GET /{ext}/{observatory}/{dataset}/{start},{end}.json
GET /{ext}/{observatory}/{dataset}/{start},{end}/{scheme}.json
```

### Parameters

| Name | Type | In | Description |
| ---- | ---- | -- | ----------- |
| `ext` | string | path | Return URLs matching this filetype (file extension) |
| `observatory` | string | path | Return URLs matching this observatory |
| `dataset` | string | path | Return URLs for this dataset (frametype) |
| `start`/`end` | integer | path | Return URLs within the GPS `[start, end)` interval |
| `scheme` | string | path | Return URLs matching this url scheme  |

### Examples

Without `{scheme}`:

```shell
curl https://gwdatafind.example.com/services/data/v1/gwf/H/H1_HOFT_C00/1000000000,1000000003.json
```

Response:

```
Status: 200 OK
```

```json
[
  "file://localhost/path/to/H-H1_HOFT_C00-1000000000-1.gwf.json",
  "file://localhost/path/to/H-H1_HOFT_C00-1000000001-1.gwf.json",
  "file://localhost/path/to/H-H1_HOFT_C00-1000000002-1.gwf.json",
  "file://localhost/backup/path/to/H-H1_HOFT_C00-1000000000-1.gwf.json",
  "file://localhost/backup/path/to/H-H1_HOFT_C00-1000000001-1.gwf.json",
  "file://localhost/backup/path/to/H-H1_HOFT_C00-1000000002-1.gwf.json",
  "gsiftp://gsiftphost.example.com:15000/path/to/H-H1_HOFT_C00-1000000000-1.gwf.json",
  "gsiftp://gsiftphost.example.com:15000/path/to/H-H1_HOFT_C00-1000000001-1.gwf.json",
  "gsiftp://gsiftphost.example.com:15000/path/to/H-H1_HOFT_C00-1000000002-1.gwf.json",
  "gsiftp://gsiftphost.example.com:15000/backup/path/to/H-H1_HOFT_C00-1000000000-1.gwf.json",
  "gsiftp://gsiftphost.example.com:15000/backup/path/to/H-H1_HOFT_C00-1000000001-1.gwf.json",
  "gsiftp://gsiftphost.example.com:15000/backup/path/to/H-H1_HOFT_C00-1000000002-1.gwf.json",
]
```

With `{scheme`}:

```shell
curl https://gwdatafind.example.com/services/data/v1/gwf/H/H1_HOFT_C00/1000000000,1000000003/file.json
```

Response:

```
Status: 200 OK
```

```json
[
  "file://localhost/path/to/H-H1_HOFT_C00-1000000000-1.gwf.json",
  "file://localhost/path/to/H-H1_HOFT_C00-1000000001-1.gwf.json",
  "file://localhost/path/to/H-H1_HOFT_C00-1000000002-1.gwf.json",
]
```

## Latest API

Returns the URL(s) of the most recent (by GPS timestamp, not by file creation
time) data file matching the request parameters.

When `{scheme}` is not given, all URLs for the same filename are returned.
However, when `{scheme}` is specified, the server configuration may optionally
dictate that only a single, _preferred_ URL is returned.

### Format

```text
GET /{ext}/{observatory}/{dataset}/latest.json
GET /{ext}/{observatory}/{dataset}/latest/{scheme}.json
```

### Parameters

| Name | Type | In | Description |
| ---- | ---- | -- | ----------- |
| `ext` | string | path | Return URLs matching this filetype (file extension) |
| `observatory` | string | path | Return URLs matching this observatory |
| `dataset` | string | path | Return URLs for this dataset (frametype) |
| `scheme` | string | path | Return URLs matching this url scheme  |

### Examples

Without `{scheme}`:

```shell
curl https://gwdatafind.example.com/services/data/v1/gwf/H/H1_HOFT_C00/latest.json
```

Response:

```
Status: 200 OK
```

```json
[
  "file://localhost/path/to/H-H1_HOFT_C00-1000000002-1.gwf.json",
  "file://localhost/backup/path/to/H-H1_HOFT_C00-1000000002-1.gwf.json",
  "gsiftp://gsiftphost.example.com:15000/path/to/H-H1_HOFT_C00-1000000002-1.gwf.json",
  "gsiftp://gsiftphost.example.com:15000/backup/path/to/H-H1_HOFT_C00-1000000002-1.gwf.json",
]
```

With `{scheme}`:

```shell
curl https://gwdatafind.example.com/services/data/v1/gwf/H/H1_HOFT_C00/latest/file.json
```

Response:

```
Status: 200 OK
```

```json
[
  "file://localhost/path/to/H-H1_HOFT_C00-1000000002-1.gwf.json",
]
```

### Error codes

#### `400 Bad Request`

A request that includes a `{observatory}` value that doesn't correspond to any
known data files will result in a `400 Bad Request` error response.

#### `404 Not Found`

A request that includes an `{ext}` value that doesn't correspond to any known
data files will result in a `404 Not Found` error response.
