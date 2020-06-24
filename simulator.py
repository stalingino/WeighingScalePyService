#!/usr/bin/env python3
import http.server
import socketserver
from http import HTTPStatus
from random import random

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(str.encode(str(round(random() * 10 + 10, 3))))

httpd = socketserver.TCPServer(('', 3303), Handler)
httpd.serve_forever()
