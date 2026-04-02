from app.config import YDL_OPTIONS, DEFAULT_QUERY_POSTFIX, DEFAULT_YT_SEARCH_LIMIT
import yt_dlp

def search_yt(query, postfix, limit):
    if postfix is None: postfix = DEFAULT_QUERY_POSTFIX
    if limit is None: limit = DEFAULT_YT_SEARCH_LIMIT
    try:
        with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(f"ytsearch{limit}:{query}{postfix}", download=False)
    except Exception:
        return []
    results = []
    for entry in info["entries"]:
        if not entry:
            continue
        duration = entry.get("duration")
        if not duration:
            continue
        results.append ({
            "name": entry.get('title'),
            "video_url": f"https://youtube.com/watch?v={entry.get('id')}",
            "from": entry.get("uploader"),
            "duration": duration,
            "thumbnails": entry.get("thumbnails")
        })
    return results