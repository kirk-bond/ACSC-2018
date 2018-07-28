#!/usr/bin/env python3

import fcntl
import os
import subprocess
import tempfile

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = b"f6bd38bacb77fa4dc5f35c963109bbdf0f70454ca935123a"
socketio = SocketIO(app, binary=True)

PROCESSES = {}


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@socketio.on("connect")
def on_connect():
    print("connect", request.sid, request.remote_addr)


@socketio.on("disconnect")
def on_disconnect():
    print("disconnect", request.sid, request.remote_addr)
    proc = PROCESSES.get(request.sid)
    if proc is not None:
        proc.kill()
        del PROCESSES[request.sid]
        if os.path.isfile(proc.args[2]):
            os.unlink(proc.args[2])


@socketio.on("upload")
def on_upload(imagedata):
    print("upload", request.sid, request.remote_addr, len(imagedata))

    # kill any existing processes associated with this connection
    proc = PROCESSES.get(request.sid)
    if proc is not None:
        proc.kill()
        del PROCESSES[request.sid]
        if os.path.isfile(proc.args[2]):
            os.unlink(proc.args[2])

    # start a new session - this will clear the terminal
    emit("start-session")

    # drop to disk and execute the simulated bootloader with unbuffered stdout
    fd, imagepath = tempfile.mkstemp(suffix=".img", prefix="jr_")
    os.close(fd)
    with open(imagepath, "wb") as f:
        f.write(imagedata)

    proc = subprocess.Popen(["./signtool.py", "run", imagepath], stdout=subprocess.PIPE)
    flags = fcntl.fcntl(proc.stdout, fcntl.F_GETFL)
    fcntl.fcntl(proc.stdout, fcntl.F_SETFL, flags | os.O_NONBLOCK)
    PROCESSES[request.sid] = proc


@socketio.on("update")
def on_update():
    print("update", request.sid, request.remote_addr)

    # there should always be a process for this request. If not, someone is
    # poking our websocket interface.
    proc = PROCESSES.get(request.sid)
    if proc is None:
        emit("stop-session")
        return

    # try to read data from the process and send it to the client.
    try:
        data = os.read(proc.stdout.fileno(), 1024)
        data = data.replace(b"\n", b"\r\n")
        print(data)
        if data:
            emit("console", data.decode("utf-8"))
        else:
            emit("stop-session")    # process finished
            del PROCESSES[request.sid]
            if os.path.isfile(proc.args[2]):
                os.unlink(proc.args[2])
    except OSError:
        pass    # no data


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
