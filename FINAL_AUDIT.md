# Learn Language Academy by Parth — Independent Audit Register

**Audit date:** 27 November 2026  
**Repository:** `parthfound25/learn-language-academy`  
**Audited branch:** `main` plus the audit-fix branch  
**Purpose:** A candid audit register. This is not a declaration that the application has passed professional release review.

## Executive finding

The application has a substantial 107-chapter Canadian French path and a separate 107-chapter Angolan Portuguese path. The Streamlit application, lesson renderer, language selector, unlock sequence, practice flow and assessment UI are present. Automated tests check lesson counts, required fields, option uniqueness, answer indexes, assessment/exercise separation and selected linguistic regressions.

However, **structural completeness is not the same as linguistic or educational validation**. The Portuguese A2–C2 generator was found to insert English scenario text into Portuguese example sentences and to give A2 learners advanced discourse dialogues and expressions. The audit branch corrects those two defects and adds regression tests. A2–C2 grammar explanations are still substantially reused by CEFR level rather than being authored for each chapter. The French banks also require a full editorial pass, especially for topic-specific grammar and natural dialogues.

The app is **not yet ready to be described as professionally polished or fully verified**.

## Provisional scorecard

Scores below are diagnostic estimates based on source inspection and existing automated coverage. They are not external accreditation or a claim that every sentence has been professionally proofread.

| Area | Provisional score | Reason |
|---|---:|---|
| Overall quality | 55/100 | Strong breadth and usable structure, but major content and persistence gaps remain |
| Educational quality | 54/100 | Self-study sections and practice exist; several lessons still rely on repeated scaffolds |
| Language accuracy | 50/100 | Known generated example defects corrected on audit branch; full expert review remains outstanding |
| Curriculum completeness | 76/100 | A1–C2 pathways and skills topics exist; listening/speaking assessment and topic-specific depth are limited |
| Exercises and assessment | 61/100 | Automated integrity checks exist; semantic correctness and CEFR suitability need human review |
| User experience | 66/100 | Navigation, progress display, unlocks and feedback exist; accessibility/mobile testing is incomplete |
| Technical reliability | 59/100 | CI compiles and tests curriculum structure; persistence and live end-to-end coverage are absent |

## Chapter-by-chapter inspection register

The current automated suite loads and structurally checks all 107 Angolan Portuguese lesson IDs and the 90 legacy French lesson records plus 17 extensions. The table below records the actual inspection boundary; it does **not** imply that every individual grammar explanation, translation and answer key has received native-speaker sign-off.

| Course | CEFR level | Chapters / stable IDs | Count | Structural inspection | Linguistic/editorial inspection |
|---|---|---|---:|---|---|
| Angolan Portuguese | A1 | 1–15, 91–92 | 17 | Automated content contract and question integrity covered | Individually authored editorial pass; specialist/native-speaker sign-off still required |
| Angolan Portuguese | A2 | 16–30, 93–94, 103–104 | 19 | Automated content contract and question integrity covered | Generated chapter scaffolds inspected; chapter-specific grammar depth remains incomplete |
| Angolan Portuguese | B1 | 31–45, 95–96, 105 | 18 | Automated content contract and question integrity covered | Generated chapter scaffolds inspected; chapter-specific grammar depth remains incomplete |
| Angolan Portuguese | B2 | 46–60, 97–98, 106 | 18 | Automated content contract and question integrity covered | Generated chapter scaffolds inspected; chapter-specific grammar depth remains incomplete |
| Angolan Portuguese | C1 | 61–75, 99–100, 107 | 18 | Automated content contract and question integrity covered | Generated chapter scaffolds inspected; chapter-specific grammar depth remains incomplete |
| Angolan Portuguese | C2 | 76–90, 101–102 | 17 | Automated content contract and question integrity covered | Generated chapter scaffolds inspected; chapter-specific grammar depth remains incomplete |
| Canadian French | A1 | 1–15, 91–92 | 17 | Automated content contract and selected linguistic regressions covered | Selected IPA and spelling fixes recorded; full lesson-by-lesson review remains |
| Canadian French | A2 | 16–30, 93–94, 103–104 | 19 | Automated content contract and question integrity covered | Full lesson-by-lesson editorial review remains |
| Canadian French | B1 | 31–45, 95–96, 105 | 18 | Automated content contract and question integrity covered | Examples/dialogues have uniqueness checks; grammar and naturalness review remains |
| Canadian French | B2 | 46–60, 97–98, 106 | 18 | Automated content contract and question integrity covered | Examples/dialogues have uniqueness checks; grammar and naturalness review remains |
| Canadian French | C1 | 61–75, 99–100, 107 | 18 | Automated content contract and question integrity covered | Examples/dialogues have uniqueness checks; grammar and naturalness review remains |
| Canadian French | C2 | 76–90, 101–102 | 17 | Automated content contract and CEFR wording regression covered | Advanced register, cultural references and assessment require specialist review |

**Status meaning:** “Structural inspection” verifies presence, counts, shape, and certain deterministic invariants. It does not prove that each translation is idiomatic, each grammar explanation is complete, or every question has exactly one semantically correct answer.

## Critical findings and fixes on the audit branch

### AP-A2C2-001 — English scenario text leaked into Portuguese examples
- **Affected component:** `angolan_portuguese_a2_c2_editorial.py`, all generated A2–C2 chapters.
- **Problem:** English scenario labels such as “at the market in Luanda” were interpolated into Portuguese vocabulary examples and a Portuguese example sentence.
- **Learner impact:** Presented code-switched, ungrammatical teaching examples as target-language models.
- **Correction:** Added Portuguese scenario labels for every CEFR level and rewrote the example pattern so the Portuguese sentence and English translation are kept separate.
- **Verification:** New regression test checks every A2–C2 lesson for English scenario leakage and the expected Portuguese example pattern.

### AP-A2C2-002 — A2 learners were shown advanced discourse language
- **Affected component:** `angolan_portuguese_a2_c2_editorial.py`, A2 expressions and conversations.
- **Problem:** The A2 chapter bank reused advanced discussion expressions and C1/C2-style dialogue content.
- **Learner impact:** Vocabulary and pragmatic complexity exceeded the intended elementary level.
- **Correction:** Added A2-appropriate everyday requests, directions, price questions and simple help-seeking dialogues. B1, B2, C1 and C2 now use differentiated expression/dialogue sets.
- **Verification:** New regression test asserts A2-specific expressions/dialogue cues and rejects the previous advanced-dialogue phrase.

### AP-A2C2-003 — Topic-specific grammar depth is still insufficient
- **Affected component:** `angolan_portuguese_a2_c2_editorial.py`.
- **Problem:** Most A2–C2 chapters receive the same five grammar explanations for their CEFR band, plus a generic application paragraph. This means a chapter about banking, relative clauses, literary analysis or technology may not teach the grammar implied by its title in enough detail.
- **Learner impact:** Learners can complete a chapter without receiving a sufficiently focused explanation of its stated topic.
- **Correction:** Not fully resolved in this change. The issue is explicitly retained as a high-priority editorial task rather than masking it with more generic text.
- **Required next step:** Replace shared level-only grammar blocks with individually authored, language-verified chapter grammar and examples.

### AP-APP-001 — Progress is not durably persisted
- **Affected component:** `app.py`.
- **Problem:** XP, completed lessons, practice statistics and achievements are held in Streamlit session state and copied into session-scoped keys. The Supabase schema exists, but the current app does not load/save learner progress to it.
- **Learner impact:** Progress may be lost when the Streamlit session ends, the browser reconnects, or the app restarts. The current UI must not promise cross-session or cross-device persistence.
- **Correction:** Not implemented in this audit branch because the existing login is a manually configured Streamlit Secrets username/password map, whereas the current Supabase progress schema is keyed to Supabase Auth `auth.uid()`. Connecting these safely requires a deliberate identity/persistence design, not an unsafe shortcut.
- **Required next step:** Implement and test durable per-learner progress storage that matches the private, manually managed account model.

### AP-EDU-001 — Listening and speaking are not directly assessed
- **Affected component:** lesson renderer and lesson content.
- **Problem:** Learners receive text instructions and may record themselves independently, but there is no bundled native audio playback, speech recognition, pronunciation scoring or listening comprehension audio workflow.
- **Learner impact:** Reading/writing and multiple-choice practice are better supported than listening/speaking performance.
- **Correction:** Limitation documented; no fake audio or speech-scoring feature has been claimed.
- **Required next step:** Add properly licensed/native-speaker recordings and accessible listening tasks; consider optional speech feedback only after accuracy and privacy are validated.

### AP-FR-001 — Canadian French needs the same editorial depth
- **Affected component:** `a1_lessons.py`, `a2_lessons.py`, `b1_lessons.py`, `b2_lessons.py`, `c1_lessons.py`, `c2_lessons.py`, `curriculum_extensions.py`.
- **Problem:** Existing automated tests validate structure and selected regressions, not a complete professional review of all grammar explanations, translations, regional usage, dialogues and answer keys. Earlier audits also identified generic/repeated material in some intermediate and advanced areas.
- **Correction:** Previously merged fixes include selected A1 IPA corrections, assessment-bank integrity improvements and C2 wording that no longer equates proficiency with native accent imitation.
- **Required next step:** Conduct a lesson-by-lesson Canadian French editorial pass, explicitly distinguishing standard Canadian French, Quebec colloquial usage and regional variation.

### AP-A2C2-004 — Assessment banks repeat across chapters within each CEFR band
- **Affected component:** `angolan_portuguese_a2_c2_editorial.py`, A2–C2 exercise and assessment generation.
- **Problem:** Each CEFR band currently reuses one six-question bank across its chapters. Prefixing the chapter title makes the prompt strings technically distinct, but the underlying questions do not test each chapter's stated topic.
- **Learner impact:** A learner studying relative clauses, shopping, professional writing or idioms may receive the same generic grammar/strategy questions as other chapters in that level. This weakens construct validity and can give a false impression of mastery.
- **Correction:** Not fully resolved in this audit branch. The regression work fixes language contamination and A2 level mismatch, but does not pretend the shared bank is chapter-specific.
- **Required next step:** Write a distinct, objective-mapped practice and assessment bank for every chapter; verify distractors, answer keys and explanations against the lesson content.

## Learning experience and technical findings

| Feature | Source inspection result | Release implication |
|---|---|---|
| Login | Username/password map configured in Streamlit Secrets; no public registration | Fits the private-use requirement; secrets must remain private |
| Language selector | Canadian French and Angolan Portuguese available; IELTS, Gujarati, Hindi and English marked coming soon | Matches the intended language list |
| Course sequence | 107 lessons per available language; original IDs preserved and extension IDs inserted in visible order | Structural checks cover the registry; live navigation still needs browser testing |
| Lesson navigation | Sequential unlocks; completed lessons remain reviewable | Implemented in code; live UI flow not end-to-end tested here |
| Practice | Ten-question rounds selected from unlocked lesson banks | Needs usability and scoring tests in a live session |
| Lesson assessment | Required responses, score display, explanations and retake | Present in code; semantic correctness of every question remains human-review work |
| Progress | Session-scoped only | Not reliable long-term persistence |
| Streaks | No dependable daily streak tracking identified | Do not advertise a streak feature |
| Hearts/lives | Not implemented | Correctly omitted |
| Listening/speaking | Text guidance and self-directed tasks; no native audio or automatic scoring | Major skills gap for a language-learning product |
| Accessibility/mobile | Streamlit responsive layout is used, but no recorded screen-reader, keyboard-only or device matrix test | Requires manual QA on desktop and mobile |
| Supabase | Schema and RLS policies exist; app source does not currently integrate progress persistence | Database presence must not be mistaken for a working integration |
| CI | GitHub Actions compiles curriculum modules and runs Python unit tests | Useful structural validation, not a production build or browser E2E test |

## Release blockers / priority order

1. **P0 — Complete topic-specific language authoring:** Remove shared level-only grammar blocks as the primary teaching content; author and verify each chapter's target forms, examples and dialogues.
2. **P0 — Expert linguistic review:** Native or professionally qualified Angolan Portuguese and Canadian French reviewers must verify idiom, grammar, regional labels, translations, register and assessment answer keys.
3. **P1 — Durable progress:** Design and test persistence compatible with manually managed private learner accounts.
4. **P1 — Listening and speaking:** Add real audio and learner-facing comprehension/production tasks; do not imply text prompts assess spoken ability.
5. **P1 — End-to-end application QA:** Test sign-in, language selection, lesson unlock, completion, assessment, practice, language switching, logout/login and reset in a deployed Streamlit session.
6. **P2 — Accessibility and mobile:** Test keyboard navigation, labels, contrast, zoom, screen readers and common phone/tablet widths.
7. **P2 — Curriculum alignment:** Map each lesson's outcomes and assessments to CEFR descriptors; the CEFR label alone is not evidence of level alignment.

## Final verdict (current evidence)

**Needs significant improvements.**

The application is a substantial working prototype with meaningful curriculum breadth and automated structural checks. It is not yet justified to label it “ready for learners” at a professional standard because topic-specific grammar depth, expert linguistic verification, durable progress, audio-based skills and live end-to-end QA remain incomplete.

A passing GitHub Actions run should be reported as “automated curriculum tests passed”, never as proof that every lesson is linguistically correct or that the entire deployed UI works on all devices.
