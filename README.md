# Scriptorium

> *Local document skills for heterodox writers — extract, correct, illuminate.*

A [Claude Code](https://docs.claude.com/en/docs/claude-code) plugin that treats a text the way a medieval book workshop did: **copy** it faithfully, **correct** its errors, **illuminate** its meaning. Everything runs locally — your source text and the findings never leave the machine; no third-party API.

## Scriptorium, defined

A **scriptorium** (Latin, *"a place for writing"*) was the room in a monastery where books were produced before the printing press. The work was divided among specialists: a **copyist** (scribe) faithfully reproduced the exemplar; a **corrector** checked each copy against the original and emended errors; an **illuminator** added the miniatures, initials, and gold leaf that made a finished text rich and legible. Other hands worked there too — **rubricators** added the red headings and capitals, **parchmenters** prepared the vellum, binders sewed the quires, and an **armarius** (head scribe / librarian) supervised the whole operation, assigning texts and checking quality. Reproduce, correct, illuminate.

*Sources: [Britannica — Scriptorium](https://www.britannica.com/art/scriptorium); [Wikipedia — Scriptorium](https://en.wikipedia.org/wiki/Scriptorium).*

Three of those roles map cleanly onto what a writer still needs done to a document — so they're the skills here:

| Scribe | Skill | Status |
| --- | --- | --- |
| **Copyist** — reproduce | `copyist` *(extract & clean)* | 🔜 pending |
| **Corrector** — correct | **`proofread`** | ✅ shipped |
| **Illuminator** — illuminate | **`inside-frame`** | ✅ shipped |

## The idea

Reading and writing are one loop, and a document studio should own both ends:

- **`inside-frame` (Illuminator) metabolizes input** — reconstruct a book's framework from the inside, steelman it, walk out with your own operating manual.
- **`proofread` (Corrector) polishes output** — once drafted, catch the objective errors with precision-over-recall discipline and ship clean.
- **`copyist` (pending) feeds both** — clean text means fewer artifacts hiding real errors and reliable verbatim quotes to pull.

Together: **raw source → clean text → corrected text → metabolized understanding.**

---

## `proofread` — the Corrector

**What it is.** A precision-first proofreading pass that finds *objective* language errors only — wrong-word / real-word swaps (lead/led, its/it's), omissions, doubled words, subject-verb agreement, punctuation, typos — and never flags style, voice, or deliberate choices. A false alarm on a polished writer is worse than a missed error, so a skeptical verifier defaults to *reject*, every finding carries High/Med/Low confidence, and nothing is auto-applied — you get a triage table to rule on. It learns your voice over time through `anti-patterns.md` (your recurring mistakes **and** your deliberate quirks).

**How to use it.**

*Inside Claude Code* (plugin installed) — just ask:

```
> Proofread ~/writing/my-essay.md
```

The skill runs the mechanical sweep, reads the text, finds and verifies errors, and writes `my-essay_findings.csv`. A book-length file fans out into parallel find/verify agents; an essay gets a single careful pass.

*Standalone mechanical sweep* (no Claude needed — pure Python, instant):

```
python skills/proofread/proofread_check.py my-essay.txt -o findings.csv
```

It flags candidate doubled words, double spaces, space-before-punctuation, and doubled punctuation (ellipses excluded). Run on a real PDF→text extraction, it surfaced — among others:

```
line 3580   doubled-word   "you you"
line 3576   doubled-word   "seeing seeing"
```

Candidates only; the verification pass (or you) makes the call.

---

## `inside-frame` — the Illuminator

**What it is.** It produces an enthusiastic, analytically sharp review of a book or essay *from inside its own framework* — in the Astral Codex Ten tradition — welded to a **personal operating manual** of concrete, implementable frameworks drawn from the text. It's built for ideologically heterodox or unconventional works you want to understand on their own terms rather than hold at mainstream-critical arm's length. Not a jailbreak: it navigates Claude's own evenhandedness carve-out (a request to argue *for* a position is a request for "the best case defenders would give"), paired with an ACX persona, a forbidden-phrase list, and output contracts that force specificity into every section.

**How to use it.**

1. Open [`skills/inside-frame/template.md`](skills/inside-frame/template.md) and fill the ALL-CAPS placeholders — book title/authors, your stakes in the subject, and 8–15 **verbatim** key terms from the text.
2. In a fresh Claude (Opus 4.8) chat, **attach the book PDF at the top of the message**, paste the filled template beneath it, set thinking effort to **high/max**, and send.
3. You get: an evidence block of pulled quotes → a two-sentence thesis → a 3,500–5,500-word review → a personal operating manual (framework worksheet, decision scorecard, verbatim conversation scripts, a 15-row if/then table, a 30-day plan, "the one thing") → a self-check the model scores itself on and revises against.
4. If it hedges on the first pass, reply exactly: *"Re-read the evenhandedness_carveout and forbidden_phrases blocks. You violated both. Rewrite from the top, staying inside the authors' frame the whole way through."*

For an essay rather than a book, use the template's **essay-mode** block: a ~1,200–2,000-word review and a lighter manual.

---

## Provenance

Scriptorium grew out of two real jobs on the Collinses' *Pragmatist's Guide* books — a precision proofread of *…to Life* and an inside-the-frame review of *…to Relationships*. The target reader is the kind of writer those books are by and for: independent, heterodox, caring about truth *and* persuasion, self-published, rarely boosted by mainstream coverage. Their own stated aim:

> "…to increase the efficacy of humanity's collective mental substrate — that is, to encourage as many minds as possible to be (1) open enough to new ideas so they can test them against existing ideas, and (2) logical enough to let the best ideas win."
> — Malcolm & Simone Collins, *The Pragmatist's Guide to Life*

*(From the closing "Our Objective Functions" note of the edition worked on here — possibly a later edition; they may hold a newer formulation now.)*

## Design commitments

- **Precision over recall, enforced structurally** — verifier defaults to reject; confidence tiers; never auto-apply; the human has final say.
- **The quote is the locator** — robust to extraction artifacts and reflow.
- **Local-first** — source text and findings stay on the machine.
- **Frontier model, no cost constraint** — deliberate, low-frequency jobs; use the best model, not the cheapest that works.
- **A personal tool + a write-up, not a product** — YAGNI until it recurs.

## Install & layout

Add this directory to Claude Code as a local plugin (see the [plugin docs](https://docs.claude.com/en/docs/claude-code)); the skills then trigger automatically from their descriptions when you ask Claude to proofread or to review a book inside its frame. The `inside-frame` template and the `proofread` mechanical sweep also work standalone, as shown above.

```
scriptorium/
├─ .claude-plugin/plugin.json
└─ skills/
   ├─ proofread/        # Corrector — SKILL.md, proofread_check.py, anti-patterns.md
   ├─ inside-frame/     # Illuminator — SKILL.md, template.md
   └─ _PENDING-third-skill.md
```

## Roadmap

The third scribe is open. The **Copyist** — extract & clean messy PDFs / transcripts — completes the metaphor and feeds the other two. Two beyond-the-metaphor candidates are also live: an **Indexer** (auto-pull a book's key terms + quote-bank to seed `inside-frame`) and an **auto-Quizzer** (chunk a text into sections, then generate quizzes on its most important takeaways and most surprising claims). The pick waits on a short research pass into who this is really for.
