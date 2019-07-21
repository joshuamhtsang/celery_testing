from youtube_download import download_yt_video

r = download_yt_video.delay('9GEs_TCLQdQ', 'out')
r.ready()
