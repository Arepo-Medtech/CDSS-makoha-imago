# L4_style — Layer 4 census, browser-borne assets (Q-D-16) — `tools/style_census.py`

Pages: **19**. Implied token set = values on ≥ 8 of 19 pages `[ASSESSOR-PROPOSED 40 %]`: **28 colours**, **38 px/rem values**, fonts ['IBM Plex Mono', 'Source Sans 3', 'Spectral'].

| Page | bytes | hex colours | px/rem | fonts | media queries | ext. stylesheets | colours outside implied set |
|---|---|---|---|---|---|---|---|
| `02_cdss-stack-augmented/cdss_diagrams.html` | 40939 | 8 | 11 | Georgia | 0 | 0 | **8** |
| `03_makoha-butterfly-corpus/artifacts-html/abdomen-corpus.html` | 47691 | 28 | 38 | IBM Plex Mono, Source Sans 3, Spectral | 2 | 1 | **0** |
| `03_makoha-butterfly-corpus/artifacts-html/antennae-corpus.html` | 73598 | 28 | 38 | IBM Plex Mono, Source Sans 3, Spectral | 2 | 1 | **0** |
| `03_makoha-butterfly-corpus/artifacts-html/compound-eyes-corpus.html` | 75122 | 28 | 38 | IBM Plex Mono, Source Sans 3, Spectral | 2 | 1 | **0** |
| `03_makoha-butterfly-corpus/artifacts-html/degrees-of-truth.html` | 29290 | 28 | 36 | IBM Plex Mono, Source Sans 3, Spectral | 1 | 1 | **0** |
| `03_makoha-butterfly-corpus/artifacts-html/execution-sourcing-map.html` | 27577 | 28 | 36 | IBM Plex Mono, Source Sans 3, Spectral | 1 | 1 | **0** |
| `03_makoha-butterfly-corpus/artifacts-html/four-faces-corpus.html` | 74971 | 28 | 40 | IBM Plex Mono, Source Sans 3, Spectral | 3 | 1 | **0** |
| `03_makoha-butterfly-corpus/artifacts-html/head-corpus.html` | 47348 | 28 | 38 | IBM Plex Mono, Source Sans 3, Spectral | 2 | 1 | **0** |
| `03_makoha-butterfly-corpus/artifacts-html/labial-palps-corpus.html` | 36914 | 28 | 38 | IBM Plex Mono, Source Sans 3, Spectral | 2 | 1 | **0** |
| `03_makoha-butterfly-corpus/artifacts-html/left-wing-corpus.html` | 74223 | 28 | 38 | IBM Plex Mono, Source Sans 3, Spectral | 2 | 1 | **0** |
| `03_makoha-butterfly-corpus/artifacts-html/legs-corpus.html` | 35234 | 28 | 38 | IBM Plex Mono, Source Sans 3, Spectral | 2 | 1 | **0** |
| `03_makoha-butterfly-corpus/artifacts-html/makoha-in-flight.html` | 26599 | 24 | 38 | IBM Plex Mono, Source Sans 3, Spectral | 3 | 1 | **0** |
| `03_makoha-butterfly-corpus/artifacts-html/proboscis-corpus.html` | 36862 | 28 | 38 | IBM Plex Mono, Source Sans 3, Spectral | 2 | 1 | **0** |
| `03_makoha-butterfly-corpus/artifacts-html/right-wing-corpus.html` | 104573 | 28 | 38 | IBM Plex Mono, Source Sans 3, Spectral | 2 | 1 | **0** |
| `03_makoha-butterfly-corpus/artifacts-html/sleep-tools-dossier.html` | 34998 | 26 | 39 | IBM Plex Mono, Source Sans 3, Spectral | 2 | 1 | **0** |
| `03_makoha-butterfly-corpus/artifacts-html/stranieri-dossier.html` | 27003 | 26 | 36 | IBM Plex Mono, Source Sans 3, Spectral | 2 | 1 | **0** |
| `03_makoha-butterfly-corpus/artifacts-html/thorax-corpus.html` | 46148 | 28 | 38 | IBM Plex Mono, Source Sans 3, Spectral | 2 | 1 | **0** |
| `09_diagrams/cdss_diagrams_v2.html` | 7219 | 7 | 12 | Georgia | 0 | 0 | **7** |
| `09_diagrams/cdss_diagrams_v3.html` | 10917 | 7 | 12 | Georgia | 0 | 0 | **7** |

Reading:
- The **16 corpus pages** (`03_/artifacts-html/`) are already one design system: 28 shared hex colours (drift 0 on every page), the same three faces, one external stylesheet each (Google Fonts), 36–40 sizes. PRESENT-IMPECCABLE on Q-D-16 for 03_, with one structural note: the token set lives inline in each of 16 pages, not in a shared sheet, so a palette change is 16 edits (CORPUS-OWNER; successor pages only).
- The **3 diagram pages** (`02_/cdss_diagrams.html`, `09_/cdss_diagrams_v2.html`, `_v3.html`) are a second family: 7–8 colours, 0 shared with the series, 0 media queries, 0 external stylesheets, no font-family declaration. STYLE-DRIFT rows for the two 09_ pages (v3 preserved v2's palette — the successor carried the drift forward) and a note for 02_ (retained original). Remedy: proposed `09_diagrams/tokens.css` (series palette + a diagram sub-palette) and a `cdss_diagrams_v4.html` successor — never an edit.
- No shared stylesheet or token file exists in the tree (`git ls-files | grep -i '\.css$\|tokens'` → none).

