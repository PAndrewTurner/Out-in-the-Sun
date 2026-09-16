"""Process approved source images into dist/img/.

Reads only the entries flagged approved: true in content/images.yaml. Source
files in "Website Assets/" are never renamed, moved, or written to.

Each portrait is a painted disc with the hair painted breaking out of the top of
the disc. Eight of the nine sources already carry clean transparency and are used
as they are. Only "Tyler Portrait.png" is flat RGB on a white field, and that one
white field is removed by flood filling inward from the four corners, so the
painted shape, including the hair that crosses the edge, survives. Nothing is
ever masked with a circle.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml
from PIL import Image, ImageChops, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "Website Assets"
MANIFEST = ROOT / "content" / "images.yaml"
METRICS = ROOT / "data" / "portraits.json"
OUT_DIR = ROOT / "static" / "img"

# The 2026-09-15 portraits are 250x250. Never upscale a source, so 250 is the
# largest variant and the largest size the site may display one at.
PORTRAIT_WIDTHS = (125, 250)
COUPLE_WIDTHS = (400, 800)
# The group watercolor is 896 wide, so 896 is the largest honest size.
SCENE_WIDTHS = (448, 896)

# Every major scraper expects this, and several ignore anything smaller.
SHARE_SIZE = (1200, 630)

SENTINEL = (255, 0, 255)
WHITE_TOLERANCE = 36


def has_transparency(image: Image.Image) -> bool:
    if "A" not in image.getbands():
        return False
    low, _ = image.getchannel("A").getextrema()
    return low < 250


def cut_background(image: Image.Image) -> Image.Image:
    """Return an RGBA copy with any white field outside the painted shape removed.

    Sources that already carry transparency are returned untouched. Removing a
    background that is not there would only risk damaging the artwork.
    """
    if has_transparency(image):
        return image.convert("RGBA")

    rgb = image.convert("RGB")
    probe = rgb.copy()
    width, height = probe.size
    corners = ((0, 0), (width - 1, 0), (0, height - 1), (width - 1, height - 1))

    for corner in corners:
        if sum(probe.getpixel(corner)) < 3 * (255 - WHITE_TOLERANCE):
            # This corner is already part of the artwork. Leave it alone.
            continue
        ImageDraw.floodfill(probe, corner, SENTINEL, thresh=WHITE_TOLERANCE)

    red, green, blue = probe.split()
    filled = ImageChops.multiply(
        ImageChops.multiply(
            red.point(lambda v: 255 if v == SENTINEL[0] else 0),
            green.point(lambda v: 255 if v == SENTINEL[1] else 0),
        ),
        blue.point(lambda v: 255 if v == SENTINEL[2] else 0),
    )
    alpha = ImageChops.invert(filled)

    # Pull the edge in by a hair, then feather it, so no white fringe survives
    # from the anti-aliased boundary in the source.
    alpha = alpha.filter(ImageFilter.MinFilter(3))
    alpha = alpha.filter(ImageFilter.GaussianBlur(0.7))

    out = rgb.convert("RGBA")
    out.putalpha(alpha)
    return out


def write_variants(image: Image.Image, name: str, widths: tuple[int, ...]) -> list[str]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    written: list[str] = []
    for width in widths:
        height = round(image.height * width / image.width)
        resized = image.resize((width, height), Image.LANCZOS)
        formats = [(".avif", {"quality": 62}), (".webp", {"quality": 82, "method": 6})]
        if width == min(widths):
            # One PNG, at the smallest size only. It is the last-resort fallback
            # in the img src; every current browser takes the avif or the webp,
            # so a second large PNG would only be repository weight.
            formats.append((".png", {"optimize": True}))
        for suffix, kwargs in formats:
            path = OUT_DIR / f"{name}-{width}{suffix}"
            # Rebuild from raw bytes so no source metadata rides along.
            clean = Image.frombytes("RGBA", resized.size, resized.tobytes())
            clean.save(path, **kwargs)
            written.append(path.name)
    return written


def share_card(entry: dict) -> None:
    """Crop the group illustration to a 1200x630 social sharing card.

    Written as JPEG rather than AVIF or WebP: link scrapers are years behind
    browsers on format support, and a card nobody can decode is worse than a
    slightly larger one.
    """
    source = SOURCE_DIR / entry["source"]
    with Image.open(source) as handle:
        image = handle.convert("RGB")

    width, height = image.size
    band = round(width * SHARE_SIZE[1] / SHARE_SIZE[0])
    top = max(0, min(height - band, round(height * entry["focus"] - band / 2)))
    card = image.crop((0, top, width, top + band)).resize(SHARE_SIZE, Image.LANCZOS)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUT_DIR / f"{entry['name']}.jpg"
    clean = Image.frombytes("RGB", card.size, card.tobytes())  # drops metadata
    clean.save(path, quality=88, optimize=True, progressive=True)
    scale = SHARE_SIZE[0] / width
    print(f"  {entry['name']}.jpg from {entry['source']}, rows {top}-{top + band}, {scale:.2f}x")


def measure_disc(path: Path) -> dict[str, float]:
    """Fit the painted disc in a portrait and report its size and top edge.

    The disc is a circle, so one measurement fits it exactly: the widest run of
    opaque pixels is its diameter, and the row that run falls on is its vertical
    centre, so the top is centre minus radius. Measuring the top directly would
    fail, because the topmost opaque pixel is hair painted breaking out above the
    circle, not the circle.

    An earlier version measured the head instead, on the reasoning that the eye
    compares faces rather than circles. That was right for the first set of art,
    where the six were framed differently. It is wrong for these: the 2026-09-15
    portraits are framed consistently, so equal circles already give equal heads,
    and head detection is unreliable at 250px, cutting off at the nose or the
    eyes. An exact measurement of the right thing beats an approximate
    measurement of a better thing.

    Returns the diameter as a fraction of the image's width, which the CSS
    divides into a target disc size, and the top as a percentage of its height.
    """
    with Image.open(path) as handle:
        alpha = handle.convert("RGBA").getchannel("A")
    width, height = alpha.size

    widest = center_y = 0
    for y in range(height):
        row = alpha.crop((0, y, width, y + 1)).tobytes()
        opaque = [x for x, value in enumerate(row) if value > 128]
        if not opaque:
            continue
        run = opaque[-1] - opaque[0] + 1
        if run > widest:
            widest, center_y = run, y

    top = max(0.0, center_y - widest / 2)
    return {
        "disc_w": round(widest / width, 4),
        "disc_top": round(top / height * 100, 2),
    }


def process(entries: list[dict], widths: tuple[int, ...], label: str) -> int:
    count = 0
    for entry in entries:
        if not entry.get("approved"):
            print(f"  skipping {entry['name']}, not approved")
            continue
        source = SOURCE_DIR / entry["source"]
        if not source.exists():
            print(f"  ERROR: missing source {source}", file=sys.stderr)
            continue
        with Image.open(source) as handle:
            cut = cut_background(handle)
        write_variants(cut, entry["name"], widths)
        print(f"  {entry['name']} from {entry['source']} ({cut.width}x{cut.height})")
        count += 1
    print(f"{count} {label} processed")
    return count


def preview(name: str) -> None:
    """Write a single before and after pair for review, without touching dist/."""
    manifest = yaml.safe_load(MANIFEST.read_text())
    entries = manifest["portraits"] + manifest["couples"]
    entry = next((e for e in entries if e["name"] == name), None)
    if entry is None:
        raise SystemExit(f"No manifest entry named {name}")

    out = ROOT / "shots"
    out.mkdir(exist_ok=True)
    with Image.open(SOURCE_DIR / entry["source"]) as handle:
        before = handle.convert("RGBA")
        after = cut_background(handle)

    # Show both on the navy the site actually uses, so the white corners are visible.
    navy = (27, 42, 74, 255)
    pad = 24
    w = before.width + after.width + pad * 3
    h = max(before.height, after.height) + pad * 2
    sheet = Image.new("RGBA", (w, h), navy)
    sheet.alpha_composite(before, (pad, pad))
    sheet.alpha_composite(after, (pad * 2 + before.width, pad))
    path = out / f"{name}-before-after.png"
    sheet.convert("RGB").save(path)
    print(f"Wrote {path.relative_to(ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preview", metavar="NAME", help="write one before/after sheet and stop")
    args = parser.parse_args()

    if args.preview:
        preview(args.preview)
        return 0

    manifest = yaml.safe_load(MANIFEST.read_text())
    print("Portraits:")
    process(manifest["portraits"], PORTRAIT_WIDTHS, "portraits")
    print("Couple images:")
    process(manifest["couples"], COUPLE_WIDTHS, "couple images")

    print("Scenes:")
    process(manifest.get("scenes", []), SCENE_WIDTHS, "scenes")

    print("Social card:")
    for entry in manifest.get("social", []):
        if entry.get("approved"):
            share_card(entry)
        else:
            print(f"  skipping {entry['name']}, not approved")

    print("Disc measurements:")
    metrics = {}
    for entry in manifest["portraits"]:
        if not entry.get("approved"):
            continue
        metrics[entry["name"]] = measure_disc(OUT_DIR / f"{entry['name']}-{max(PORTRAIT_WIDTHS)}.webp")
        print(f"  {entry['name']}  {metrics[entry['name']]}")
    METRICS.parent.mkdir(parents=True, exist_ok=True)
    METRICS.write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {METRICS.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
