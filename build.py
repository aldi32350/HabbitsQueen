"""Buat index.html (untuk localhost) dari habbits-queen.html.

Jalankan: python build.py
"""
import re
from pathlib import Path

root = Path(__file__).parent
src = (root / "habbits-queen.html").read_text(encoding="utf-8")

# <title> dan ikon tab harus ada di <head> supaya browser menampilkannya.
body = re.sub(r"<title>.*?</title>\s*", "", src, count=1, flags=re.S)
body = re.sub(r'<link rel="icon"[^>]*>\s*', "", body, count=1)

head = """<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Habits Queen</title>
<link rel="icon" type="image/svg+xml" href="logo.svg">
<link rel="apple-touch-icon" href="logo.svg">
<meta name="theme-color" content="#E43F86">
</head>
<body>
"""
(root / "index.html").write_text(head + body + "\n</body>\n</html>\n", encoding="utf-8")
print("index.html dibuat")
