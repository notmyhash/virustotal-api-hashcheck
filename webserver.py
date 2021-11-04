#!/usr/bin/env python

import http.server
import socketserver


def start(port):
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), Handler)
    print("Webserver started at port", port)
    httpd.serve_forever()
