import os
import sys

# Tambahkan direktori root proyek ke sys.path agar app.py dan modul lainnya terbaca
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from app import app

# Middleware untuk memastikan path /api/index diubah kembali menjadi /
class StripPrefixMiddleware:
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        path = environ.get("PATH_INFO", "")
        if path.startswith("/api/index"):
            new_path = path[len("/api/index"):]
            environ["PATH_INFO"] = new_path if new_path else "/"
        return self.wsgi_app(environ, start_response)

app.wsgi_app = StripPrefixMiddleware(app.wsgi_app)

# Vercel requires the app variable to be exposed
