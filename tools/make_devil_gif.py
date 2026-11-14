"""Generate devil.gif: a laughing devil with flickering flames, flashing eyes and popping 'HA' text."""
import math
import random
import sys

from PIL import Image, ImageDraw, ImageFont

OUT = sys.argv[1]
W = H = 160
N = 14
random.seed(7)

KEY = (255, 0, 255)  # transparent colour (magenta, far from every real colour)
PAL = [KEY, (0, 0, 0), (40, 0, 6), (95, 0, 14), (170, 0, 25), (255, 31, 61),
       (255, 110, 40), (255, 170, 20), (255, 225, 90), (255, 255, 255)]
BLACK, DEEP, DARK, MID, RED, ORANGE, AMBER, YELLOW, WHITE = PAL[1:]

pal_img = Image.new("P", (1, 1))
flat = [c for rgb in PAL for c in rgb] + [0, 0, 0] * (256 - len(PAL))
pal_img.putpalette(flat)

try:
    font = ImageFont.load_default(size=20)
except TypeError:
    font = ImageFont.load_default()

frames = []
for f in range(N):
    t = f / N * 2 * math.pi
    im = Image.new("RGB", (W, H), KEY)
    d = ImageDraw.Draw(im)
    bob = round(math.sin(t * 2) * 3)
    cx, cy = W // 2, 86 + bob

    # flames behind the head
    for i in range(9):
        x = 18 + i * 15.5
        h = 30 + 22 * abs(math.sin(t * 3 + i * 1.7)) + random.randint(0, 8)
        base = H - 6
        d.polygon([(x - 13, base), (x + 13, base), (x + random.randint(-4, 4), base - h)], fill=RED)
        d.polygon([(x - 8, base), (x + 8, base), (x + random.randint(-3, 3), base - h * 0.62)], fill=ORANGE)
        d.polygon([(x - 4, base), (x + 4, base), (x, base - h * 0.32)], fill=YELLOW)

    # horns
    d.polygon([(cx - 36, cy - 30), (cx - 52, cy - 70), (cx - 18, cy - 40)], fill=RED, outline=DARK)
    d.polygon([(cx + 36, cy - 30), (cx + 52, cy - 70), (cx + 18, cy - 40)], fill=RED, outline=DARK)

    # head
    d.ellipse([cx - 44, cy - 44, cx + 44, cy + 44], fill=RED)
    d.ellipse([cx - 40, cy - 40, cx + 40, cy + 40], fill=MID)
    d.ellipse([cx - 34, cy - 36, cx + 30, cy + 10], fill=DARK)  # shading

    # angry brows
    d.line([(cx - 30, cy - 22), (cx - 8, cy - 12)], fill=BLACK, width=5)
    d.line([(cx + 30, cy - 22), (cx + 8, cy - 12)], fill=BLACK, width=5)

    # flashing slit eyes
    eye = YELLOW if f % 4 < 2 else WHITE
    d.polygon([(cx - 30, cy - 14), (cx - 9, cy - 6), (cx - 28, cy - 2)], fill=eye)
    d.polygon([(cx + 30, cy - 14), (cx + 9, cy - 6), (cx + 28, cy - 2)], fill=eye)
    d.ellipse([cx - 22, cy - 10, cx - 17, cy - 5], fill=BLACK)
    d.ellipse([cx + 17, cy - 10, cx + 22, cy - 5], fill=BLACK)

    # laughing mouth: jaw opens and shuts
    open_ = 8 + round(14 * abs(math.sin(t * 3)))
    top = cy + 10
    d.chord([cx - 28, top - 10, cx + 28, top + open_ + 12], 0, 180, fill=BLACK, outline=RED, width=2)
    d.rectangle([cx - 27, top, cx + 27, top + 1], fill=RED)
    for fx in (-17, 11):  # fangs
        d.polygon([(cx + fx, top + 1), (cx + fx + 7, top + 1), (cx + fx + 3, top + 10)], fill=WHITE)
    if open_ > 14:
        d.ellipse([cx - 9, top + open_ - 2, cx + 9, top + open_ + 8], fill=ORANGE)  # tongue

    # goatee
    d.polygon([(cx - 7, cy + 40), (cx + 7, cy + 40), (cx, cy + 56)], fill=DEEP)

    # "HA" pops
    for k in range(2):
        if (f + k * 3) % 6 < 3:
            hx = random.choice([6, 12, W - 44, W - 50])
            hy = random.randint(4, 46)
            d.text((hx, hy), "HA", fill=YELLOW if k else RED, font=font, stroke_width=2, stroke_fill=BLACK)

    frames.append(im.quantize(palette=pal_img, dither=Image.Dither.NONE))

frames[0].save(OUT, save_all=True, append_images=frames[1:], duration=75, loop=0,
               transparency=0, disposal=2, optimize=False)
print("wrote", OUT, len(frames), "frames")
