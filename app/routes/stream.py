import yt_dlp

def get_stream_url(video_url):
    ydl_opt = {
        "format": 'bestaudio[ext=m4a]/bestaudio',
        'quiet': True,
        'noplaylist':True
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opt) as ydl:
            info = ydl.extract_info(video_url, download=False)
            if info.get("age_limit", 0) >= 18 or info.get("availability") == "needs_auth":
                return []
            return info["url"]
    except Exception:
        return []