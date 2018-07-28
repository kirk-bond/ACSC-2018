#!/usr/bin/env python3

from gevent.pywsgi import WSGIServer
from app import app

server = WSGIServer(("", 5000), app)
server.serve_forever()
