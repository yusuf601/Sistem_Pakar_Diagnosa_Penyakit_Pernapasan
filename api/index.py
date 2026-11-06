import os
import sys

# Tambahkan direktori root proyek ke sys.path agar app.py dan modul lainnya terbaca
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from app import app

# Vercel requires the app variable to be exposed
