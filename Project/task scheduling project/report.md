# Project Report

## Problem

We need to schedule a set of tasks so that each task is completed before its
deadline and the total profit is as large as possible. Each task takes exactly
one unit of time. Only one task can run per time slot.

## Inputs

- A list of tasks
- Each task has an id, a deadline (in time units), and a profit value

## Outputs

- The selected tasks and their assigned time slots
- A list of skipped tasks that could not be placed
- The total profit of all scheduled tasks

## Algorithm Choice: Greedy

1. Sort tasks by profit in descending order.
2. Initialize a slot array of size equal to the maximum deadline.
3. For each task (in sorted order), scan backwards from its deadline to find
   the latest free slot. Assign the task there.
4. If no valid slot exists, skip the task.

The greedy choice is correct here because:
- Placing high-profit tasks first always increases total profit.
- Placing each task in its latest valid slot leaves earlier slots open for
  tasks with tighter deadlines.
- A formal exchange argument shows that any non-greedy schedule can be
  transformed into the greedy schedule without reducing profit.

## Why This Approach

The greedy strategy is simple to explain, easy to trace step by step, and
provably optimal for this problem. It avoids the overhead of dynamic programming
or brute-force enumeration and runs efficiently even for larger inputs.

## Time Complexity

- Sorting: O(n log n)
- Slot placement: O(n * d) in the worst case, where d is the maximum deadline
- Overall: O(n log n + n * d)

For n tasks and deadline d bounded by n, this simplifies to O(n^2).

## Space Complexity

- O(d) for the slot array, where d is the maximum deadline
- O(n) for the sorted task list and selected/skipped output lists

## Alternative Approach

A brute-force approach would enumerate all 2^n subsets of tasks and check
feasibility for each. This has O(2^n) time complexity and is not practical
beyond small inputs. The greedy approach is strictly better.

## Test Case

Input:
- Task A: Deadline 4, Profit 20
- Task B: Deadline 1, Profit 10
- Task C: Deadline 1, Profit 40
- Task D: Deadline 1, Profit 30

Greedy trace:
1. C (profit 40, deadline 1) -> placed in Slot 1
2. D (profit 30, deadline 1) -> Slot 1 taken, skipped
3. A (profit 20, deadline 4) -> placed in Slot 4
4. B (profit 10, deadline 1) -> Slot 1 taken, skipped

Expected result:
- Selected Tasks : C, A
- Skipped Tasks  : D, B
- Total Profit   : 60
- Schedule: Slot 1 -> C, Slot 4 -> A
