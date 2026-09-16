# Out in the Sun: site design spec

Date: 2026-09-15. Approved by Andrew. Supersedes the first design in the same file,
which is preserved in NOTES.md.

## Scope

Three pages: Home, The couples, The narrators. Static, built by `build.py`, deployed to
GitHub Pages at `https://pandrewturner.github.io/Out-in-the-Sun/`.

No availability or launch-status language. The sign-up is a clearly marked placeholder.

## Direction

White carries the pages and the reading. Navy is the ink, and one full-bleed block per
page carrying a single sentence. Pastel orange is display type on navy, the sign-up
band, and the couple markers. Each color has exactly one job.

Two constraints the palette imposes, both measured rather than assumed:

- Pastel orange is never a field behind long text. At full-screen scale `#FFC49B` reads
  peach-pink rather than sun.
- Pastel orange is never text on white: 1.54:1. The book's own title is set in a
  brighter, denser step of the same hue instead, because a book called *Out in the Sun*
  should not have its title in navy. Section titles on the other pages stay navy; only
  the book's name is orange.

There is no signature widget. The boldness is spent on scale: the home title runs to
about 165px, the rules are 2px navy rather than hairline gray, and the navy block is
edge to edge rather than a tinted panel.

## Tokens

| Token | Hex | Job |
|---|---|---|
| `--white` | `#FFFFFF` | the page |
| `--navy` | `#1B2A4A` | ink, and the full-bleed block |
| `--navy-900` | `#101B32` | footer |
| `--mute` | `#5A6B8C` | secondary text on white, 5.36:1 |
| `--sun` | `#FFC49B` | display type on navy, sign-up band, couple markers |
| `--sun-bright` | `#E2620B` | the book's title on white, 3.51:1, large text only |
| `--sun-ink` | `#BE4D02` | the wordmark, small bold on white, 4.94:1 |
| `--warm` | `#F2E4D8` | body text on navy, 11.42:1 |
| `--line` | `#DCE2E8` | rules between rows |

Couple colors stay as in the original brief and are used only as markers, rules, and
the reveal arrow. Four of the six miss the 3:1 non-text minimum on white, so no control
boundary depends on one.

## Type

Fraunces for display at weight 800 with `SOFT` and `WONK` raised. Schibsted Grotesk for
everything else. Both self-hosted, 168 KB total.

## Portraits

Sized and aligned by the painted disc measured in `scripts/images.py` and written to
`data/portraits.json`, so all six render at one diameter on every page whatever the
framing of each file. Never masked with `border-radius`: the hair is painted breaking
out of the circle. Sources are 250px, so nothing is displayed larger than that.

## Content

All narrative prose is Andrew's own, kept verbatim: the home synopsis, the six narrator
blurbs, and the couple summaries. Check `content/source/synopsis.md` before writing any
new prose about the book. Site
furniture is written to the Section 2 rules in CLAUDE.md. The chapter rotation is no
longer published, and the site does not read the manuscript.

## Quality bar

Responsive from 360px. WCAG 2.1 AA contrast, visible keyboard focus, semantic headings,
reveals operable by keyboard with `aria-expanded`. Home first load 138 KB. No trackers.
`scripts/audit.py` asserts all of it.
