"""Contrast, layout, and behavior checks against the built site."""

from __future__ import annotations

from playwright.sync_api import sync_playwright

BASE = "http://localhost:8000"
PAGES = ("/", "/couples/", "/narrators/")

NAVY, NAVY9, MUTE = "#1B2A4A", "#101B32", "#5A6B8C"
SUN, WHITE, WARM = "#FFC49B", "#FFFFFF", "#F2E4D8"
SUN_BRIGHT, SUN_INK = "#E2620B", "#BE4D02"

SOURCE_PX = 250  # the portrait sources; nothing may be displayed larger


def srgb(c: float) -> float:
    c /= 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def lum(hexcolor: str) -> float:
    h = hexcolor.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * srgb(r) + 0.7152 * srgb(g) + 0.0722 * srgb(b)


def blend(fg: str, bg: str, alpha: float) -> str:
    f, b = fg.lstrip("#"), bg.lstrip("#")
    return "#%02X%02X%02X" % tuple(
        round(int(f[i:i + 2], 16) * alpha + int(b[i:i + 2], 16) * (1 - alpha)) for i in (0, 2, 4)
    )


def ratio(a: str, b: str) -> float:
    la, lb = lum(a), lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


CHECKS = [
    ("body text on white", NAVY, WHITE, 4.5),
    # The home title is ~165px, which is large text, so the bar is 3:1.
    ("book title on white", SUN_BRIGHT, WHITE, 3.0),
    ("wordmark on white, small bold", SUN_INK, WHITE, 4.5),
    ("muted text on white", MUTE, WHITE, 4.5),
    ("display type on navy", SUN, NAVY, 3.0),
    ("body text on navy", WARM, NAVY, 4.5),
    ("footer text on deep navy", WARM, NAVY9, 4.5),
    ("footer note, 65% alpha", blend(WARM, NAVY9, 0.65), NAVY9, 4.5),
    ("sign-up text on orange", NAVY, SUN, 4.5),
    ("sign-up note, 75% alpha on orange", blend(NAVY, SUN, 0.75), SUN, 4.5),
    ("sign-up button label", SUN, NAVY, 4.5),
    ("focus ring on white", NAVY, WHITE, 3.0),
]


class Audit:
    def __init__(self) -> None:
        self.failures = 0

    def check(self, ok: bool, message: str) -> None:
        print(f"  {'ok  ' if ok else 'FAIL'} {message}")
        self.failures += not ok


DISCS = """() => Array.from(document.querySelectorAll(SEL)).map(el => {
  const img = el.querySelector('img'), r = img.getBoundingClientRect();
  const cs = getComputedStyle(el);
  return { disc: +(r.width * parseFloat(cs.getPropertyValue('--disc-w'))).toFixed(1),
           scale: +(SRC / r.width).toFixed(2) };
})"""


def discs(page, selector: str) -> list[dict]:
    return page.evaluate(DISCS.replace("SEL", repr(selector)).replace("SRC", str(SOURCE_PX)))


def main() -> int:
    audit = Audit()

    print("Contrast")
    for label, fg, bg, need in CHECKS:
        r = ratio(fg, bg)
        audit.check(r >= need, f"{r:5.2f}:1  (needs {need})  {label}")

    print("\nPortraits")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        errors: list[str] = []
        page.on("pageerror", lambda e: errors.append(str(e)))

        for path, selector, where in (
            ("/", ".pairing__who .por", "home, narrator links"),
            ("/narrators/", ".who .por", "narrators"),
        ):
            page.goto(f"{BASE}{path}", wait_until="networkidle")
            found = discs(page, selector)
            sizes = {d["disc"] for d in found}
            audit.check(len(sizes) == 1, f"{where}: all discs one diameter ({sizes})")
            worst = min(d["scale"] for d in found)
            audit.check(worst >= 1.0, f"{where}: never upscaled, tightest {worst}x the source")

        page.goto(f"{BASE}/", wait_until="networkidle")
        art = page.evaluate("""() => Array.from(document.querySelectorAll('.pairing__art img')).map(i => ({
          rendered: Math.round(i.getBoundingClientRect().width), natural: i.naturalWidth }))""")
        worst = min(a["natural"] / a["rendered"] for a in art)
        audit.check(worst >= 1.0, f"couple art never upscaled, tightest {worst:.2f}x ({len(art)} images)")

        scene = page.evaluate("""() => { const i = document.querySelector('.opening__scene img');
          return { rendered: Math.round(i.getBoundingClientRect().width), natural: i.naturalWidth }; }""")
        audit.check(scene["natural"] / scene["rendered"] >= 1.0,
                    f"opening scene never upscaled ({scene['natural']}/{scene['rendered']})")

        print("\nLayout")
        page.goto(f"{BASE}/couples/", wait_until="networkidle")
        tops = page.evaluate(
            "() => Array.from(document.querySelectorAll('.pair__name')).map(e => Math.round(e.getBoundingClientRect().top))"
        )
        audit.check(len(set(tops)) == 1, f"couples columns line up row by row ({tops})")

        overlaps = page.evaluate("""() => {
          const bad = [];
          document.querySelectorAll('.pair').forEach(el => {
            const boxes = Array.from(el.children).map(k => k.getBoundingClientRect());
            for (let i = 1; i < boxes.length; i++)
              if (boxes[i].top < boxes[i - 1].bottom - 1) bad.push(el.id + ' row ' + i);
          });
          return bad;
        }""")
        audit.check(not overlaps, f"couples columns stack without overlap ({overlaps or 'none'})")

        types = page.evaluate(
            "() => Array.from(document.querySelectorAll('.pair__image source')).map(s => s.type)"
        )
        audit.check(
            types.count("image/avif") == 3 and types.count("image/webp") == 3,
            f"couple images negotiate format through <picture> ({len(types)} sources)",
        )

        print("\nSharing")
        card = page.evaluate("""() => {
          const g = n => (document.querySelector(`meta[property="${n}"], meta[name="${n}"]`) || {}).content;
          return { url: g('og:image'), w: g('og:image:width'), h: g('og:image:height'),
                   alt: g('og:image:alt'), card: g('twitter:card') };
        }""")
        audit.check(bool(card["url"]) and card["url"].startswith("http"),
                    f"share image URL is absolute ({card['url']})")
        audit.check(card["w"] == "1200" and card["h"] == "630",
                    f"share image is declared 1200x630 ({card['w']}x{card['h']})")
        audit.check(bool(card["alt"]), "share image has alt text")
        audit.check(card["card"] == "summary_large_image",
                    f"twitter card type matches the image ({card['card']})")

        from pathlib import Path as _P
        from PIL import Image as _I
        path = _P(__file__).resolve().parent.parent / "static" / "img" / "share-card.jpg"
        with _I.open(path) as handle:
            size = handle.size
        audit.check(size == (1200, 630), f"share card file really is 1200x630 ({size[0]}x{size[1]})")

        print("\nBehavior")
        page.goto(f"{BASE}/narrators/", wait_until="networkidle")
        button = page.locator(".reveal__button").first
        panel = page.locator("#carries-connor")
        closed_first = not panel.is_visible()
        button.click()
        opened = panel.is_visible() and button.get_attribute("aria-expanded") == "true"
        button.click()
        closed = not panel.is_visible() and button.get_attribute("aria-expanded") == "false"
        audit.check(closed_first and opened and closed, "Tier 1 reveal toggles and reports aria-expanded")

        # Four of the six couple colours miss the 3:1 non-text minimum on white,
        # so no control boundary may depend on one. They stay decorative.
        border = page.evaluate(
            "() => getComputedStyle(document.querySelector('.reveal__button')).borderBottomColor"
        )
        audit.check(border == "rgb(27, 42, 74)", f"reveal control boundary is navy, not a couple colour ({border})")

        print("\nPages")
        for path in PAGES:
            page.goto(f"{BASE}{path}", wait_until="networkidle")
            headings = page.evaluate(
                "() => Array.from(document.querySelectorAll('h1,h2,h3')).map(h => +h.tagName[1])"
            )
            ok = headings and headings[0] == 1 and all(b - a <= 1 for a, b in zip(headings, headings[1:]))
            audit.check(ok, f"{path} headings start at h1 and never skip ({headings})")

            missing = page.evaluate("() => Array.from(document.images).filter(i => !i.alt).length")
            audit.check(not missing, f"{path} every image has alt text")

            overflow = page.evaluate(
                "() => document.documentElement.scrollWidth - document.documentElement.clientWidth"
            )
            audit.check(overflow <= 0, f"{path} no horizontal overflow at 1440px ({overflow}px)")

        audit.check(not errors, f"no JavaScript errors ({errors})")
        browser.close()

    print(f"\n{'All checks passed' if not audit.failures else str(audit.failures) + ' FAILURES'}")
    return 1 if audit.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
