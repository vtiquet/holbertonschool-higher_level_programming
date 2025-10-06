#!/usr/bin/python3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

SAMPLE_DATA = {"name": "John", "age": 30, "city": "New York"}

INFO_DATA = {"version": "1.0", "description": "A simple API built with http.server"}

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    Handles GET requests for the basic API endpoints: /, /data, and /status.
    """
    def do_GET(self):
        if self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response_content = json.dumps(SAMPLE_DATA)
            self.wfile.write(response_content.encode('utf-8'))

        elif self.path == '/status':
            response_content = "OK"
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(response_content.encode('utf-8'))

        elif self.path == '/':
            response_content = "Hello, this is a simple API!"
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(response_content.encode('utf-8'))

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response_content = json.dumps(INFO_DATA)
            self.wfile.write(response_content.encode('utf-8'))

        else:
            error_message = "Endpoint not found"
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(error_message.encode('utf-8'))


def run(server_class=HTTPServer,
        handler_class=SimpleHTTPRequestHandler, port=8000):
    """
    Sets up and runs the HTTP server.
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping httpd server.")
        httpd.server_close()


if __name__ == '__main__':
    run()
