"""
Generate favicon (32x32, 180x180) and OG social thumbnail (1200x630)
for lilanazemian.com, using the cosmos PNG from assets/.
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, math

BASE   = os.path.dirname(os.path.abspath(__file__))
COSMOS = os.path.join(BASE, "assets", "cosmos-flower-clipart-lg.png")
ASSETS = os.path.join(BASE, "assets")

# ── colours (from site palette) ──────────────────────────────────────────────
DARK_GREEN   = (57,  71,  34,  255)   # deep moss
MID_GREEN    = (90,  110, 70,  255)   # bio-box green
CREAM        = (245, 242, 237, 255)
LILAC        = (216, 176, 213, 255)
COSMOS_PINK  = (220, 88,  138, 255)   # warm pink of the cosmos in the .mov
GOLD         = (245, 208, 96,  255)

# ── helpers ───────────────────────────────────────────────────────────────────
def load_cosmos(size):
    img = Image.open(COSMOS).convert("RGBA")
    img = img.resize((size, size), Image.LANCZOS)
    return img

def tint(img, colour):
    """Recolour the non-transparent pixels of a RGBA image."""
    r, g, b, _ = colour
    data = img.getdata()
    out  = []
    for px in data:
        if px[3] > 10:
            out.append((r, g, b, px[3]))
        else:
            out.append((0, 0, 0, 0))
    img2 = img.copy()
    img2.putdata(out)
    return img2

# ── favicon 32×32 ─────────────────────────────────────────────────────────────
def make_favicon_32():
    size = 32
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    cosmos = load_cosmos(size)
    cosmos = tint(cosmos, COSMOS_PINK)
    canvas.paste(cosmos, (0, 0), cosmos)
    out = os.path.join(ASSETS, "favicon-32.png")
    canvas.save(out, "PNG")
    print("  favicon-32.png")
    return out

# ── Apple touch icon 180×180 ──────────────────────────────────────────────────
def make_touch_icon():
    size   = 180
    canvas = Image.new("RGBA", (size, size), MID_GREEN)
    cosmos = load_cosmos(int(size * 0.85))
    cosmos = tint(cosmos, CREAM)
    # centre it
    offset = (size - cosmos.width) // 2
    canvas.paste(cosmos, (offset, offset), cosmos)
    out = os.path.join(ASSETS, "apple-touch-icon.png")
    canvas.save(out, "PNG")
    print("  apple-touch-icon.png")

# ── OG / social thumbnail 1200×630 ────────────────────────────────────────────
def make_og():
    W, H = 1200, 630
    canvas = Image.new("RGBA", (W, H), DARK_GREEN)
    draw   = ImageDraw.Draw(canvas)

    # soft vignette — slightly lighter centre
    for y in range(H):
        for x in range(W):
            dx = (x - W/2) / (W/2)
            dy = (y - H/2) / (H/2)
            dist = math.sqrt(dx*dx + dy*dy)
            alpha = int(min(dist * 28, 40))
            draw.point((x, y), fill=(0, 0, 0, alpha))

    # large cosmos, right side, low opacity
    cosmos_bg = load_cosmos(580)
    cosmos_bg = tint(cosmos_bg, (90, 110, 70, 255))
    # make it translucent
    r2, g2, b2, a2 = cosmos_bg.split()
    a2 = a2.point(lambda p: int(p * 0.22))
    cosmos_bg = Image.merge("RGBA", (r2, g2, b2, a2))
    cx_offset = W - 560
    cy_offset = (H - 580) // 2 - 10
    canvas.paste(cosmos_bg, (cx_offset, cy_offset), cosmos_bg)

    # small crisp cosmos, left accent
    cosmos_sm = load_cosmos(90)
    cosmos_sm = tint(cosmos_sm, LILAC)
    canvas.paste(cosmos_sm, (72, H - 130), cosmos_sm)

    # title text — draw with default font scaled up; fall back gracefully
    try:
        # Try system serif fonts in order
        for fname in [
            "/System/Library/Fonts/Supplemental/Georgia.ttf",
            "/Library/Fonts/Georgia.ttf",
            "/System/Library/Fonts/Times.ttc",
        ]:
            if os.path.exists(fname):
                from PIL import ImageFont as IF
                font_title = IF.truetype(fname, 108)
                font_sub   = IF.truetype(fname, 28)
                break
        else:
            font_title = ImageFont.load_default()
            font_sub   = font_title
    except Exception:
        font_title = ImageFont.load_default()
        font_sub   = font_title

    # shadow
    draw.text((82, 222), "LILA", font=font_title, fill=(0, 0, 0, 80))
    draw.text((82, 332), "NAZEMIAN", font=font_title, fill=(0, 0, 0, 80))
    # main text
    draw.text((80, 220), "LILA",     font=font_title, fill=CREAM)
    draw.text((80, 330), "NAZEMIAN", font=font_title, fill=LILAC)
    # subtitle
    draw.text((84, 462), "Curator · Programs Director · Independent Writer",
              font=font_sub, fill=(216, 216, 200, 200))

    # thin horizontal rule
    draw.rectangle([(80, 456), (560, 457)], fill=(*LILAC[:3], 120))

    out = os.path.join(ASSETS, "og-image.png")
    canvas.convert("RGB").save(out, "PNG", optimize=True)
    print("  og-image.png")

# ── run ───────────────────────────────────────────────────────────────────────
print("Generating meta images…")
make_favicon_32()
make_touch_icon()
make_og()
print("Done.")
