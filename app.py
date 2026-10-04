from flask import Flask, render_template, send_from_directory
from pathlib import Path

app = Flask(__name__)

DOWNLOAD_FOLDER = Path(app.root_path) / "static" / "downloads"


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/descargar")
def descargar():
    archivo = "sirius.exe"
    return send_from_directory(
        DOWNLOAD_FOLDER,
        archivo,
        as_attachment=True,
        download_name="Sirius_3.0_Venus.exe"
    )


if __name__ == "__main__":
    app.run(debug=True)
