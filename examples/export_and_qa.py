# Font-verified PNG export + pixel QA for the channel diagram example.
# Usage: python export_and_qa.py
# Runs the export with a fonts-ready assertion (unicode-range aware), then
# pixel-QAs the result: safe margins, legend band, accent presence, bbox.
from playwright.sync_api import sync_playwright
from PIL import Image
import pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "channel-architecture-example.html"
OUT = HERE / "channel-architecture-example.png"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(device_scale_factor=2)
    page.goto(f"file://{SRC.resolve()}")
    page.wait_for_load_state("networkidle")
    # unicode-range pitfall: check() is false on an empty probe — load with
    # sample text first, then check (channel memory: live-verified method)
    loaded = page.evaluate("""async () => {
        await document.fonts.ready;
        await document.fonts.load('630 16px MiSans', 'VIEWER QUESTIONS TRIAGE');
        await document.fonts.load('380 16px MiSans', 'viewer question');
        await document.fonts.load('600 16px Inter', 'Triage agent');
        return {
            misans630: document.fonts.check('630 16px MiSans'),
            misans380: document.fonts.check('380 16px MiSans'),
            inter600: document.fonts.check('600 16px Inter'),
        };
    }""")
    print("font probe:", loaded)
    ok = all(loaded.values())
    print("fonts loaded:", "YES" if ok else "NO - FALLBACK RENDER RISK")
    page.locator("svg").first.screenshot(path=str(OUT), omit_background=True)
    browser.close()

# ---- pixel QA (visual-qa skill: structure checks) ----
im = Image.open(OUT).convert("RGBA")
W, H = im.size
print(f"size: {W}x{H} (expect 2560x1440)")

alpha = im.getchannel("A")
bbox = alpha.getbbox()  # content bbox: None if fully transparent
px = im.load()

def band_content(y0, y1, x0=0, x1=None):
    x1 = x1 or W
    n = 0
    for y in range(y0, y1, 4):
        for x in range(x0, x1, 4):
            if px[x, y][3] > 16:
                n += 1
    return n

issues = []
if bbox:
    l, t, r, b = bbox
    print(f"content bbox: L{l} T{t} R{r} B{b}")
    # 40px viewBox margin x scale 2 = 80px PNG
    if l < 80 or t < 80: issues.append(f"content violates top/left safe margin: {l},{t}")
    if r > W - 80: issues.append(f"content violates right margin: {r}")
    # bottom edge handled by the legend-band checks below (40px margin +
    # 60px legend strip), not by a flat bottom-margin assertion
else:
    issues.append("fully transparent image - nothing rendered")

# Bottom chrome per output-spec: 40px margin for diagram content, PLUS a
# 60px legend strip at the bottom (legend-only zone). viewBox 720, scale 2:
# non-legend content must end above y 640 (1280 PNG); legend must stay
# within y 660-720 and clear of the edge (>=32 PNG px = 16 viewBox px).
LEGEND_BAND_TOP = int((720 - 60) * 2)   # 1320
NODE_ZONE_BOTTOM = int((720 - 80) * 2)  # 1280: 40px margin + 60px legend

def row_has_content(y, x0=0, x1=None):
    x1 = x1 or W
    return any(px[x, y][3] > 16 for x in range(x0, x1, 4))

node_bottom = max((y for y in range(0, NODE_ZONE_BOTTOM, 4) if row_has_content(y)), default=0)
legend_bottom = max((y for y in range(LEGEND_BAND_TOP, H, 4) if row_has_content(y)), default=0)
print(f"node content bottom: {node_bottom} (limit {NODE_ZONE_BOTTOM})")
print(f"legend content bottom: {legend_bottom} (limit {H - 32})")
if node_bottom >= NODE_ZONE_BOTTOM:
    issues.append(f"diagram content intrudes into bottom chrome: {node_bottom}")
if legend_bottom > H - 32:
    issues.append(f"legend too close to bottom edge: {legend_bottom}")
# and nothing between the node zone and the legend band (dead row check)
gap_rows = sum(1 for y in range(NODE_ZONE_BOTTOM, LEGEND_BAND_TOP, 4) if row_has_content(y))
if gap_rows > 4:
    issues.append(f"unexpected content between node zone and legend band: {gap_rows} rows")

# nothing above the legend band should sit inside the bottom 120px zone
stray = 0
for y in range(H - 240, H - 120, 2):  # band just above legend strip
    for x in range(0, W, 2):
        if px[x, y][3] > 16:
            stray += 1
if stray > 40: issues.append(f"unexpected content in pre-legend band (~y {H-240}-{H-120}): {stray} samples")

# accent presence: count purple-family pixels
accent_n = 0
for y in range(0, H, 3):
    for x in range(0, W, 3):
        r_, g_, b_, a_ = px[x, y]
        if a_ > 200 and 90 <= r_ <= 160 and 70 <= g_ <= 140 and b_ >= 220:
            accent_n += 1
print("accent px samples:", accent_n)
if accent_n < 50: issues.append("brand accent missing or nearly absent")

print("QA:", "CLEAN" if not issues else "ISSUES")
for i in issues: print("  -", i)
sys.exit(0 if ok and not issues else 1)
