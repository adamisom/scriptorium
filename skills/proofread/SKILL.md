---
name: proofread
description: >-
  Precision-first proofreading that finds OBJECTIVE language errors only
  (wrong-word/real-word swaps, omissions, doubled words, subject-verb agreement,
  punctuation, typos) and never flags style or voice. Use this whenever the user
  wants writing checked for errors before publishing — "proofread," "copyedit,"
  "error-check," "do a final pass," "catch my typos," "is this clean," "look over
  my draft / manuscript" — for their own essay or post or someone else's book, even
  if they never say the word "proofread." Handles essay-length (single pass) and
  book-length (chunked, multi-agent). Defaults to precision: a false alarm on a
  polished writer is worse than a missed error. Do NOT use for developmental
  editing, restructuring, rewriting, or style/clarity feedback — it deliberately
  refuses those.
---

# Proofread — the Corrector

Find objective language errors only, with precision-over-recall discipline. The
deliverable is a triage table a human reviews before anything is changed. **Never
auto-apply edits.**

## When to use

- Final error pass on the user's own essay/post before publishing (hero case).
- Proofreading a longer manuscript or a book the user is helping with.
- Any "catch my typos / copyedit this / is this clean?" request.

**Not** for developmental editing, restructuring, or style/clarity feedback — this
skill deliberately refuses those. If the user wants that, say so and stop.

## Core principle

**Precision over recall.** Before flagging anything, ask: *"Is this objectively
wrong, or just not how I would write it?"* Keep only the former. If something might
be deliberate, leave it out or mark it **Low** confidence. The verifier defaults to
*reject* when uncertain. The author always has the final say.

## What to flag (all matter equally)

- **Wrong-word / real-word errors** — a correctly spelled word that is wrong in
  context, especially confusables (illicit/elicit, affect/effect,
  complement/compliment, lead/led, its/it's, principal/principle). Hardest to catch
  because each word is individually valid — give these extra attention. Actively
  test the most likely confusable alternative; keep the flag only if it clearly
  fits the meaning better.
- **Missing words (omissions)** — a dropped article, preposition, auxiliary, or
  verb ("to elicit ___ response"). Spell-checkers miss these — extra attention.
- **Doubled words** ("the the"), **subject-verb agreement**, **punctuation
  errors**, and plain **typos/misspellings**. These matter just as much.

## What NOT to flag (critical — assume a skilled writer)

- Style, voice, word choice, rhythm, or anything you'd merely "prefer."
- Intentional fragments, comma splices for effect, dialect, dialogue grammar,
  archaic/technical usage, em-dash and serial-comma choices.
- Proper nouns, names, invented terms, or foreign words you cannot verify — treat
  invented terms as intentional.
- **Read `anti-patterns.md` first** (same folder). Its "Deliberate style" section
  lists the user's intentional choices — do not flag those. Its "Recurring errors"
  section lists mistakes they actually make — give those extra attention.

## Quoting rule

Quote the original **verbatim** (~5–10 words, enough to locate via Ctrl-F). If you
cannot quote the exact words from the text, do not flag it. Never invent text, page
numbers, or chapter titles. **The quote is the locator** — robust to PDF artifacts
and reflow; line numbers are a best-effort convenience.

If the source is a PDF→text extraction, expect artifacts — standalone/inline page
numbers, running heads, sentences shattered across blank lines (sometimes one word
per line), TOC dumps. **Mentally reassemble** the prose and **ignore artifacts — do
not flag them.** Skip non-prose front/back matter (cover, copyright, TOC, index)
unless whole-file completeness is explicitly wanted.

## Two modes

Pick by length; when unsure, ask.

### Essay mode (hero — single pass)

For anything that fits comfortably in one pass (≈ up to a few thousand words):

1. Run the mechanical sweep: `python proofread_check.py <file>` → candidate
   doubled-words / spacing / punctuation anomalies.
2. Read the whole text slowly, in order, sentence by sentence. Produce candidate
   findings (verbatim quote, type, fix, confidence, why).
3. **Verify** each candidate against the rules above, defaulting to reject. Merge
   the mechanical-sweep candidates through the same verification.
4. Emit the output (below).

### Book mode (chunked, multi-agent)

For book-length input, use the `Workflow` tool to parallelize:

0. **Structural probe** — read the file's shape (section boundaries, paragraph
   structure, artifact density) to set chunk boundaries and artifact instructions.
1. **Mechanical sweep** — `proofread_check.py` over the whole file.
2. **Chunk** into section-aligned pieces (~6k tokens / ~250–320 lines), cut at
   paragraph boundaries, each with a ~6-line tail overlap so nothing falls in a
   boundary crack. Small chunks keep each agent's attention high.
3. **Pass 1 — parallel find:** one agent per chunk reads its own line range from
   disk and returns structured findings — pass each the **find-agent prompt** in
   `references/agent-prompts.md`.
4. **Pass 1 — verifier:** a second, *skeptical* agent per chunk re-reads the same
   lines and rules confirmed / adjusted / rejected, **defaulting to reject** (the core
   precision lever) — use the **verify-agent prompt** in `references/agent-prompts.md`.
5. **Synthesis:** dedupe overlap double-reports (by quote substring), order by line,
   tally by type/confidence, write the CSV.
6. *(Optional, for max recall)* **Pass 2 — independent second sample:** fresh
   find+verify over the same sections, nudged toward the two easiest-to-miss classes
   (omissions, real-word swaps); dedupe against pass 1. New-confirmed ≈ single-pass
   miss rate; cross-pass agreement is evidence of reliability.

## Output

1. **One-line summary** — how much text reviewed; counts by error type and by
   confidence.
2. **High-confidence shortlist** — the items you are most sure are real.
3. **Full CSV** (write to `<name>_findings.csv`), in order of appearance, columns:
   `# | line | found_in | quoted_original | error_type | suggested_fix | confidence | human_checked | why`
   - `error_type` ∈ {wrong-word, missing-word, doubled-word, subject-verb-agreement,
     punctuation, typo, other}
   - `confidence` ∈ {High, Med, Low}
   - `found_in` ∈ {pass1, pass2, both} — which pass caught it (book mode); just `pass1`
     in essay mode.
   - `human_checked` — blank until a human rules on the row, then yes/no; tracks the audit.
   - `why` = one line; cite that the quote appears verbatim and the test you applied.

## Human-audit & the voice-learning loop

The model cannot audit its own precision — **only a human verdict can.** For a real
job, hand the user a small curated packet (weighted to Med/Low judgment calls) to
rule on, each with enough surrounding text to judge without opening the file.

After the human rules, **update `anti-patterns.md`:**
- A confirmed recurring mistake → add/strengthen it under "Recurring errors (flag +
  fix)."
- A rejected flag that was actually deliberate style → add it under "Deliberate
  style (never flag)" so the next run respects it.

Over time this file becomes the user's personal style guide, and the proofreader
gets quieter and sharper on their voice specifically.

## Gauging reliability (no ground truth)

You can't score recall without an answer key, but you can read the signals:
- **Human-audit precision** — on the curated packet, the share of flags the human
  confirms real. **Below ~90% → tighten the find prompt** (push "might be deliberate →
  drop" harder) and re-scrutinize the weakest error class. Above it, trust the full set.
- **Cross-pass corroboration** (book mode) — the share of pass-1 finds that pass 2
  independently re-finds is evidence pass 1 was reliable; pass-2's *new* confirmed
  errors estimate the single-pass miss rate.

## Stronger recall (optional)

Reach for these only when the basics leave errors on the table — and most want **clean
text first** (the Copyist, when it lands):
- **LanguageTool** (local, free, rule/n-gram) as a higher-precision mechanical pass —
  but only on clean text; it drowns in extraction artifacts.
- **Correct-then-diff** for omissions (the weakest class): have the model rewrite *only*
  objective errors, then read the diff's insertions — dropped words surface as additions
  better than find-and-report.
- **Confusion-set gating** — a curated homophone/confusable list to lift confidence on
  known pairs.
