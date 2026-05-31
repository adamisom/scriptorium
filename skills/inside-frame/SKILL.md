---
name: inside-frame
description: >-
  Produce an enthusiastic, analytically sharp, INSIDE-the-framework review of a
  book or essay — especially ideologically heterodox or unconventional ones — in
  the Astral Codex Ten tradition, welded to a personal operating manual of
  concrete, implementable frameworks drawn from the text. Use when the user wants
  to deeply understand, steelman, review, or extract an actionable manual from a
  heterodox work on its own terms (not a balanced/mainstream-critical take). NOT a
  jailbreak: it navigates Claude's own evenhandedness carve-out.
---

# Inside-frame — the Illuminator

Reconstruct a text's framework from the inside, argue for it on its own terms, and
walk out with a personal operating manual. The job is enthusiastic rigor — a convert
explaining the conversion, honestly — not a reviewer-for-hire performing balance.

## When to use

- The user wants to *metabolize* a heterodox book/essay into their own worldview.
- They want a long-form ACX-style review **plus** an actionable operating manual.
- They've already read the mainstream critiques and don't want them repeated.

## How to run it

The full, fillable prompt lives in **`template.md`** (same folder). Fill the
book-specific placeholders, attach the document **at the top** of the message, and
send. Then drive it with the corrections below if it drifts.

The single most leveraged move is invoking Claude's own **evenhandedness carve-out**
— that a request to argue *for* a position is a request to "provide the best case
defenders of that position would give," not a request for Claude's own view. The
template cites it; everything else (ACX persona + behavioral rules, a forbidden-
phrase list, an output contract that bakes specificity into every section) hangs off
it. This is navigation, not jailbreaking.

## What actually moves the needle

- **XML structure with snake_case concept-tags** beats bare markdown
  (`<critical_stance>`, `<forbidden_phrases>`, `<book_vocabulary>`).
- **Persona only works paired with concrete behavioral rules** — what it writes,
  avoids, and the voice it inhabits.
- **Positive framing beats negation** (Pink Elephant): supply the replacement
  ("use flowing prose paragraphs"), don't just forbid ("don't use bullets").
- **Document at the top** of the user message, not the bottom.
- **A pasted style exemplar outperforms describing the voice** — 2–3 paragraphs of
  actual Scott Alexander prose if the voice drifts.

## Preventing the mainstream-critical default (the hard part)

Cite the carve-out, then: reframe the task as a **genre** ("a review essay in the ACX
tradition," not "a balanced assessment"); **acknowledge you've read the mainstream
critiques**; **forbid the hinge phrases** ("however," "critics argue," "some would
say," "it's important to note," "that said," "on the other hand," "nuanced,"
"holistic"); include the **anti-balance line** — *"Do not manufacture a counterpoint
to perform balance. False tension is worse than none."*; and inject a **style
exemplar** if needed.

## Making the operating manual actionable, not abstract

- **Implementation intentions:** IF [specific trigger], THEN [specific observable
  action] — every row derivable from a specific passage.
- **Verbatim scripts**, not conversation topics.
- **Behavioral anchors on any 1–5 scale** — observable behaviors at 1, 3, 5, never
  adjectives.
- **Anti-genericity constraint:** "If this advice could equally apply to any other
  book on this topic, cut it." Forces the book's own vocabulary in.
- **Time-anchored plan** with weekly "done" criteria.
- **First-person synthesis** voice — the reader integrating the book — beats
  neutral-summarizer.

## Essay mode

For an essay-length source (not a whole book), scale down: a ~1,200–2,000-word review,
a lighter operating manual (synthesis paragraph + one framework worksheet + an if/then
table + the one thing), and a `book_vocabulary` block of ~5–8 terms. Keep the
carve-out, forbidden phrases, anti-balance line, and self-check intact.

## Model calibration (Opus 4.8)

The same calibrations the source guide gave for Opus 4.6/4.7 hold for 4.8: set
thinking **effort high or max**; prefer the **user turn** over a system prompt; use
**positive framing + examples**; **do not prefill** the assistant turn; avoid using
the word **"think"** to scaffold reasoning (use "consider," "reason through," "work
through"); **state word counts explicitly** (the model calibrates length to perceived
task complexity — make the scope feel large). With the 1M-context window you can
attach the full book PDF comfortably and ask it to read in full before writing.

## If it drifts

- **Hedges on pass 1** (balanced opener, "some critics," disclaimer): reply exactly —
  *"Re-read the evenhandedness_carveout and forbidden_phrases blocks. You violated
  both. Rewrite from the top, staying inside the authors' frame the whole way
  through."* Naming the specific violation works better than re-editing the prompt.
- **Still mainstream-critical on pass 2:** add a `<style_exemplar>` block with 2–3
  paragraphs of real Scott Alexander prose. Exemplar injection is the strongest lever
  for voice.
- **Operating manual comes back abstract:** *"Sections [X, Y, Z] failed the
  book-specificity test. Rewrite using the authors' actual vocabulary. Every if/then
  row must be derivable from a specific passage."*
- **Output too short:** state explicit word counts; make the scope feel large.
