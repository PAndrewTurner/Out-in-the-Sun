"""Render content and templates into dist/.

Everything the site knows comes from content/*.yaml and data/portraits.json.
The manuscript is not read here, or anywhere else in this repository.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from PIL import Image

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
DIST = ROOT / "dist"


def load_yaml(name: str):
    return yaml.safe_load((CONTENT / name).read_text(encoding="utf-8"))


def image_height(name: str, width: int = 250) -> int:
    """Real height of a processed image, so nothing is ever squashed.

    Reads the webp, because the PNG fallback is only written at the smallest size.
    """
    with Image.open(ROOT / "static" / "img" / f"{name}-{width}.webp") as handle:
        return handle.height


def favicon() -> str:
    """A pastel orange sun on navy, in a browser tab."""
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
        '<rect width="64" height="64" rx="12" fill="#1B2A4A"/>'
        '<circle cx="32" cy="32" r="17" fill="#FFC49B"/>'
        "</svg>"
    )


def main() -> int:
    site = load_yaml("site.yaml")
    characters = load_yaml("characters.yaml")
    couples = load_yaml("couples.yaml")
    # Written by scripts/images.py, which measures each painted disc so the six
    # portraits can be sized and aligned identically. Rerun it if the art changes.
    portraits = json.loads((ROOT / "data" / "portraits.json").read_text(encoding="utf-8"))

    base = os.environ.get("SITE_BASE_URL", site.get("base_url", "")).rstrip("/")
    by_slug = {c["slug"]: c for c in characters}

    for person in characters:
        person.update(portraits[person["portrait"]])
        person["h"] = image_height(person["portrait"])

    for couple in couples:
        couple["people"] = [by_slug[slug] for slug in couple["narrators"]]

    # Home introduces the six in the order the couples are introduced, so the
    # faces read left to right as three pairs. The bio pages use the same order,
    # which is what "before him" and "after him" walk through.
    ordered = [person for couple in couples for person in couple["people"]]

    for couple in couples:
        for person in couple["people"]:
            person["couple"] = couple["slug"]
            person["couple_name"] = couple["name"]
            person["couple_billing"] = couple["billing"]
            person["couple_summary"] = couple["summary"]
            person["couple_tint"] = couple["tint"]

    for index, person in enumerate(ordered):
        person["prev"] = ordered[index - 1]
        person["next"] = ordered[(index + 1) % len(ordered)]

    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        autoescape=True,
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    def url(path: str = "") -> str:
        return f"{base}/{str(path).lstrip('/')}"

    def asset(path: str) -> str:
        """A URL that changes whenever the file does.

        Without this, a returning visitor can be handed new HTML and a cached
        stylesheet from the previous deploy.
        """
        digest = hashlib.md5((ROOT / path).read_bytes()).hexdigest()[:8]
        return f"{url(path)}?v={digest}"

    env.globals["url"] = url
    env.globals["asset"] = asset

    shared = {
        # The narrowest painted disc across the six. Every portrait is scaled so
        # its own disc matches this fraction of its box, which makes all six
        # render at one diameter whatever the framing of each file.
        "disc_norm": min(m["disc_w"] for m in portraits.values()),
        "site": site,
        "characters": characters,
        "ordered": ordered,
        "couples": couples,
    }

    pages = [
        ("index.html", "", "index.html"),
        ("couples.html", "couples/", "couples/index.html"),
        ("narrators.html", "narrators/", "narrators/index.html"),
    ]
    pages += [
        ("narrator.html", f"narrators/{p['slug']}/", f"narrators/{p['slug']}/index.html")
        for p in ordered
    ]

    for template_name, href, output in pages:
        person = next((p for p in ordered if href == f"narrators/{p['slug']}/"), None)
        html = env.get_template(f"pages/{template_name}").render(
            page_href=href, person=person, **shared
        )
        target = DIST / output
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8")
        print(f"  {output}  {len(html) // 1024} KB")

    static_out = DIST / "static"
    if static_out.exists():
        shutil.rmtree(static_out)
    shutil.copytree(ROOT / "static", static_out)
    (DIST / "static" / "favicon.svg").write_text(favicon(), encoding="utf-8")
    (DIST / ".nojekyll").write_text("", encoding="utf-8")

    print(f"Built into {DIST.relative_to(ROOT)} with base {base or '/'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
