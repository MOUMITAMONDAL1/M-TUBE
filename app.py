from flask import Flask, request, render_template, send_from_directory
import yt_dlp
import os

app = Flask(__name__)
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    completed = False
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            try:
                ydl_opts = {
                    'format': 'best',
                    'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s')
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                message = "✅ Download completed successfully. <a href='/downloads' class='underline text-yellow-300 hover:text-yellow-100'>Check the 'downloads' folder</a>."
                completed = True
            except Exception as e:
                message = f"❌ Error: {str(e)}"
        else:
            message = "⚠ Please provide a valid URL."
    return render_template("index.html", message=message, completed=completed)

# Serve the downloads folder
@app.route("/downloads")
def serve_downloads():
    files = os.listdir(DOWNLOAD_FOLDER)
    return render_template("downloads.html", files=files)

# Serve individual files
@app.route("/downloads/<filename>")
def download_file(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)



import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

