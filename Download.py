import yt_dlp

url = input("Enter YouTube URL: ")

ydl_opts = {
    "format": "best",
    "outtmpl": "YouTube/%(title)s.%(ext)s",
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download Complete!")
