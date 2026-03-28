# 🎧 px7-dlp API

![Status](https://img.shields.io/uptimerobot/status/m802716312-e588c1cc94949a008b6ba422?style=for-the-badge)


A lightweight API for discovering media via YouTube search and retrieving temporary audio stream URLs.

**Base URL:** ``https://px7-dlp.onrender.com``


## Table of Contents

* [Overview](#overview)
* [Search Endpoint](#endpoint-search)
* [Stream Endpoint](#endpoint-stream)
* [Implementation](#-implementation)


## Overview

This API provides two core capabilities:

**1.** `Search` for videos using YouTube  
**2.** `Extract` a direct audio stream URL

* No media is hosted or stored
* Stream URLs are temporary
* Initial requests may experience delay due to cold starts on free hosting

---

## Endpoint: Search

### `GET /search`

Search YouTube and return structured video metadata.


### Query Parameters

| param         | required | default                  | description                     |
| ------------- | -------- | ------------------------ | ------------------------------- |
| `query`       | yes      | —                        | search term                     |
| `limit`       | no       | `5`                      | max number of results           |
| `postfix`     | no       | `original audio song`    | improves music search relevance |


### Example

```
/search?query=the%20weeknd&limit=1
```

### Response

```
[
  {
    "name": "The Weeknd - Blinding Lights (Official Audio)",
    "video_url": "https://youtube.com/watch?v=fHI8X4OXluQ",
    "from": "The Weeknd",
    "duration": 204
  }
]
```
> ⚠️ `duration` is in seconds

---

## Endpoint: Stream

### `GET /stream`

Extract a direct audio stream URL for a given video.


### Query Parameters

| param | required | description       |
| ----- | -------- | ----------------- |
| `url` | yes      | YouTube video URL |



### Example

```
/stream?url=https://youtube.com/watch?v=fHI8X4OXluQ
```

### Response

```
{
  "stream_url": "https://..."
}
```
> ⚠️ `stream_url` is temporary and may expire after some instance of time

---

## 🛠 Implementation

This API uses yt-dlp under the hood for media extraction.

