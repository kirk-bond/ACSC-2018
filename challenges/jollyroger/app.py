import os

from flask import Flask, flash, redirect, render_template, request
from werkzeug.utils import secure_filename

import signtool

app = Flask(__name__)
app.config["SECRET_KEY"] = b"f6bd38bacb77fa4dc5f35c963109bbdf0f70454ca935123a"


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part", "warning")
            return redirect(request.url)
        image = request.files["file"]
        if image.filename == "":
            flash("No selected file", "warning")
            return redirect(request.url)

        imagedata = image.stream.read()
        try:
            signtool.verify_firmware(imagedata)
        except AssertionError as e:
            flash("Verify failed: {!s}".format(e), "error")
            print("Verify failed: {!s} ({:s})".format(e, image.filename))
            return redirect(request.url)
        except Excception as e:
            flash("Unknown verify error", "error")
            print("Unknown verify error: {!s} ({:s})".format(e, image.filename))
            return redirect(request.url)

        flash("Verify success! Executing firmware...", "success")
        print("Verify success! ({:s})".format(image.filename))
        return redirect(request.url)

    return render_template("index.html")
