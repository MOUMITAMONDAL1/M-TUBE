import yt_dlp

yt_dlp.YoutubeDL({"format":'best','outtmpl':"%(title)s.%(ext)s"}).download(('https://youtu.be/FOwFHvt0IiU?si=1-pR_y6fQOqAjVG6'))