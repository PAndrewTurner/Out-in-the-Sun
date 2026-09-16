# Notes

Design ideas tried and decisions made, newest first.

## 2026-09-15: published, without git

The site is live at https://pandrewturner.github.io/Out-in-the-Sun/.

The system git is Apple's stub and still refuses every command until the Xcode licence
is accepted, which needs a password. There is no Homebrew git on this machine either. So
the first publish went through GitHub's Git Data API instead: a blob per file, one tree,
one commit, then move refs/heads/main. The Pages workflow saw an ordinary push and built
from it normally.

One gotcha: the Git Data API returns 409 on a repository with zero commits. Seed one file
through the Contents API first, which does work on an empty repo, then the tree-based
path is available.

`scripts/publish.py` wraps this so it is repeatable, with the same exclusion list as
.gitignore and a hard refusal if the manuscript or anything under private/ ever appears
in the file list. Delete it once `sudo xcodebuild -license` has been run and real git
works.

Verified live: all three pages 200, fonts and images served, og:image absolute and
reachable, and the manuscript path 404s.

## 2026-09-15: social sharing card

Andrew added `Group Photo.jpg`, a watercolor of the six on the soccer sideline, to be
the sharing image focused on the middle where the couples are interacting.

The source is portrait, 896x1195, and a share card is landscape 1200x630, so the crop is
a full-width band. `scripts/images.py` takes it centered at 47 percent of the source
height, which was the one of three candidates that kept every head in frame with the
kiss in the middle. The focus fraction lives in `content/images.yaml` so it is tunable
without touching code.

Written as JPEG on purpose. Link scrapers lag browsers badly on AVIF and WebP, and a
card that Slack or iMessage cannot decode is worse than a slightly larger one.

Two things flagged in CLAUDE.md: it is a watercolor, not the painted near-photoreal
style of the other nine, so it suits a card seen away from the site but would look out
of place on a page; and it upscales 1.34x to reach 1200 wide.

`og:image` needs an absolute URL, so `site.yaml` gained an `origin` that is prefixed to
the path. The audit checks the URL is absolute, the declared dimensions match, the alt
text exists, the Twitter card type is `summary_large_image`, and the file on disk really
is 1200x630.

## 2026-09-15: Noah and Diego, in that order

Andrew asked for Noah's portrait first, then Diego's, and the pair titled "Noah and
Diego". One change in `content/couples.yaml` propagates to all three pages: the six
faces on Home, the couple row, the couples page, and the order of the narrator entries.

It surfaced a hidden coupling worth removing. `build.py` derived each couple's marker
colour from whichever narrator was listed first, so reordering the pair silently
switched the colour from Diego's blossom pink to Noah's deeper step. The colour CLAUDE.md
names for that couple is the pink, so `tint` is now stated outright in `couples.yaml`
rather than inferred from list order. Derive nothing from ordering that is meant to be a
brand decision.

Not changed: the internal image name `couple-diego-noah` and the anchor `#diego-noah`,
which are the normalised names Section 6 specifies and are never visible.

## 2026-09-15: the home blurb is Andrew's synopsis

I had written the navy block's copy myself, a pull quote plus a paragraph. Andrew
preferred his own synopsis, which is the second time I have invented prose where his
already existed. Section 3 of the brief says to use his synopsis as the base and not to
write from scratch, and I have now broken that twice.

His synopsis is in `content/site.yaml` verbatim and set as the block's only content,
like a jacket blurb, at about 37px. The invented display line is gone. Everything
narrative on the site is now his words: the six narrator blurbs, the home synopsis, and
the couple summaries.

Standing rule for this project: before writing any prose about the book, check
`content/source/synopsis.md` first.

## 2026-09-15: the title is orange

Andrew: setting "Out in the Sun" in navy is contradictory. Correct, and worth the two
extra tokens.

The constraint is that the pastel is 1.54:1 on white, so no small adjustment to it is
legible. The title is about 165px, which counts as large text and needs 3:1, so
`#E2620B` at 3.51:1 is roughly the brightest orange that clears it with margin. The
wordmark in the masthead is small bold text and needs the full 4.5:1, so it takes
`#BE4D02` at 4.94:1.

Two oranges on one page turned out to read as a light and a deep step of one hue, which
is what CLAUDE.md Section 5 asks for anyway. Section titles on the other pages stay
navy, so only the book's own name is orange.

## 2026-09-15: redesign, bolder and more modern

Andrew asked for a redesign. The honest diagnosis of what was wrong: the palette was
diluted (orange only ever appeared as a 10 percent wash, so the identity lived in maybe
15 percent of the pixels), nothing was at poster scale, and every section was a centred
column of the same width and rhythm. Polite, not bold.

**Five mockups before one landed, and each rejection taught something.**

1. Navy page, giant interactive sun, orange blocks. Rejected: 36 saturated couple
   colours as a pinwheel competed with the primaries, which Section 5 forbids.
2. Same with the sun enlarged so the rays became a thin corona. Better, but Andrew did
   not want an interactive sun at all, and the navy blocked with the three navy-backed
   portraits.
3. Orange as the dominant field. Solved the blending outright, but at full-screen scale
   `#FFC49B` reads peach-pink rather than sun. Rejected.
4. Back to navy with a pastel orange disc behind each portrait. Solved blending as an
   accent rather than a field. Andrew then said to drop the discs.
5. **White as the main surface.** Andrew's note that whites were fair game unlocked it.
   Every one of the six painted backgrounds separates on white, so the blending problem
   disappears with nothing added.

**The lesson worth keeping:** two of these rounds were spent treating a background
problem as a decoration problem. The portraits carry their own baked-in backgrounds, so
the fix was always to choose a page colour none of them share, not to add rings, discs
or mats on top.

**What shipped.** White surface, navy ink, one navy full-bleed block per page carrying a
single sentence in pastel orange, one orange sign-up band. Fraunces 800 with WONK at
poster scale; the home title runs to about 165px. Schibsted Grotesk replaced Newsreader
and Atkinson, which is two families instead of three and 108 KB lighter.

**Dropped:** the chapter ring, `scripts/chapter_index.py`, `data/chapters.json`, and
`static/js/ring.js`. The site no longer reads the manuscript at all.

**Accessibility finding:** four of the six couple colours miss the 3:1 non-text minimum
on white (Rami's mint is 1.72:1). So no control boundary may depend on one. The reveal
button's underline is navy; the colours stay on the arrow, the panel rule, and the
markers, all decorative and all redundant with text. The audit asserts that underline
stays navy.

The previous design is copied to `private/pre-redesign/` since git still is not
initialised here.

## 2026-09-15: new 250x250 portrait art

Andrew replaced all six portraits. New files are 250x250 with clean transparency, and
three have new names: `Caleb.png`, `Noah.png`, and `Tyer.png`, which is a misspelling of
Tyler. Sources are never renamed here, so `content/images.yaml` points at `Tyer.png` as
it stands and both the manifest and CLAUDE.md say why.

**Reverted to disc normalization.** The head-based scaling was the right answer for the
old art, where the six were framed differently. It is the wrong answer here. The new set
is framed consistently, so equal circles already give equal heads, and head detection
falls apart at 250px: the shoulder-gradient method cut off at the nose or the eyes on
four of six. Checked by drawing the boxes, as usual, and then checked the replacement by
compositing all six at an identical disc and confirming the heads line up. An exact
measurement of the circle beats an approximate measurement of the head.

Measurement still lives in `scripts/images.py` and still writes `data/portraits.json`.

**The new files are smaller than the ones they replace**, 250px against about 410px, so
the portraits had to come down: 220px disc on the narrators page against about 243px, and
200px on Home. Variants are now 125 and 250 rather than 200 and 400, and the audit
asserts nothing is ever upscaled. Larger portraits need larger exports, 600px or more.

A bug this caught: the CSS still declared `--head` on `.person__portrait` while the img
rule had been switched to read `--disc`. An undefined custom property makes the whole
`calc()` invalid, so `width` silently fell back to the intrinsic size and every portrait
rendered at 247px regardless of its framing. It looked plausible, which is exactly why
the audit asserts equal diameters rather than trusting the stylesheet.

## 2026-09-15: portraits enlarged properly

Andrew: revert the images, they're tiny. Checked before reverting, because a revert
would have made them smaller, not larger. Measured: the head-normalization pass had
already made every image 6 to 13 percent BIGGER than the equal-circle version it
replaced. So "tiny" was not about that change. They were simply too small in absolute
terms, and had been for several rounds, because I kept defending a 2x retina rule that
was my constraint rather than his.

Heads now render at 168px on the narrators page (portraits about 265 to 281px wide, up
from roughly 200) and 140px on Home. The narrators column widened to 60rem to hold it.

The sharpness floor dropped from 1.7x to 1.35x of source, and the widest-framed portrait
now lands at 1.42x. On soft painted illustration that is fine. It would not be fine on
line art or text, and the audit still asserts a floor so it cannot slide further without
someone noticing.

Lesson: check the direction of a change before reverting it. "Go back" and "make it
bigger" pointed opposite ways here, and only one of them was the actual goal.

## 2026-09-15: portraits normalize on the head, not the circle

Andrew: enlarge the photos as necessary to make them all equal. Correct instinct, and
the opposite of what I had built. I was sizing by the painted circle, which is the part
nobody looks at. The eye compares faces.

Sized by circle, Tyler's head rendered about six percent larger than Connor's. My
earlier measurement claimed the reverse, and it was wrong: the head-height detection
was picking up shoulders. The one that works finds the shoulder line as the sharpest
widening in the subject's silhouette and takes everything above it, from the topmost
opaque pixel, which is hair. Verified by drawing the box back onto all six and looking:
hair-top to chin on every one.

Head measurement now lives in `scripts/images.py`, which already opens these files, and
writes `data/portraits.json`. `build.py` reads it. Previously build.py re-analysed six
images on every single build, which was both slow and the wrong place for it.

All six now render at exactly the same head size, 115px on Home and 136px on the
narrators page, aligned to the same top. The circles come out slightly different as a
result, up to about six percent, which is unavoidable: equal heads and equal circles
cannot both be true when the art is framed differently. Equal heads is the one that
matters.

Resolution cost: Noah and Diego are framed widest, so they scale up the most and render
at about 1.76x source on the narrators page rather than 2x. On soft painted art that is
invisible, but the audit now asserts nothing falls below 1.7x, so a future size increase
cannot quietly blur them.

## 2026-09-15: the overlap was the problem, not the scale

Andrew, twice: Tyler does not match Connor. I kept checking the scaling, because the
scaling was correct, and kept missing the actual cause.

Measured properly: at a common 180px disc, head heights are Connor 111px, Tyler 107px.
Tyler's head is 3 percent smaller, not larger. The discs are identical to the pixel and
level to within half a pixel. Nothing about the sizing was wrong.

**The paired portraits overlapped by 22 percent, and the second one was painted on top.**
So Tyler's circle was complete and Connor's was clipped by it. A whole circle beside a
cut-off one reads as the wrong size no matter what the numbers say. Removed the overlap,
put a small gap between them, dropped the disc slightly to 168px so the pair still fits
the column. Now both circles are whole and obviously equal.

Lesson: when someone says two things look wrong together and the measurements of each
one separately come out right, the fault is in the relationship between them, not in
either one. Measure the composition, not just the parts. The audit now asserts that
paired portraits never overlap.

Head heights at a common disc, for reference, since the six do vary: Rami 99, Tyler 107,
Noah 108, Connor 111, Caleb 111, Diego 123. Diego is the outlier, framed closest.

## 2026-09-15: two measurement bugs fixed

**The couples columns overlapped at the bottom.** I declared five subgrid rows but each
column has six children, so the sixth was auto-placed on top of the fifth: "What is in
the way" and the closing line were sitting in the same row. Six rows, span six. When
using subgrid, count the children.

**The portraits were mis-measured, and the fix is geometry, not tuning.** `disc_top` was
"the first row whose opaque width reaches 55 percent of the widest run", which is a point
part-way DOWN the circle, not its top, and how far down it lands depends on how much hair
overhangs. The error ranged from 7.1 to 11.1 percent of image height across the six, so
aligning on it left up to 8px of drift. Tyler was the worst because his file is square
and framed tightest.

The disc is a circle, so one measurement fits it exactly: the widest run of opaque pixels
is the diameter, and the row it falls on is the vertical center. Top is centre minus
radius. Measuring the top directly never works here because the topmost opaque pixel is
hair, not circle.

Verified by drawing the fitted circle back onto each portrait and looking at it, which is
what should have happened the first time instead of trusting a threshold. All six discs
now render at exactly 180px on Home and 200px on the narrators page, level to within half
a pixel, and the audit asserts all of it so it cannot drift again.

**Still an open art question, not a code one.** Tyler's illustration is framed closer than
the other five: his head fills noticeably more of his circle. Equal circles and equal
heads cannot both be true with these files.

## 2026-09-15: couples page added, blurbs replaced, portraits aligned

**The blurbs are Andrew's now, not mine.** I had written the six narrator intros from
scratch, which Section 3 of the brief explicitly says not to do: his synopsis blurbs
are the source copy. They are in `content/characters.yaml` essentially verbatim, with
only "Washington D.C." punctuated and one comma splice fixed. The invented "detail"
paragraphs are gone entirely.

**Portraits align to the name, not to the rule.** The head-crossing-the-rule idea
required lifting the portrait above the row, which put every face well above the text
it belonged to. Each disc's top now sits exactly level with the top of the name beside
it, measured, so the framing differences between the six files do not show. Verified:
disc top and name top match to the pixel for all six.

**New couples page.** Three columns side by side, one per couple, each with its full
kiss illustration. Aligned row by row with CSS subgrid so the names, obstacles, and
closing lines sit level across all three however long the text runs, with the plain
grid as the fallback where subgrid is missing.

Bug worth remembering: I first served the couple images with `srcset` alone listing
AVIF files. `srcset` picks by width, not by format, so a browser without AVIF support
would have got an AVIF anyway. Only `<picture>` with `<source type>` negotiates
format. Fixed, and the audit now asserts the six typed sources exist.

The three couple images are approved in `content/images.yaml` because Andrew asked for
this page. The Tier 2 and wedding band questions from Section 6 are still open: flip
an entry to `approved: false` and rebuild to pull it.

## 2026-09-15: narrators page, fourth version

Andrew: bigger portraits, and the small suns gone. Both done, and the mini rotation
is out of `build.py` and the CSS too rather than left sitting unused.

Portraits are now 200px on desktop, up from 160px, and 160px on mobile. **200px is a
hard ceiling, not a preference.** Five of the six source files are about 410px wide,
so a 200px disc is exactly 2x on a retina screen. Anything larger renders soft, and
the sources cannot be upscaled. Going bigger needs regenerated art, which is already
open decision 8 in CLAUDE.md. Tyler's file is 1254px and could go much larger, but
the six have to match.

The chapter count survives the suns as a plain line under the role, with a hairline
under it: "5 of 36 chapters, first at 1". It was a true fact about the book before it
was a graphic, and it costs nothing to keep.

## 2026-09-15: narrators page, third version

**The band version was wrong and the brief already said why.** Section 5 says couple
colors are secondary accents, used sparingly, and must never compete with orange and
navy. Six full-width tinted bands made them the entire page: no navy, no orange,
pastel wallpaper. The two-column split also left a wide void down the middle of every
band, because the text is capped at the reading measure while its column was not.

Rebuilt so the primaries carry the page. Navy header and footer, salt body, orange in
the headings and in a small sun beside each narrator. Each man's color now appears in
exactly two places: his chapters lit in that small sun, and the marker on his reveal.

**The small sun is the fix for both problems at once.** It is the hero's rotation at
`4.75rem` with an orange core, all thirty-six chapters present, his own lit in his
color. It puts orange on the page, it uses his color the sparing way the brief asks
for, it ties the page back to the home page, and it says something true that a number
alone does not: where in the year he speaks. Diego's eight are clustered differently
from Caleb's six.

Dim segments started at `#C8D0D6` and the lit ones vanished into them. `#DFE5E9`
separates them cleanly.

Dropped the left-right alternation. One consistent rhythm reads as composed; the
zigzag read as restless. Also scoped `--page` to `52rem` on this page so the heading,
the narrators, the content notes, and the sign-up share one left edge, with the
gutter outside the column so the content boxes actually line up rather than nearly
lining up.

## 2026-09-15: narrators page v2 and portraits normalized

**Andrew rejected the first narrators page.** It was six tall alternating rows on
near-white with hairline rules, and it read as a different site from Home. He chose
to carry Home's band language over, so each narrator now gets a full-width band
tinted in his own color, with the head crossing the band's top edge instead of a
hairline. The page reads as three color pairs: blue, pink, mint.

That meant reordering the six by couple rather than by first-speaking order, since
the whole point of the color pairs is that the two men in each one sit together.
The rotation information is not lost: each band still says how many chapters that
narrator gets and which one he opens at. One loop in `narrators.html` if it should
go back.

First attempt at the bands left a wide dead zone in the middle, because the text is
capped at the reading measure but the column was `1fr`. Anchoring portrait and text
to opposite edges with `justify-content: space-between` turns that leftover width
into a deliberate gutter.

**Portraits are now sized by their disc, not their file.** Andrew said the Home
images should be equal sized. They were all set to the same CSS width, but the
painted disc fills 98 to 100 percent of five files and only 93 percent of Tyler's,
which is also square while the others are taller than wide. So a shared width
rendered them at visibly different sizes. `build.py` now measures each disc and the
CSS divides by that ratio, so every disc lands at exactly the same diameter.
Generalizable lesson: normalize on the subject, not on the file.

## 2026-09-15: first build (Home and The narrators)

**Direction chosen.** Three were considered: the book's rotation as the organizing
object, the friend group as a social web, and the year as a seasonal timeline. The
rotation won because its signature element is built from real chapter data, and
because the timeline's spine would have been the Tier 2 ending and the unwritten
Act III. Approved by Andrew.

**The ring went through three versions.** First attempt was an annulus of 36
couple-tinted segments with a faint orange radial glow behind it. It read as a donut
chart, and there was no pastel orange anywhere in it. Second attempt lengthened the
rays and added a hairline orange limb: better, still a chart, and the low-opacity
orange over navy came out gray rather than warm. Third attempt made the center a
solid pastel orange disc with the title in navy on it. That is the version that
reads as a sun. Lesson: a low-opacity warm over navy goes gray. Use the color solid.

**The portraits turned out to already have transparency.** CLAUDE.md Section 6 says
all nine files are a circle on solid white. Eight of nine are actually clean RGBA.
Only `Tyler Portrait.png` needed the flood fill. `images.py` now detects this and
leaves alpha alone when it is already there, since removing a background that is not
there can only damage the artwork.

**"The heads break the line" is the layout idea worth keeping.** The illustrations
are painted with the hair crossing the top of the disc, so every narrator row has a
hairline rule that the head crosses. `build.py` measures where each disc starts and
writes it out as `--disc-top`, so all six sit on the rule identically instead of
being nudged by eye.

**Two bugs worth remembering.** Alternating a two-column grid with `order` does not
work: `order` changes paint order but not which column an item lands in, so the
narrow column got the text. Setting `grid-column` alone was not enough either,
because with DOM order and column order disagreeing, auto-placement pushed the
second item to row two. Both items need an explicit `grid-row: 1`.

**Contrast.** `#B9622C` was proposed for orange text on light and measured 4.10:1,
under AA. Now `#A85724`. More interesting: Tyler `#4A87C4` and Noah `#C06284` sit in
a band where neither navy nor white text reaches AA, so no text goes on a couple
color anywhere. The chapter count became navy on a pale tint with the full color as
the circle's edge.

**Cut during the build.** A "six voices" portrait strip on Home, because the three
couple bands already show all six faces. One accessory removed.
