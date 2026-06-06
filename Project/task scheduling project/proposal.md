# Project Proposal

## Topic: Task Scheduling with Deadlines and Profits

---

## Brief Discussion

The **Task Scheduling with Deadlines and Profits** problem asks: given a set of
jobs, each with a deadline and a profit, how do you schedule them to maximize
total profit, where each job takes exactly one unit of time and must be
completed on or before its deadline?

This is a classic application of **Greedy Algorithm** design. A greedy approach
works here because always prioritizing the highest-profit task and placing it in
the latest available slot before its deadline never blocks a better solution.
The argument holds because:

- No task needs more than one time slot.
- Placing a high-profit task as late as possible leaves earlier slots open for
  other tasks with tighter deadlines.
- Skipping a task only happens when no valid slot remains, so no profit is lost
  unnecessarily.

**Algorithm Steps:**

1. Sort all tasks by profit in descending order.
2. Create a slot array of size equal to the maximum deadline.
3. For each task (in sorted order), find the latest available slot at or before
   its deadline and assign it there.
4. Skip the task if no valid slot is free.
5. Sum the profits of all scheduled tasks.

**Why this topic?**

- Directly maps to the Greedy Algorithms topic area in the handout.
- The problem is easy to state, easy to trace by hand, and has a clear
  correctness argument.
- Real-world relevance: CPU scheduling, freelance job selection, logistics.
- Time complexity is tractable and easy to analyze: O(n log n) for sorting plus
  O(n * d) for placement.

---

## Input

A list of tasks and their attributes:

| Task | Deadline | Profit |
|------|----------|--------|
| A    | 4        | 20     |
| B    | 1        | 10     |
| C    | 1        | 40     |
| D    | 1        | 30     |

Each task takes exactly one time unit. Deadlines are given in time units from
the start.

---

## Expected Outcome

| Output Field     | Value                         |
|------------------|-------------------------------|
| Selected Tasks   | C, A                          |
| Total Profit     | 60 (= 40 + 20)                |
| Schedule         | Slot 1 -> C, Slot 4 -> A      |
| Skipped Tasks    | B, D (no valid slot remaining)|

The greedy trace shows why:

- C (profit 40) is picked first, placed in Slot 1 (latest before deadline 1).
- A (profit 20) is picked next, placed in Slot 4 (latest before deadline 4).
- D (profit 30) and B (profit 10) both need Slot 1, which is already taken.

---

## Summary

| Property         | Detail                                  |
|------------------|-----------------------------------------|
| Problem Type     | Combinatorial Optimization / Scheduling |
| Algorithm Class  | Greedy                                  |
| Time Complexity  | O(n log n + n * d)                      |
| Space Complexity | O(d) for the slot array                 |
| Language         | Python                                  |
| Deliverables     | Code, schedule output, report           |
