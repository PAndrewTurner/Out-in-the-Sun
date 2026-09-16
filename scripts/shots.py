"""Screenshot the built site at mobile and desktop widths for self review."""
from __future__ import annotations

import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "shots"
BASE = "http://localhost:8000"

VIEWS = {"mobile": (390, 844), "desktop": (1440, 960)}
PAGES = {"home": "/", "couples": "/couples/", "narrators": "/narrators/"}


def main() -> int:
    only = sys.argv[1:] or list(PAGES)
    OUT.mkdir(exist_ok=True)
    problems: list[str] = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for view, (w, h) in VIEWS.items():
            page = browser.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
            page.on("pageerror", lambda e: problems.append(f"JS error: {e}"))
            for name in only:
                page.goto(BASE + PAGES[name], wait_until="networkidle")
                page.wait_for_timeout(1400)
                page.screenshot(path=OUT / f"{name}-{view}.png", full_page=True)
                overflow = page.evaluate(
                    "() => document.documentElement.scrollWidth - document.documentElement.clientWidth"
                )
                if overflow > 0:
                    problems.append(f"{name} {view}: {overflow}px horizontal overflow")
                print(f"  {name}-{view}.png")
            page.close()
        browser.close()
    for problem in problems:
        print(f"PROBLEM: {problem}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
