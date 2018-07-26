from fcntl import fcntl, F_GETFL, F_SETFL
import os
import subprocess

from flask import Flask, flash, redirect, render_template, request, session
from flask_socketio import SocketIO, disconnect, emit
from werkzeug.utils import secure_filename

import signtool

app = Flask(__name__)
app.config["SECRET_KEY"] = b"f6bd38bacb77fa4dc5f35c963109bbdf0f70454ca935123a"
socketio = SocketIO(app)

PROCESSES = {}

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

    print("GET", id(request), request.remote_addr)
    proc = subprocess.Popen("echo 'test' && sleep 1 && echo 'test2' && sleep 4 && echo 'test3'", shell=True, stdout=subprocess.PIPE)
    flags = fcntl(proc.stdout, F_GETFL)
    fcntl(proc.stdout, F_SETFL, flags | os.O_NONBLOCK)
    PROCESSES[id(request)] = proc
    return render_template("index.html")


@socketio.on("connect")
def on_connect():
    print("connect", id(request), request.sid, request.remote_addr)


@socketio.on("disconnect")
def on_disconnect():
    print("disconnect", id(request), request.sid, request.remote_addr)
    proc = PROCESSES.get(id(request))
    if proc is not None:
        proc.kill()
        del PROCESSES[id(request)]


@socketio.on("update")
def on_update():
    print("update", id(request), request.sid, request.remote_addr)
    proc = PROCESSES.get(id(request))
    if proc is not None:
        try:
            data = os.read(proc.stdout.fileno(), 1024)
            data = data.replace(b"\n", b"\r\n")
            print(data)
            if data:
                emit("console", {"data": data.decode("utf-8")})
            else:
                disconnect()
        except OSError:
            pass    # no data


if __name__ == "__main__":
    socketio.run(app)
