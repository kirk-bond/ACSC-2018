from fcntl import fcntl, F_GETFL, F_SETFL
import os
import subprocess

from flask import Flask, flash, redirect, render_template, request
from flask_socketio import SocketIO, emit
from werkzeug.utils import secure_filename

import signtool

app = Flask(__name__)
app.config["SECRET_KEY"] = b"f6bd38bacb77fa4dc5f35c963109bbdf0f70454ca935123a"
socketio = SocketIO(app)

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


@socketio.on("upload")
def on_upload(imagedata):
    print("upload", request.sid, request.remote_addr, len(imagedata))
    imagedata = imagedata.encode()

    # kill any existing processes associated with this connection
    proc = PROCESSES.get(request.sid)
    if proc is not None:
        proc.kill()
        del PROCESSES[request.sid]

    # start a new session - this will clear the terminal
    emit("start-session")

    # try to verify the uploaded firmware
    try:
        signtool.verify_firmware(imagedata)
    except AssertionError as e:
        emit("console", "Verify failed: {!s}".format(e))
        emit("stop-session")
        print("Verify failed: {!s}".format(e))
        return
    except Excception as e:
        emit("console", "Unknown verify error")
        emit("stop-session")
        print("Unknown verify error: {!s}".format(e))
        return

    emit("console", "Verify success! Executing firmware...")
    print("Verify success!")

    # firmware verified successfully - drop to disk and execute
    proc = subprocess.Popen("echo 'test' && sleep 1 && echo 'test2' && sleep 4 && echo 'test3'", shell=True, stdout=subprocess.PIPE)
    flags = fcntl(proc.stdout, F_GETFL)
    fcntl(proc.stdout, F_SETFL, flags | os.O_NONBLOCK)
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
    except OSError:
        pass    # no data


if __name__ == "__main__":
    socketio.run(app)
