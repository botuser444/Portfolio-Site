from PIL import Image
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
SRC = BASE / 'main' / 'static' / 'images' / 'portfoliologo.png'
ICO_OUT = BASE / 'main' / 'static' / 'favicon.ico'

if not SRC.exists():
    print(f"Source logo not found: {SRC}")
    raise SystemExit(1)

# Open image and save as multi-size ICO
img = Image.open(SRC)
# ensure RGBA for transparency
if img.mode != 'RGBA':
    img = img.convert('RGBA')

sizes = [(16,16),(32,32),(48,48),(64,64),(128,128),(256,256)]
try:
    img.save(ICO_OUT, format='ICO', sizes=sizes)
    print(f"Wrote {ICO_OUT}")
except Exception as e:
    print('Failed to write ICO:', e)
    raise
