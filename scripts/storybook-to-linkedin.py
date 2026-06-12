#!/usr/bin/env python3
"""
Convert eUICC.tech storybooks to LinkedIn carousel PDFs.
Extracts each page by finding <div class="page boundaries, wraps in
standalone HTML with original dark theme CSS, renders with Playwright,
and assembles into square PDF slides.

Usage:
    python3 storybook-to-linkedin.py storybook-07          # single
    python3 storybook-to-linkedin.py --all                 # all 52
    python3 storybook-to-linkedin.py --all --spec sgp32    # SGP.32 only

Output: /tmp/linkedin-carousels/<name>.pdf
"""

import argparse
import io
import os
import re
import sys
import tempfile
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Install Pillow: pip install Pillow")
    sys.exit(1)

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Install playwright: pip install playwright && playwright install chromium")
    sys.exit(1)

STORYBOOKS_DIR = Path("/home/alex/Repos/esim-knowledge/docs/articles/kids")
OUTPUT_DIR = Path("/tmp/linkedin-carousels")
SLIDE = 1080
RENDER_W = 800
RENDER_H = 1200

# Dark navy theme CSS — extracted from storybook styles
PAGE_STYLES = """
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Georgia',serif;background:#0a1628;color:#c8d6e5;overflow:hidden}
.page-wrapper{width:100%;height:100vh;display:flex;flex-direction:column;
  align-items:center;justify-content:center;padding:2.5rem 2rem;
  background:#0a1628}
h1{font-size:2.2rem;color:#e8eef5;text-align:center;margin-bottom:.5rem}
h2{font-size:1.3rem;color:#85c1e9;text-align:center;font-weight:400;margin-bottom:1.5rem}
h3{font-size:1.15rem;color:#5dade2;text-align:center;margin-bottom:1rem}
.story-text{font-size:1.1rem;line-height:1.8;text-align:center;max-width:550px;margin:0 auto}
.story-text em{color:#85c1e9;font-style:italic}
.story-text strong{color:#e8eef5}
.illustration{margin:1.2rem 0}
.illustration svg{max-width:100%;height:auto;max-height:450px}
.page-num{color:#5a6d80;font-size:.85rem}
@keyframes twinkle{0%,100%{opacity:.3}50%{opacity:1}}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
.floating{animation:float 3s ease-in-out infinite}
.sparkle{animation:twinkle 2s infinite}
"""


def extract_pages_raw(html_content):
    """
    Extract each page's HTML using regex to find <div class="page boundaries.
    Preserves SVG case (viewBox, radialGradient, etc.) unlike BeautifulSoup.
    Returns list of (page_html_snippet, page_label).
    """
    # Find all .page div openings (class="page" or "page page-cover", but NOT .page-num)
    pattern = r'<div\s+class="page(?: page-cover)?"[^>]*>'
    page_starts = list(re.finditer(pattern, html_content))
    if not page_starts:
        return []

    pages = []
    for i, m in enumerate(page_starts):
        start_pos = m.start()

        # Find where this page's content ends and next page begins
        if i + 1 < len(page_starts):
            end_pos = page_starts[i + 1].start()
        else:
            # Last page — find closing </div> that balances
            # Simple approach: find the last </div> in the document
            end_pos = len(html_content)

        page_html = html_content[start_pos:end_pos]

        # Strip the outermost <div class="page..."> wrapper but keep content
        # Remove opening tag
        inner = re.sub(r'^<div\s+class="page[^"]*"[^>]*>', '', page_html, count=1)
        # Remove trailing </div> (last one)
        inner = re.sub(r'</div>\s*$', '', inner, count=1)

        if inner.strip():
            pages.append(inner)

    return pages


def wrap_page_html(content, page_num, total_pages):
    """Wrap extracted page content in standalone HTML with dark theme."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>{PAGE_STYLES}</style>
</head>
<body>
<div class="page-wrapper">
{content}
<div class="page-num" style="margin-top:1.5rem">Page {page_num} of {total_pages}</div>
<div style="margin-top:.5rem;font-size:11px;color:#4a5d6e;font-family:system-ui,sans-serif">
  📖 euicc.tech
</div>
</div>
</body>
</html>"""


def list_storybooks(spec_filter=None):
    storybooks = []
    for f in sorted(STORYBOOKS_DIR.glob("storybook-*.html")):
        name = f.stem
        content = f.read_text()
        title_match = re.search(r"<title>(.*?)</title>", content)
        title = title_match.group(1) if title_match else name

        if spec_filter == "sgp22":
            m = re.search(r"storybook-0?(\d+)", name)
            num = int(m.group(1)) if m else 999
            if num > 6:
                continue
        elif spec_filter == "sgp32":
            m = re.search(r"storybook-0?(\d+)", name)
            num = int(m.group(1)) if m else 999
            if num < 7 or num > 16:
                continue
        elif spec_filter == "sgp02":
            if "sgp02" not in name:
                continue

        storybooks.append((name, title, f))
    return storybooks


def convert_storybook(name, title, filepath):
    """Convert one storybook to a LinkedIn carousel PDF."""
    output_pdf = OUTPUT_DIR / f"{name}.pdf"

    raw_html = filepath.read_text()
    pages = extract_pages_raw(raw_html)

    if not pages:
        print(f"  ✗ {name}: no pages extracted")
        return None, ""

    total = len(pages)
    images = []

    with sync_playwright() as p:
        browser = p.chromium.launch()

        for idx, content in enumerate(pages):
            wrapped = wrap_page_html(content, idx + 1, total)

            with tempfile.NamedTemporaryFile(suffix='.html', mode='w', delete=False) as tf:
                tf.write(wrapped)
                temp_path = tf.name

            try:
                pg = browser.new_page(viewport={"width": RENDER_W, "height": RENDER_H})
                pg.goto(f"file://{temp_path}", timeout=10000)
                pg.wait_for_timeout(1500)

                screenshot = pg.screenshot(full_page=False)
                img = Image.open(io.BytesIO(screenshot))

                w, h = img.size
                scale = min(SLIDE / w, SLIDE / h)
                new_w, new_h = int(w * scale), int(h * scale)
                img_resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)

                canvas = Image.new("RGB", (SLIDE, SLIDE), (10, 22, 40))
                canvas.paste(img_resized, ((SLIDE - new_w) // 2, (SLIDE - new_h) // 2))
                images.append(canvas)

                pg.close()
            finally:
                os.unlink(temp_path)

        browser.close()

    if not images:
        print(f"  ✗ {name}: no images generated")
        return None, ""

    print(f"  {name}: {len(images)} slides → {output_pdf.name}")

    first = images[0].convert("RGB")
    rest = [img.convert("RGB") for img in images[1:]]
    first.save(str(output_pdf), save_all=True, append_images=rest)
    print(f"    ✓ {output_pdf.stat().st_size // 1024} KB")

    short_title = title.replace(": An eSIM Story", "").replace(": Storybook", "").strip()
    short_title = re.sub(r'\s+\d+$', '', short_title)
    post_text = (
        f"🔐 {short_title}\n\n"
        f"Illustrated breakdown of eSIM technology — no jargon, clear visuals.\n\n"
        f"👉 Full story: euicc.tech/articles/kids/{name}.html\n\n"
        f"#eSIM #IoT #Telecom #TechExplained"
    )
    (OUTPUT_DIR / f"{name}.post.txt").write_text(post_text)

    return str(output_pdf), post_text


def main():
    parser = argparse.ArgumentParser(description="Storybooks → LinkedIn PDF carousels")
    parser.add_argument("storybook", nargs="?", help="Storybook name (e.g. storybook-07)")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--spec", choices=["sgp22", "sgp32", "sgp02"])
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if args.all:
        storybooks = list_storybooks(args.spec)
        print(f"Converting {len(storybooks)} storybooks...\n")
        for name, title, filepath in storybooks:
            try:
                convert_storybook(name, title, filepath)
            except Exception as e:
                print(f"  ✗ {name}: {e}")
        print(f"\nDone! PDFs in {OUTPUT_DIR}/")
    elif args.storybook:
        filepath = STORYBOOKS_DIR / f"{args.storybook}.html"
        if not filepath.exists():
            candidates = sorted(STORYBOOKS_DIR.glob(f"*{args.storybook}*.html"))
            if candidates:
                print("Not found. Did you mean?")
                for c in candidates:
                    print(f"  {c.stem}")
            else:
                print(f"Not found: {filepath}")
            sys.exit(1)
        content = filepath.read_text()
        title_match = re.search(r"<title>(.*?)</title>", content)
        title = title_match.group(1) if title_match else args.storybook
        pdf_path, post_text = convert_storybook(args.storybook, title, filepath)
        if pdf_path:
            print(f"\nPost copy:\n{post_text}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
