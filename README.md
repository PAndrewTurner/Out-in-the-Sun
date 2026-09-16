# Out in the Sun

The promotional website for *Out in the Sun*, a literary queer romance novel by
P. Andrew Turner.

Live at <https://pandrewturner.github.io/Out-in-the-Sun/>.

## What is not in this repository

The manuscript. It lives in `private/`, which is gitignored, along with the
`Website Assets/` source illustrations and the working archive. Nothing in this
repository reads the manuscript. If you clone this repo you can build the site
straight away: the processed images are committed in `static/img/`, and only
`scripts/images.py` needs anything from `Website Assets/`.

## Working on it

```bash
uv sync                                    # install dependencies
uv run scripts/images.py                   # process approved images into static/img/
uv run build.py                            # build the site into dist/
uv run python -m http.server -d dist 8000  # preview at http://localhost:8000
```

With the preview server running:

```bash
uv run scripts/shots.py                    # screenshots at 390px and 1440px into shots/
uv run scripts/audit.py                    # contrast, keyboard, and heading checks
```

`scripts/fonts.py` downloads the three typefaces into `static/fonts/`. They are
committed, so it only needs running again if the type changes.

## How it is put together

- `content/*.yaml` holds every word on the site. `content/images.yaml` controls which
  illustrations are approved for processing.
- `templates/` is Jinja2. `static/css/site.css` declares every design token at the top.
- `build.py` renders the pages. `scripts/images.py` measures each portrait's painted disc into `data/portraits.json` so the six render at one size.
- Pushing to `main` builds and deploys through `.github/workflows/deploy.yml`.

`CLAUDE.md` is the full brief: canon, writing rules, image policy, and open decisions.
