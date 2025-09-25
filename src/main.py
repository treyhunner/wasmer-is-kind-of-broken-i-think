import os
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer
from random import randint

numbers = []


class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        numbers.append(randint(0, 9))
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        data = {
            "message": "Python app on Wasmer: {','.join(numbers)}"
        }
        self.wfile.write(json.dumps(data).encode('utf-8'))


if __name__ == "__main__":
    host = os.environ.get('HOST', '127.0.0.1')

    # Get the PORT environment variable if it's present; otherwise, default to 8000
    port = int(os.environ.get('PORT', 80))

    server = HTTPServer((host, port), CustomHandler)
    print(f"Starting server on http://{host}:{port}")
    server.serve_forever()
