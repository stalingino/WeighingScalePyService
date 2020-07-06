#!/usr/bin/env python3
import http.server
import socketserver
from http import HTTPStatus
from random import random

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.send_header("Cache-Control", "no-cache")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET,OPTIONS')
        self.end_headers()
        self.wfile.write(b'{"weight":"' + str.encode(str(round(random() * 10 + 10, 3))) + b'"}')

    def do_OPTIONS(self):
        self.send_response(HTTPStatus.OK)
        self.send_header("Cache-Control", "no-cache")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET,OPTIONS')
        self.end_headers()
        
httpd = socketserver.TCPServer(('', 3303), Handler)
httpd.serve_forever()
