"""Serve dist/ for local preview.

Reads PORT from the environment so the preview harness can assign one. Nothing
here needs a fixed port: it is a static site with no callbacks or webhooks.

This only serves. Run `uv run build.py` to regenerate dist/ and refresh the
browser; an earlier version shelled out to the build first and hung before it
ever reached the socket.

    uv run scripts/serve.py
"""

from __future__ import annotations

import functools
import http.server
import os
import socketserver
from pathlib import Path

DIST = Path(__file__).resolve().parent.parent / "dist"


class NoCache(http.server.SimpleHTTPRequestHandler):
    """Serve dist/ and forbid caching.

    http.server sends Last-Modified but no ETag and no Cache-Control, so browsers
    cache heuristically and stop revalidating. That showed up as a page rendering
    against a stylesheet from several edits ago, which looks like a broken build
    and is not one.
    """

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


def main() -> int:
    port = int(os.environ.get("PORT", "8000"))
    handler = functools.partial(NoCache, directory=str(DIST))
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", port), handler) as server:
        print(f"Serving {DIST} on http://localhost:{port}", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
