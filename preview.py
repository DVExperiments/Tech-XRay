"""Optional local preview helper (Python standard library, no packages or keys).
Opens Tech X-Ray from http://localhost:<port>/ for stable browser storage.
"""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
from pathlib import Path
import webbrowser
import os

ROOT=Path(__file__).resolve().parent
os.chdir(ROOT)
server=ThreadingHTTPServer(('127.0.0.1',0),partial(SimpleHTTPRequestHandler,directory=str(ROOT)))
port=server.server_address[1]
url=f'http://127.0.0.1:{port}/'
print(f'\nTech X-Ray preview is running: {url}\nPress Ctrl+C to stop.\n')
webbrowser.open(url)
try:server.serve_forever()
except KeyboardInterrupt:pass
finally:server.server_close()
