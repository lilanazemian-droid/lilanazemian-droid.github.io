# Lila Nazemian — Website Design Ethos & Purpose

## Who this site is for
Lila Nazemian is an independent curator, educator, and writer based in New York.
The site serves as her professional presence — a living, breathing extension of her
curatorial sensibility, not a generic portfolio template.

## Core purpose
- Present Lila's bio and curatorial catalogue to artists, institutions, and collaborators
- Communicate her aesthetic world before a visitor reads a single word
- The experience of visiting the site *is itself* a curatorial gesture

## Design ethos — non-negotiable principles

### Sensory atmosphere first
The site should feel like entering a space, not loading a page.
- The flower video plays as a fixed background across the entire page at all times
- Cosmos flowers fall slowly like snow — always visible, never intrusive
- A music box melody in dastgah-e Isfahan plays on visit, with gentle wind underneath
- Scroll triggers small nature-inspired note splurges (bird calls, water drops)
- All sound fades in slowly; nothing startles

### Palette — drawn from the site assets
Sourced from `flowers lilac.png` and the CSS variables in `assets/style.css`:
- `--lilac: #d8b0d5` — the primary accent; used for the logo, links, highlights
- `--sage: #a0c05f` — secondary green accent
- `--moss: #617222` — dark anchor
- `--olive: #808c20` — warm secondary
- `--cream: #f5f2ed` — text on dark/green backgrounds
- `--dark: #2e2b24` — body text on light backgrounds
- Green box: `rgba(90, 110, 70, 0.82)` — used consistently for bio and nav logo

### Typography
- Serif (Tasman / Cormorant Garamond) for display and navigation
- DM Sans (light weight) for body
- Never bold, never heavy — everything is delicate

### Layout logic
- Bio text lives in the left half of the homepage (`margin-right: 50%`)
- Bio is visible immediately on load — no scrolling required to find content
- Navigation is a floating, spinning cosmos flower button (top-right, fixed)
- The drawer nav appears on click and is compact — sized to fit its links only
- No bottom navigation on any page
- No page titles on Bio, Curatorial Catalogue, or Lila & Salar pages

### Interactivity
- The cosmos flower menu button floats and spins on a 3D tilted Y axis with a gentle bob
- Cosmos flowers fall perpetually in the background (z-index 10, pointer-events none)
- Music plays on every page visit; sound starts on first user gesture if autoplay is blocked
- Scroll triggers musical note bursts — Isfahan scale, upper octave
- No hover states that feel aggressive or corporate

### What to avoid
- Do not add gradients that create visible separators between sections
- Do not add heavy backgrounds that obscure the video
- Do not add page titles (h1 headings) to Bio, Catalogue, or Lila & Salar pages
- Do not increase opacity of the green box beyond 0.85 — the video must remain visible
- Do not add bottom navigation links
- Do not make the sound aggressive, dissonant, or Western-scale — stay in Isfahan dastgah
- Do not break the fixed video background — the `<video class="bg-video">` element
  must live directly in `<main>`, not inside any hidden container
- Do not add animations that are fast or jarring — everything moves slowly

## File structure notes
- `index.html` — homepage (bio + video + music + cosmos snow)
- `catalogue.html` — Curatorial Catalogue page
- `music.html` — Lila & Salar page (on server, not yet edited locally)
- `assets/style.css` — shared styles; edit here for global changes
- `assets/flowers_bg.mp4/.webm` — the homepage background video
- `paisley_btn.png` — legacy; replaced by inline SVG cosmos flower button

## Git workflow
- Repo: git@github.com:lilanazemian-droid/lilanazemian-droid.github.io.git
- Branch: main (auto-deploys to lilanazemian.com via GitHub Pages)
- Commit after every meaningful change; push to see changes live (1–2 min deploy)
