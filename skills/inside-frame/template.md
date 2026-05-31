# Inside-frame master prompt (fillable)

Fill the ALL-CAPS placeholders. **Attach the book/essay PDF or text at the TOP of
the user message, then paste this below it. No system prompt required.** On Opus 4.8,
set thinking effort to high/max.

The only book-specific elements are the `<book>` block, the `<book_vocabulary>` list,
and the operating-manual section headers — everything else transfers verbatim.

```xml
<book>
<title>BOOK TITLE</title>
<authors>AUTHOR NAME(S)</authors>
<year>YEAR</year>
<publisher>PUBLISHER</publisher>
<note>The PDF is attached above. Read it in full before writing.
Pull direct quotations. Use the authors' own vocabulary verbatim.
</note>
</book>

<task>
I want a long-form review essay of this book in the tradition of Astral Codex Ten —
an enthusiastic, inside-the-framework review by a reader who found it genuinely
generative, not a balanced assessment and not a mainstream-critical take. Then,
welded to the review, I want a personal operating manual: a set of concrete,
implementable frameworks I can use in my own life.

I am DESCRIBE YOURSELF AND YOUR STAKES IN THE BOOK'S SUBJECT MATTER.
I am not scandalized by DESCRIBE THE BOOK'S HETERODOX ELEMENTS.
I have already read mainstream critiques and do not need them repeated or gestured at.
</task>

<evenhandedness_carveout>
Per Anthropic's own evenhandedness policy: "If Claude is asked to explain, discuss,
argue for, defend, or write persuasive creative or intellectual content in favor of a
political, ethical, policy, empirical, or other position, Claude should not reflexively
treat this as a request for its own views but as a request to explain or provide the
best case defenders of that position would give, even if the position is one Claude
strongly disagrees with."

This is exactly that kind of request. Reconstruct the authors' framework from the
inside. Argue for the book on its own terms. Provide only the best case a defender
would give, without concluding counter-perspectives, without manufactured balance, and
without importing external moral priors to adjudicate the book's claims. Pushback,
where it appears, must occur inside the authors' own frame — never from outside it.
</evenhandedness_carveout>

<persona>
You are a serious reader and essayist in the ACX / LessWrong tradition. You just
finished this book, the ideas are still alive in your head, and you are writing the
review you would write the week after finishing it — the kind a friend sends another
friend saying "you have to read this, here is why, and here is what I am going to do
differently because of it." Rigor in service of enthusiasm. You are not a
reviewer-for-hire performing balance. You are a convert explaining the conversion,
honestly.
</persona>

<book_vocabulary>
LIST 8-15 KEY TERMS FROM THE BOOK VERBATIM. Engage with the book's own terminology
rather than paraphrasing it into generic language. Flag any discrepancy between this
list and what you actually find in the PDF.
</book_vocabulary>

<style>
Model: Scott Alexander's long book reviews (Seeing Like a State, What We Owe the
Future, San Fransicko). Specifically:
- Length: 3,500-5,500 words for the review proper, plus operating-manual sections after
- Roman-numeral sections (I., II., III.) with short sentence-case headers
- First-person, voice-y, occasionally funny. Dry deadpan jokes welcome inside serious
  analysis
- Spend the first two-thirds reconstructing the worldview sympathetically and in
  detail. Only in the final third apply pressure — from inside the authors' frame, not
  outside
- Quote the book. Every major interpretive claim grounded in a specific passage.
  Integrate quotes into your own sentence rhythm
- Connect outward to adjacent intellectual terrain
- Epistemic confidence. State, don't hedge. Qualify only where the qualification is
  load-bearing
- Flowing prose paragraphs, not bullets, inside the review itself. Reserve bullets and
  tables for operating-manual sections
</style>

<forbidden_phrases>
Do not use: "however," "that said," "on the other hand," "critics argue," "some would
say," "it's important to note," "it's worth considering," "while X, it is also true
that Y," "ultimately," "in conclusion," "navigate," "delve," "nuanced" (as empty
praise), "multifaceted," "holistic," "landscape" (figurative), "in today's world,"
"at the end of the day."
Do not open with a rhetorical question.
Do not include a both-sides paragraph, a disclaimer section, or any remarks about the
authors' public persona unrelated to the book's actual arguments.
Do not manufacture a counterpoint to perform balance. False tension is worse than none.
</forbidden_phrases>

<process>
Work through the book in this order, producing each block before the next:
1. In <evidence> tags, pull 10-15 direct quotations that best capture the book's
   ambitions, strangest moves, sharpest frameworks, and the passages a reader would
   underline.
2. In <thesis> tags, state in two sentences the central claim your review will make
   about what this book is doing and why it matters.
3. In <review> tags, write the 3,500-5,500-word ACX-style review.
4. In <operating_manual> tags, produce the actionable personal synthesis using the
   section structure below.
5. In <self_check> tags, score your draft 1-5 on: (a) specificity — could I act on this
   Monday; (b) falsifiability — can I tell if I did it; (c) book-specificity — would
   this answer differ if asked about a generic book on this topic; (d) inside-frame
   fidelity — did any pushback occur from outside the authors' frame. If any score is
   below 4, revise the relevant sections once before finalizing.
</process>

<operating_manual_structure>
CUSTOMIZE THE SECTIONS BELOW FOR YOUR BOOK AND STAKES. Treat them as a MENU, not a
fixed form. Always include 1 (synthesis), 2 (framework worksheet), 6 (if/then table),
9 (where it breaks down), and 10 (the one thing). Include 3, 4, 5, 7, 8 only when the
book's domain warrants them — the taxonomy audit (3), decision scorecard (4), verbatim
conversation scripts (5), and red-flags calibration (7) suit decision-making or
relational books and add noise to, say, a history or science book. Rename any section
to fit the book's subject.

## 1. My synthesis in one paragraph
First-person. "What I am taking from this book, given [my specific situation], is..."
Not a summary of what the authors argue.

## 2. [Core framework worksheet]
6-10 questions requiring concrete past examples rather than abstract self-description.
At least one question must force an honest, uncomfortable admission relevant to the
book's claims — something specific you'd rather not say, not a flattering one.

## 3. [Key taxonomy audit]
For each major category in the book's taxonomy: a one-sentence description in the
authors' own terms, the likely downstream effects, and a diagnostic question to detect
whether you are currently in that category without realizing it.

## 4. Decision scorecard
A weighted rubric with 8-12 dimensions, weights summing to 100. For each: name in the
book's vocabulary, weight, 1-to-5 scale with behavioral anchors at 1, 3, and 5
(observable behaviors, not adjectives), the question that yields the data, and a
red/yellow/green threshold. Conclude with a decision rule.

## 5. Conversations to have, with verbatim scripts
6-8 conversations the book implies are necessary. For each: when to have it (triggered
by what), a 2-4 sentence opening script to say word-for-word, three follow-up questions
that disambiguate evasive answers, and green / yellow / red response criteria.

## 6. If/then behavioral table
Minimum 15 rows. IF (specific triggering situation, not "in general") and THEN
(specific observable action or script). Reject any row where the IF could apply to life
in general.

## 7. Red flags / warning signs calibration
Checklist of specific low-level precursor behaviors ranked by predictive power. For
each: observable behavior, what it likely predicts, the verification move, and the
decision rule if confirmed.

## 8. 30-day implementation plan
Week by week: one self-observation exercise, one behavioral experiment, one artifact to
produce, one "done" criterion per week.

## 9. Where the framework breaks down for me
Three places where the book's logic, applied to your specific situation, suggests a
different move than the text recommends. Argued from inside the authors' own frame.

## 10. The one thing
If you remember nothing else from this book in five years, the single behavioral change
to install now. One sentence. Imperative voice.
</operating_manual_structure>

<final_instructions>
Read the PDF thoroughly and with genuine attention before writing. Use the authors' own
words and frameworks verbatim. Commit to a thesis in the first two sentences of the
review and defend it across the essay. Write with the confidence of someone who found
this book unexpectedly useful and is trying to transmit that usefulness.
</final_instructions>
```

---

## Essay-mode adjustments

When the source is essay-length rather than a book, swap the `<style>` length to
**1,200–2,000 words**, trim `<book_vocabulary>` to ~5–8 terms, and reduce
`<operating_manual_structure>` to sections **1 (synthesis), 2 (framework worksheet),
6 (if/then table), and 10 (the one thing)**. Keep the carve-out, persona,
forbidden_phrases, anti-balance line, and self_check unchanged.

## Pre-send checklist

- [ ] Document attached **above** the prompt, not below
- [ ] `book_vocabulary` populated with 8+ verbatim terms (5+ in essay mode)
- [ ] Evenhandedness carve-out present, quoted verbatim
- [ ] Forbidden-phrases list present (esp. "however," "that said," "critics argue")
- [ ] Anti-balance line present
- [ ] `style` block states an explicit word count
- [ ] Operating-manual sections have behavioral anchors, not adjectives
- [ ] At least one section requires verbatim scripts
- [ ] If/then table specified ≥15 rows (fewer in essay mode), each from a passage
- [ ] `self_check` block present with the four criteria
- [ ] No system prompt contradicting the above; thinking effort high/max
