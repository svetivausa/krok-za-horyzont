#!/usr/bin/env python3
"""Simple dev server for krok-za-horyzont (strips .html extension)."""
import http.server, os, socketserver

PORT = 3456
ROOT = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def translate_path(self, path):
        # Remove query string
        path = path.split('?', 1)[0]
        # Try exact file first
        result = super().translate_path(path)
        if os.path.isfile(result):
            return result
        # Try appending .html
        html = result.rstrip('/') + '.html'
        if os.path.isfile(html):
            return html
        return result

    def log_message(self, fmt, *args):
        pass  # quiet

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print(f'Serving on http://localhost:{PORT}')
    httpd.serve_forever()
