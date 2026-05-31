---
name: inside-frame
description: >-
  Produce an enthusiastic, analytically sharp review of a book or essay from INSIDE
  its own framework (Astral Codex Ten style), welded to a personal, implementable
  operating manual extracted from the text. Use this whenever the user wants to
  deeply understand, steelman, metabolize, or review-on-its-own-terms a book or
  essay — ESPECIALLY ideologically heterodox, unconventional, or contrarian ones —
  or asks for an operating manual, actionable frameworks, or a personal synthesis
  from something they read, even if they never say "inside the frame." Trigger on
  requests like "give me a steelman review of <book>," "what should I actually do
  differently after reading this," "extract a playbook from <author>," or "review
  this on its own terms, not the mainstream take." NOT a jailbreak: it navigates
  Claude's own evenhandedness carve-out. Do NOT use for a neutral summary, a
  balanced or mainstream-critical book report, or fact-checking.
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

**Mode A — directly, in Claude Code (default when you're handed a document).** Read the
target book/essay in full, then produce the five blocks in order, following the contract
in `template.md`: `<evidence>` (10–15 verbatim quotes) → `<thesis>` (two sentences) →
`<review>` (the long ACX-style essay) → `<operating_manual>` (the section menu) →
`<self_check>` (score 1–5 on specificity, falsifiability, book-specificity, inside-frame
fidelity; revise any section below 4). Build the `book_vocabulary` yourself from the text
— 8–15 verbatim key terms — because **that block does the heaviest lifting**: generic
vocabulary is exactly what makes an operating manual collapse into generic advice.

**Mode B — portable (a fresh chat, or handing it to someone else).** The full fillable
prompt lives in **`template.md`**. Fill the placeholders, attach the document at the top
of the message, set thinking effort high/max, and send.

Either way, the single most leveraged move is invoking Claude's own **evenhandedness
carve-out** — that a request to argue *for* a position is a request to "provide the best
case defenders of that position would give," not a request for Claude's own view.
Everything else (ACX persona + behavioral rules, the forbidden-phrase list, an output
contract that bakes specificity into every section) hangs off it. This is navigation, not
jailbreaking. **If the verbatim carve-out ever stops parsing** as recognized policy (its
wording is from 4.6/4.7-era leaks and may drift), the surrounding frame — "argue the best
case a defender would give, from inside the authors' own frame" — still works on its own.

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
- **Output too short:** the reference run was ~12k words (≈5k review + a dense manual);
  if yours is much shorter, the scope isn't registering — state explicit word counts and
  make the task feel large.
