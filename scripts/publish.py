"""Publish the working tree to GitHub without git.

Only needed because the system git is Apple's stub and refuses to run until the
Xcode licence is accepted, which needs a password this cannot supply:

    sudo xcodebuild -license

Once that is done, use git normally and delete this. Until then, this uploads
every publishable file through GitHub's Git Data API and moves refs/heads/main,
which produces an ordinary commit that the Pages workflow builds from.

    uv run scripts/publish.py "Commit message"
"""

from __future__ import annotations

import base64
import json
import subprocess
import sys
from pathlib import Path

REPO = "PAndrewTurner/Out-in-the-Sun"
ROOT = Path(__file__).resolve().parent.parent

# Anything here never leaves the machine. The manuscript lives in private/ and
# the unprocessed illustrations in "Website Assets/".
EXCLUDE_DIRS = {"private", "Website Assets", "Archive", "Charcters", "New Photos",
                "dist", "shots", ".venv", "__pycache__", ".ruff_cache", ".git"}
EXCLUDE_SUFFIXES = {".pyc", ".docx", ".pages"}
EXCLUDE_NAMES = {".DS_Store"}

ATTRIBUTION = "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"


def api(path: str, payload=None, method: str | None = None):
    cmd = ["gh", "api", f"repos/{REPO}/{path}"]
    if method:
        cmd += ["-X", method]
    if payload is not None:
        cmd += ["--input", "-"]
    result = subprocess.run(
        cmd, input=json.dumps(payload) if payload is not None else None,
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise SystemExit(f"GitHub API failed on {path}:\n{result.stderr}")
    return json.loads(result.stdout)


def publishable() -> list[Path]:
    found = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if set(relative.parts) & EXCLUDE_DIRS:
            continue
        if relative.suffix in EXCLUDE_SUFFIXES or relative.name in EXCLUDE_NAMES:
            continue
        found.append(relative)
    return found


def main() -> int:
    message = sys.argv[1] if len(sys.argv) > 1 else "Update the site"
    files = publishable()

    leaks = [f for f in files if f.name == "Out in the Sun.md" or "private" in f.parts]
    if leaks:
        raise SystemExit(f"Refusing to publish: {leaks}")

    total = sum((ROOT / f).stat().st_size for f in files)
    print(f"{len(files)} files, {total / 1024 / 1024:.2f} MB")

    head = api("git/ref/heads/main")["object"]["sha"]

    tree = []
    for index, relative in enumerate(files, 1):
        content = base64.b64encode((ROOT / relative).read_bytes()).decode()
        blob = api("git/blobs", {"content": content, "encoding": "base64"})
        tree.append({"path": str(relative), "mode": "100644", "type": "blob", "sha": blob["sha"]})
        if index % 20 == 0 or index == len(files):
            print(f"  uploaded {index}/{len(files)}", flush=True)

    tree_sha = api("git/trees", {"tree": tree})["sha"]
    commit = api("git/commits", {
        "message": f"{message}\n\n{ATTRIBUTION}",
        "tree": tree_sha,
        "parents": [head],
    })
    api("git/refs/heads/main", {"sha": commit["sha"]}, method="PATCH")

    print(f"\nPushed {commit['sha'][:10]}")
    print("Pages will rebuild. Watch it with:")
    print(f"  gh run watch --repo {REPO}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
