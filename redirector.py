#!/usr/bin/env python3

# This script is an http redirector
# https://stackoverflow.com/questions/2506932/how-do-i-redirect-a-request-to-a-different-url-in-python
# sudo python3 redirector.py 800 http://127.0.0.1:8000/
# 
# https://realpython.com/python-http-server
# python3 -m http.server 8000
#
# test
# curl -v -L --insecure  http://127.0.0.1:800/dasfsdf

import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

if len(sys.argv)-1 != 2:
    print("""
Usage: {} <port_number> <url>
    """.format(sys.argv[0]))
    sys.exit()

class Redirect(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(302)
       self.send_header('Location', sys.argv[2])
       self.end_headers()

HTTPServer(("", int(sys.argv[1])), Redirect).serve_forever()
