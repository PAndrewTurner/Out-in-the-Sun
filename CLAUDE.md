# CLAUDE.md: Out in the Sun (showcase website)

This repo builds the promotional website for *Out in the Sun*, a literary queer romance novel by **P. Andrew Turner** (pen name). The site introduces the six narrators, the three couples, what each man carries, and how the book is built, so a reader finishes the visit wanting the book.

Andrew (the author) makes every creative decision. Claude proposes, Andrew approves, Claude builds. When Andrew clarifies intent, that clarification overrides any reading Claude brought to the text.

---

## 1. Ground rules (read first)

1. **The manuscript is the source of truth, and it is private.** It lives at `private/Out_in_the_Sun.md` and is gitignored. Never commit it, never copy long passages of it into `content/`, `dist/`, commit messages, or alt text. The public repo only ever holds derived data (chapter numbers, narrator names) and excerpts Andrew has approved.
2. **Never edit the manuscript.** This repo reads it; it does not change it.
3. **Propose before building.** For any new page, section, design direction, or piece of copy: show the plan or draft, wait for Andrew's approval, then implement. Work in small chunks and verify each one before moving on.
4. **Do not invent canon.** If a fact about a character (age, job detail, family, backstory, date) is not in Section 4 or confirmed in the manuscript, do not put it on the site. Ask.
5. **The site is safe for work; the book is not.** The novel contains explicit sex scenes. The website never shows or quotes explicit material.
6. **Act III is still being written.** Never present planned or unwritten beats as published fact.

---

## 2. Writing rules for all site copy

These apply to headlines, blurbs, character cards, alt text, meta descriptions, and button labels.

- **No em dashes.** Use commas, colons, periods, or parentheses.
- **American English** throughout (gray, cataloged, backward).
- Sentence case for headings and buttons. No all-caps labels.
- Avoid the manuscript's overused constructions in marketing copy too: "That's the thing," "for the record," "I want to be honest," "the specific quality of," and filler uses of *specific* / *particular*.
- Avoid mechanical vocabulary for anyone but Tyler: *apparatus, machinery, architecture, calibrated, recalibrated*.
- Show the people, do not diagnose them. Describe what a character does and wants; do not write clinical summaries of trauma responses.
- The book does not treat being gay as the conflict. Copy should not either. No coming-out framing, no "against all odds because they're gay" angle.
- Keep each block of copy to one job. Plain verbs. Specific over clever.

### Canon prohibitions (errors Andrew has already corrected)

- **Jealousy is not a theme.** Never name it in copy.
- **Nobody is actually falling out of love.** No couple in the book is losing the love or forcing themselves to keep it. Every obstacle is about letting love in, or what it costs.
- **Tyler's fear is a stack of what-ifs, and "what if we fall out of love and break up" is one of them** (Andrew's ruling, 2026-09-15, synopsis wins). Write it as something Tyler fears, never as something happening to him and Connor. The love is not in doubt; Tyler's confidence that it will last is.
- **Caleb is not analytical, robotic, or rigidly systematic.** He is warm, funny, and present. His guardedness comes from rejection history, not detachment.
- **Noah's guardedness is armor over real warmth,** not coldness.
- **Diego runs chronically late.** Never write him as early.
- **Rami does not worship Caleb's stretch marks.** He simply does not care about them. He is drawn to who Caleb is.
- **Diego's wound is the Miami traffic stop.** Do not substitute or add to it.
- The legal/testimonial register ("for the record," courtroom framing) belongs to Diego's voice only. Do not use it in other characters' voice samples.

---

## 3. What the site needs to do

**Audience:** adult readers of queer romance and literary fiction, early readers, agents/editors, and social followers.
**Primary job:** make someone care about six specific men in about ninety seconds.
**Secondary jobs:** capture interest (update sign-up), give press/agents a clean summary, and be highly shareable on social.

### Proposed site map (confirm with Andrew before building)

| Page | Purpose | Spoiler tier |
|---|---|---|
| Home | Title, pen name, one-line hook, the three couples at a glance, sign-up | 0 |
| The story | Premise and setting, spoiler-free | 0 |
| The couples | One section per couple: who they are together and the obstacle between them | 0 |
| The narrators | Six profiles: look, life, voice, what they carry | 0 visible, 1 behind a reveal |
| How it's told | The six-voice rotation across all chapters, and one "same moment, two narrators" pairing | 0 |
| Their Orlando | The real places in the book, as an illustrated map | 0 |
| Gallery (optional) | Only worth building once there are more images than the six portraits and three couple scenes, which already appear on their own pages | 0 |
| Content notes | Clear, calm list of what the book contains | n/a |

**Source copy:** `Website Assets/Out_in_the_Sun_Synopsis_and_Characters.md` is Andrew's own marketing synopsis and six character blurbs. Use it as the base for the Home, Story, and Narrator page copy rather than writing from scratch, but run every line through Section 2's writing rules and Section 4's canon before publishing, and resolve the Tyler conflict noted in Section 4 first.
| About the author | P. Andrew Turner, pen-name bio only, text supplied by Andrew | n/a |

### Spoiler tiers

- **Tier 0 (always visible):** premise, characters as introduced, the obstacle each couple faces, settings.
- **Tier 1 (behind a clearly labeled reveal, with a content note):** each character's wound in plain, non-graphic terms.
- **Tier 2 (do not publish without Andrew's explicit sign-off):** arc outcomes and late-book events. Examples: the LSAT result, the public kiss, the Key West finale, relationship milestones, the rupture and what follows it.

---

## 4. Canon reference

Verified against the manuscript and against `Website Assets/Out_in_the_Sun_Synopsis_and_Characters.md` (Andrew's own marketing synopsis, also treated as canon). If something here ever conflicts with the manuscript or with Andrew, the manuscript and Andrew win; flag the conflict rather than silently choosing. One live conflict is called out below and must be resolved with Andrew before it goes on the site.

> **Resolved 2026-09-15:** the synopsis wins. Tyler's fear is the whole run of what-ifs, including what if they fall out of love and break up, what if one of them gets sick, what if a job disappears. Andrew's earlier correction, that Tyler only fears the cost of losing Connor, is superseded. The one line still to hold in copy: Tyler *fears* this. It is not happening to him and Connor.

### The book

- Literary queer romance. About 80,000 words, 36 chapters (Act III in progress).
- Three gay couples in and around Orlando, Florida, over roughly a year. Side settings: Washington, D.C. (Noah's apartment, the National Mall, the Tidal Basin in cherry blossom season), Miami (Diego's past). The book closes in Key West (Tier 2).
- Tone for marketing copy, per Andrew's synopsis: warm, fun, and occasionally steamy. Six men, six voices, trying to love well and be loved back.
- Six rotating first-person narrators: Connor, Tyler, Diego, Noah, Rami, Caleb.
- Core idea: love is a decision you keep making, not a feeling that arrives. The interlocking POVs let readers see what one narrator cannot.
- Opens at an Out Pride Soccer League game on an unusually cool spring evening, where Connor watches Diego and Noah see each other for the first time.

### The couples

**Connor and Tyler: the foundation.** Together about five years. They met in Boston and moved to Florida together, about eight months before the book opens. Their obstacle is commitment: Connor is ready to build (a house in Winter Park, the practical next steps) and Tyler is terrified of what permanence would cost if he ever lost him.

**Diego and Noah: the spark.** They meet in Chapter 1. Diego is all momentum; Noah is careful. Their obstacle is the shadow of Noah's previous relationship with Luis, which taught Noah to read warmth as a threat.

**Rami and Caleb: the slow burn.** Longtime friends in the same circle. Rami has been quietly chasing Caleb for months; Caleb reads every sign of interest as kindness, because he cannot believe he is the one being wanted. Their obstacle is Caleb's inability to receive affection.

### The narrators

**Connor**
- The heart of the friend group, the one who connected everyone. Grew up in the Orlando area; his mother lives in Longwood.
- Financial analyst, background in finance and data science. Spent five years in Boston, where he met Tyler, then brought him home to Florida.
- Wants the permanence Tyler is scared of: the house, marriage, joint accounts, the visible symbols of commitment. He has been ready for a while.
- The group's reader. He notices everything, usually before anyone else, and often keeps it to himself. Kayaks the Econlockhatchee off Snow Hill Road.
- Look: bearded, warm, easy presence (see `Connor.png`).

**Tyler**
- Civil engineer (site inspections, structures). New England native. Studied calculus and statistics before engineering.
- Plays in the Out Pride Soccer League with Noah. Lean, clean-cut, short dark hair, angular face that gives little away until it decides to. Moves with economy.
- Deeply devoted to Connor. Left eight years of Boston life to come south with him, deliberately and without reservation.
- The only narrator for whom structural and mechanical language is native voice.
- Wound (Tier 1): commitment feels like adding load to a structure he has not finished checking. The what-ifs are what stop him: what if they fall out of love and break up, what if one of them gets sick, what if a job disappears. He is not falling out of love with Connor. He cannot make himself believe the load will hold.

**Diego**
- Studying for the LSAT; wants to be a trial lawyer. Believes that if he says enough words fast enough he can fix anything.
- Warm, unfiltered, impossible not to like. The smile arrives first. Chronically late.
- Voice: breathless, emotional, reactive, never detached.
- Wound (Tier 1): at twenty-two, a U.S. citizen, he was pulled over in Miami, detained as if he might not be from here, and charged with resisting while trying to prove his citizenship. The case was thrown out. The city settled with no admission of wrongdoing and nothing changed. He carries the lesson that being innocent may not matter.

**Noah**
- Political operative and LGBTQ+ advocate, Georgetown Law graduate. Splits his life between Orlando and his apartment in Washington, D.C.
- Dark-framed glasses, composed, measured. Plays soccer with Tyler. Always already there when you arrive.
- Warmth under armor. His rare, unmanaged smile is the payoff.
- Wound (Tier 1): five years with Luis, who was unfaithful and came to resent Noah's success. Noah still catches himself running threat assessment on kindness.

**Rami**
- Content creator known to millions of followers as "Zane," and a small business owner: he owns a clothing brand and has staff. Met Noah through advocacy work. Close with his friend Jodi.
- Palestinian heritage: tan skin, thick dark hair, green eyes, a smile that stops traffic.
- Reads rooms and intentions instantly. Voice is sharp, fast, funny, fashion-aware, less academic than Noah's.
- Wound (Tier 1): for years, men decided which part of him they wanted before he said a word. He let it happen because being wanted is fast and being loved is slow. **Do not quote or paraphrase the explicit language from his mirror monologue anywhere on the site.**

**Caleb**
- Data scientist; works two floors from Connor in the same building. Tall, well built, dark hair styled with care, clear-framed glasses. Nightly skincare routine.
- Lost 180 pounds over several years, through work Andrew's synopsis calls real and extraordinary. Completely oblivious to how often people look at him now. Warm, dry, genuinely funny (he once called Rami's gym shorts "a public service," completely straight-faced).
- Wound (Tier 1): the faint stretch marks left by that weight loss, which he keeps on purpose as a record of where he came from, and years of being overlooked that taught him anyone who got close would run the numbers and leave. He has not learned how to let himself be chosen.

---

## 5. Visual direction (proposal; get Andrew's approval before building)

Ground the design in the book, not in generic "romance novel" styling.

**Motifs from the text:** Florida heat and the sun itself (the title), the rainbow soccer jerseys, the Key West sunset, pink cherry blossoms against D.C. granite, the tea-dark water of the Econlockhatchee, Rami's mint shorts.

**Primary colors (set by Andrew, not up for debate):** pastel orange and navy blue. Together they carry the title: the warmth of the Florida sun against the deep blue of evening water. Every page is built on these two; everything else supports them.
- Pastel orange (the sun): starting point `#FFC49B`. Use for large fields, highlights, the sun ring, and warm backgrounds.
- Navy blue (the water and the night): starting point `#1B2A4A`. Use for primary text, headers, footers, and dark sections.
- Propose exact values, plus lighter and darker steps of each, for Andrew to approve. Check contrast: navy text on pastel orange should pass AA easily, but pastel orange text on white will not, so never use it for body text or small labels on light backgrounds. On navy, pastel orange works for text and buttons.

**Couple colors (secondary accents only)** (each couple owns one, used sparingly in cards, the POV rotation, and the map; they must never compete with orange and navy):
- Connor and Tyler: jersey blue, from Tyler's jersey, kept clearly lighter than the navy so the two never read as the same color. Starting point `#7FB3E0`.
- Diego and Noah: blossom pink, from the Tidal Basin. Starting point `#E98FAE`.
- Rami and Caleb: mint, from the shorts. Starting point `#8FD3BC`.

**Neutrals (supporting):** cool salt white `#F7F9F8` for light backgrounds and a soft warm gray for rules and captions. If a couple color clashes with the orange/navy pair, adjust the couple color, not the primaries.

**Avoid** (orange and navy are the brief; these apply to everything around them): warm cream backgrounds with a clay/terracotta accent, near-black with one neon accent, identical rounded card grids with soft shadows, all-caps eyebrow labels, `01 / 02 / 03` numbering on content that is not a sequence, fade-up animation on every section, and generic stock "rainbow gradient" pride styling.

**Signature element.** ~~A chapter ring.~~ Rejected by Andrew, 2026-09-15: he did not want an interactive sun, and the chapter data is no longer published at all. The site's identity now rests on scale and color blocking instead of a widget: the display face set at poster size (the home title runs to about 165px), a single navy full-bleed block per page carrying one sentence in pastel orange, and one orange band for the sign-up. Spend the boldness there and keep everything else quiet.

**Surfaces.** White carries the pages and the reading. Navy is the ink, and the one full-bleed block. Pastel orange is display type on navy, the sign-up band, and the couple markers. Each color has one job. Orange is never a field behind long text (at full-screen scale it reads pink) and never text on white (it fails AA badly).

**Type (approved 2026-09-15):** Fraunces for display, at weight 800 with the `SOFT` and `WONK` axes raised, which gives it an inked, slightly off-kilter quality at large sizes. Schibsted Grotesk for everything else: body, labels, buttons, captions. Two families, both self-hosted by `scripts/fonts.py`. Body line length under 80 characters.

**Illustrations:** all site art comes from `Website Assets/` and shares one painted, near-photoreal style in circular frames (see Section 6). Echo the circle in the layout, which fits the sun motif, rather than introducing competing shapes. Any new art should match this style.

Before writing code for a new design direction, produce a short plan (palette, type, layout wireframe in ASCII, principles), review it for generic defaults, then present it to Andrew.

---

## 6. Image policy

All source images live in the **`Website Assets/`** folder at the repo root. Treat it as read-only: never rename, move, edit, or delete files there. The folder name contains a space, so always quote it in shell commands (`"Website Assets/"`) and use `pathlib.Path("Website Assets")` in Python. Only files listed in `content/images.yaml` with `approved: true` are ever processed into `dist/`.

### Inventory (nine files)

All nine share one painted, near-photoreal illustration style, so the site uses that style throughout. None has transparency: each is a circle on a solid white background.

**Portraits (one per narrator).** Replaced 2026-09-15. All six are 250x250 with clean
transparency, a painted disc with the hair breaking out of the top, and consistent
framing, so sizing them to one disc diameter also gives them matching heads.

| File | Size | Disc | Background | What it shows |
|---|---|---|---|---|
| `Connor.png` | 250×250 | 90% of width | Ochre/tan | Bearded, three-quarter profile, chambray shirt, backpack straps |
| `Tyer.png` | 250×250 | 96% | Golden yellow | Clean-shaven, facing forward, blue quarter-zip over blue gingham |
| `Diego.png` | 250×250 | 90% | Deep green | Short dark hair, light beard, charcoal tee, slight smile |
| `Noah.png` | 250×250 | 93% | Navy with the U.S. Capitol dome | Dark-framed glasses, navy suit and tie, profile |
| `Rami.png` | 250×250 | 90% | Navy | Black rectangular glasses, stud earring, cream cable-knit hoodie |
| `Caleb.png` | 250×250 | 89% | Navy | Clear-framed glasses, gray quarter-zip over blue gingham |

Two things to raise with Andrew about this set:

1. **Tyler's file is named `Tyer.png`.** That looks like a typo. Sources are never renamed
   here, so `content/images.yaml` points at the name as it stands. Rename the source and
   that manifest line together, or leave both.
2. **These are smaller than the files they replaced,** which were about 410px wide. 250px
   caps how large a portrait can appear: the disc reaches 220px on the narrators page and
   200px on Home, and going beyond that means upscaling, which this repo does not do.
   Exports at 600px or more would allow noticeably larger portraits.

**Group illustration.** Added 2026-09-15.

| File | Size | Style | What it shows |
|---|---|---|---|
| `Group Photo.jpg` | 896×1195 | Watercolor, not the painted near-photoreal style of the rest | The six on a soccer sideline at golden hour, rainbow jerseys and pride flags, two of them kissing at the center |

Used only as the social sharing card, cropped by `scripts/images.py` to a 1200×630 band
centered at 47% of the source height, which puts all six in frame with the kiss in the
middle. Two things for Andrew:

1. **It is a different illustration style** from the nine painted portraits and couple
   images. That is fine for a share card, which is seen away from the site, but it would
   look out of place on a page. Do not put it on one without deciding that deliberately.
2. **It upscales 1.34x** to reach 1200×630, because the source is 896 wide. Soft
   watercolor hides this well, but a 1200px-wide export would be sharper.

**Couple images (one per couple, all 1254×1254, all full circles)**

| File | Scene | Notes |
|---|---|---|
| `Connor and Tyler Kiss.png` | Kissing on a brick sidewalk under autumn trees and gas lamps; Connor in a cable-knit cardigan, Tyler in a gray quarter-zip | The setting reads as Boston, not Orlando. Alt text and captions must not call it Orlando. |
| `Diego and Noah Kiss.png` | Kissing, shirtless, on a beach at sunset with palm trees | Tone check (shirtless). Possible spoiler (see below). |
| `Caleb and Rami Kiss.png` | Kissing across a candlelit table in a formal restaurant; Rami in a burgundy suit, Caleb in navy | Possible spoiler (see below). |

### How to use them

- **Do not crop portraits with `border-radius` or `clip-path`.** The heads are painted breaking out of the circle; masking would cut off the hair. Display each image as-is at its natural aspect ratio.
- **The white corners are part of the files.** On navy or pastel orange sections they will show as white squares. Either place images on light (white or salt) surfaces only, or have `images.py` generate transparent PNG/WebP versions by removing the near-white background outside the painted shape (flood fill from the corners, with a soft edge). Show Andrew a before/after of one portrait before processing the rest.
- **The portraits are 250px square.** Never display one wider than 250 CSS pixels, and never upscale. `scripts/images.py` writes 125px and 250px variants and measures each painted disc into `data/portraits.json`; the CSS divides a target disc size by that ratio so all six render identically whatever their framing. A larger portrait slot needs higher-resolution source art.
- **The six portrait backgrounds are different colors** (ochre, gold, green, and three navy). Present this to Andrew as a design decision: keep them as a deliberate mix, or request regenerated versions on a shared navy or pastel orange background.
- **Filenames are inconsistent** (`Caleb.png` vs `Caleb and Rami Kiss.png`, and `Tyer.png` is misspelled). Do not rename the sources. `images.py` should output normalized names: `portrait-connor`, `portrait-tyler`, `portrait-diego`, `portrait-noah`, `portrait-rami`, `portrait-caleb`, `couple-connor-tyler`, `couple-diego-noah`, `couple-rami-caleb`.
- **Source PNGs are heavy** (about 1.8 to 2.3 MB each). Always serve processed AVIF/WebP, sized for their slots.

### Flag these to Andrew before publishing

1. **Possible Tier 2 spoilers.**
   - `Caleb and Rami Kiss.png` looks like the restaurant kiss that concludes Caleb's arc.
   - `Diego and Noah Kiss.png` could read as the beach finale.
   - Ask whether each is safe to show, and where.
2. **Canon mismatches for Andrew to rule on.** Do not fix these or explain them away in copy.
   - In `Connor and Tyler Kiss.png`, Connor wears what looks like a wedding band. The book's central tension is Tyler's fear of commitment.
   - In `Rami.png`, Rami's eyes look brown, while the manuscript gives him green eyes.
3. **AI credit.** Whether to include a small credit noting the illustrations were created with AI tools. Recommend yes; Andrew decides.

### Other rules

- **Social sharing image:** `Group Photo.jpg`, cropped to 1200×630 by `scripts/images.py`
  and written as JPEG, because link scrapers lag browsers badly on AVIF and WebP. It is
  wired into `og:image` and `twitter:image` on every page with absolute URLs built from
  `site.origin`. If a version with the title and pen name set over it is ever wanted, that
  is a separate card, not a replacement for this one.
- **Public repo:** if the repo is public, add `Website Assets/` to `.gitignore` and deploy only the processed files in `dist/`.
- **Processing:** generate responsive AVIF and WebP (plus a PNG fallback where transparency is used), strip metadata, and write alt text for every image. Alt text is a plain description of the scene: no spoilers, no explicit language, and never invented settings.
- **New images:** if Andrew adds files to `Website Assets/`, inventory them in this section (size, framing, content, flags) before using them.

---

## 7. Content notes page

The book is for adult readers. The site should state that plainly and list content notes calmly, without drama. Draft list for Andrew to confirm:

- Explicit sexual content between adult men
- Racial profiling and police misconduct (a wrongful detention)
- Infidelity in a past relationship
- Sexual objectification (past experiences, discussed)
- Body image
- Strong language

The Tier 1 reveals on the narrators page link back to this page.

---

## 8. Excerpts

- Excerpts are optional and always Andrew-approved. Store them in `content/excerpts.yaml` with chapter, narrator, and an `approved` flag.
- Keep each under about 150 words. Never excerpt explicit scenes or Tier 2 material.
- Good candidates: the Chapter 1 sideline moment, Caleb's "public service" line, Diego and Noah's first café conversation.
- Excerpt text is reproduced exactly as written in the manuscript. Do not "fix" it.

---

## 9. Tech stack

Andrew works in Python on macOS. Keep the stack small, static, and Python-driven.

- **Python 3.12+**, managed with **uv** (`uv sync`, `uv run`).
- **Jinja2** templates, **PyYAML** for content, **Markdown** for longer text, **Pillow** (with AVIF support) for images.
- Hand-written HTML, CSS (custom properties for all design tokens), and a small amount of vanilla JavaScript for reveals and the POV ring. No frontend framework. No build step beyond `build.py`.
- **Playwright** (Python) for screenshots during self-review and for basic accessibility checks.
- **Hosting:** proposed GitHub Pages via GitHub Actions, or Cloudflare Pages. Confirm with Andrew. Either way, the manuscript never leaves `private/`.
- **Sign-up form:** needs a third-party email service (Buttondown, ConvertKit, etc.). Andrew chooses; until then, render a clearly marked placeholder.

### Layout

```
.
├── CLAUDE.md
├── pyproject.toml
├── build.py                 # renders content + templates into dist/
├── scripts/
│   ├── fonts.py             # downloads and self-hosts the two typefaces
│   ├── images.py            # approved images in "Website Assets/" -> resizing, AVIF/WebP in static/img/, and disc measurement
│   ├── shots.py             # screenshots every page at 390px and 1440px
│   └── audit.py             # contrast, portrait sizing, layout, and behavior checks
├── private/                 # gitignored: manuscript, unapproved notes
├── assets/
│   └── fonts/               # self-hosted fonts
├── Website Assets/          # source images, read-only (see Section 6)
├── content/
│   ├── site.yaml            # title, pen name, tagline, meta, social
│   ├── source/
│   │   └── synopsis.md      # copy of Website Assets/Out_in_the_Sun_Synopsis_and_Characters.md, for reference
│   ├── characters.yaml      # Section 4 as structured data, seeded from source/synopsis.md
│   ├── couples.yaml
│   ├── places.yaml
│   ├── images.yaml          # manifest with approved flags and alt text
│   └── excerpts.yaml
├── data/portraits.json      # measured painted disc per portrait, written by images.py
├── templates/               # Jinja2: base.html, partials/, pages/
├── static/                  # css/, js/, favicon, og images
└── dist/                    # build output, gitignored
```

**The site no longer reads the manuscript at all.** `chapter_index.py` and `data/chapters.json` were deleted on 2026-09-15 when Andrew dropped the chapter rotation from the site. Nothing in this repository opens `private/`.

### Commands

```bash
uv sync                                   # install deps
ls "Website Assets"                       # check what source images are available
uv run scripts/images.py                  # process approved images, measure the discs
uv run build.py                           # build the site into dist/
uv run python -m http.server -d dist 8000 # preview at http://localhost:8000
uv run scripts/shots.py                   # screenshots of every page, both widths
uv run scripts/audit.py                   # contrast, sizing, layout, behavior
```

---

## 10. Quality bar

- Responsive from 360px phones up. Test mobile first; most visitors will arrive from social links.
- WCAG 2.1 AA: color contrast (check the pink and mint especially), visible keyboard focus, semantic headings, reveals operable by keyboard with `aria-expanded`.
- Respect `prefers-reduced-motion`. One orchestrated motion moment at most.
- Performance: aim for under 1 MB on first load for the home page; lazy-load gallery images; self-host fonts with `font-display: swap`.
- Every page has a title, meta description, and Open Graph/Twitter card image (the designed share card from Section 6).
- No trackers or analytics unless Andrew asks for them.
- After each visual chunk, take screenshots at mobile and desktop widths, review them, and fix issues before presenting.

---

## 11. Workflow with Andrew

- Start each new area with a short proposal. Build only after approval.
- Present copy as drafts for Andrew to edit. Integrate his lines verbatim.
- When Andrew corrects a fact or a voice, fix it everywhere it appears and update Section 4 (or the relevant YAML) so it stays fixed.
- List any bulk find/replace across content files before running it.
- Keep a running `NOTES.md` of design ideas tried and decisions made.

## 12. Open decisions (ask before assuming)

1. Image flags from Section 6: possible spoilers in two couple images, Connor's ring, Rami's eye color, and whether to unify the portrait backgrounds.
2. ~~The Tyler conflict in Section 4.~~ Resolved 2026-09-15: synopsis wins, see Section 4.
3. Domain name and hosting target.
4. Email sign-up provider.
5. Whether to publish any Tier 1 material, and in what form. (Currently: yes, behind the labeled reveal on the narrators page.)
6. Which excerpts, if any.
7. ~~AI-illustration credit wording.~~ A one-line credit sits in the footer; reword or remove it in `templates/base.html`.
8. Whether to request higher-resolution portraits for larger display. The 2026-09-15 art is 250px, which caps the narrators page at a 221px disc. 600px exports would allow noticeably larger.
9. Author bio text and author photo (if any).
10. Launch status copy: "coming soon," "in progress," or a release window.
