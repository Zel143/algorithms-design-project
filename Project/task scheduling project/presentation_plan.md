# Presentation Plan — Task Scheduling with Deadlines and Profits

**Due:** June 8, 2026 (≈ 48 hours from now)
**Format:** Recorded video — PowerPoint/Google Slides + screen recording of live demo
**Estimated runtime:** 8–12 minutes

---

## Timeline

| When              | Milestone                                       |
|-------------------|-------------------------------------------------|
| June 6 (today)    | Finalize slides content (use this outline)      |
| June 6–7 (night)  | Build slides in PowerPoint / Google Slides      |
| June 7 (morning)  | Dry run narration, time it                      |
| June 7 (afternoon)| Record screen + voice (OBS / Windows Game Bar)  |
| June 7 (evening)  | Edit, trim, export MP4                          |
| June 8 (morning)  | Final review + submit by deadline               |

---

## Recording Tools

### Slides
- **PowerPoint** — export as PDF backup after recording
- **Google Slides** — alternative; use "Present" mode for full screen

### Screen Recording
- **Windows Game Bar** (`Win + G`) — built-in, zero setup, records active window
- **OBS Studio** — more control (scene switching, audio levels); recommended if
  you want to show code terminal alongside slides

### Audio
- Use a headset mic for clarity. Record in a quiet room.
- Speak at ~130–150 wpm (slower than normal conversation).

---

## Slide Outline (7 Slides)

### Slide 1 — Title Slide
- Title: **Task Scheduling with Deadlines and Profits**
- Subtitle: *A Greedy Algorithm Approach*
- Authors, course name, date

**Narration cue:** "Today we'll look at how a greedy algorithm solves the task
scheduling problem — maximizing profit when each job must be done before its
deadline."

---

### Slide 2 — Problem Statement
- One task = one time unit; only one task per slot
- Each task has: ID, deadline d, profit p
- Goal: maximize total profit of scheduled tasks
- Visual: small table of 4 sample tasks (A, B, C, D from your test case)

**Narration cue:** "The input is a list of tasks. Each has a deadline and a
profit. We can only run one task per time unit, so we have to choose wisely."

---

### Slide 3 — Algorithm Overview
- Greedy choice: sort by profit descending
- Placement rule: latest available slot ≤ deadline
- If no slot → skip
- Bullet: why greedy? Exchange argument + tight deadlines

**Narration cue:** "The greedy idea is simple — always pick the most profitable
task first, and squeeze it into the latest possible slot. That keeps earlier
slots open for tasks with tighter deadlines."

---

### Slide 4 — Pseudocode (Annotated)
- Show the `SCHEDULE-TASKS` pseudocode from `report.md`
- Highlight: sort step, inner loop, slot assignment
- Annotate with `O(n log n)` and `O(n·d)` labels

**Narration cue:** "Here's the formal pseudocode. The outer loop runs once per
task. The inner backward scan finds the latest free slot in O(d) time."

---

### Slide 5 — Greedy Trace (Step-by-Step)
- Animate one row at a time:
  - C (40) → Slot 1 ✓
  - D (30) → Slot 1 taken ✗
  - A (20) → Slot 4 ✓
  - B (10) → Slot 1 taken ✗
- Final schedule: `[C, _, _, A]`

**Narration cue:** "Let's trace through the example. C has the highest profit,
so it goes first into Slot 1. D also wants Slot 1 — it's taken, skip. A gets
Slot 4. B is stuck — skipped."

**Demo cue:** Switch to terminal, run `python task_scheduling.py`, walk through
the printed greedy trace output live.

---

### Slide 6 — Edge Cases
- Single task → always scheduled
- All same deadline → only highest-profit fits
- Zero-profit tasks → scheduled last, no profit contribution
- Deadline > n → extra empty slots, no impact

**Narration cue:** "A robust algorithm handles corner cases. Let's quickly walk
through a few to show our solution handles them correctly."

---

### Slide 7 — Complexity & Conclusion
- Time: O(n log n + n·d); Space: O(n + d)
- Compare: brute-force O(2^n) — impractical
- Greedy: optimal, proven by exchange argument
- Real-world relevance: CPU scheduling, logistics, freelance job selection
- Closing: "Questions?"

**Narration cue:** "The greedy solution runs in polynomial time and is provably
optimal. Brute-force would be exponential. For this problem, greedy wins."

---

## Live Demo Script (Slide 5 / after Slide 5)

```
# Switch to VS Code / terminal on screen
# Run:
python task_scheduling.py

# Walk through output:
# 1. Show the input table
# 2. Narrate the greedy trace line by line
# 3. Confirm selected = C, A; skipped = D, B; profit = 60
# 4. Show the slot array printout
```

Estimated demo time: **1–2 minutes**

---

## Delivery Checklist

- `[ ]` Slides complete (PowerPoint / Google Slides)
- `[ ]` PDF export of slides saved
- `[ ]` Terminal / code ready to demo (`task_scheduling.py`)
- `[ ]` Audio input tested (mic levels OK)
- `[ ]` Recording started (Game Bar: Win+G → record; OBS: Start Recording)
- `[ ]` Recording exported as MP4 (≤ 1080p, ≤ 500 MB recommended)
- `[ ]` Video reviewed (no dead silence, no long pauses)
- `[ ]` Submitted before June 8, 2026

---

## Slide Design Tips (PowerPoint)

- Use a dark theme (dark navy / charcoal) — looks professional on screen recordings
- Use a monospace font (Cascadia Code, Consolas) for pseudocode slides
- Use Sans-serif (Calibri, Segoe UI, or Inter) for body text
- Limit each slide to ≤ 5 bullet points
- Animate the greedy trace table row-by-row (Appear animation, on-click)
- Add slide numbers in the footer
