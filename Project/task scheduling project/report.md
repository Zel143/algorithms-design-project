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

---

## Pseudocode

```
SCHEDULE-TASKS(tasks)
  // Input:  tasks — array of n records, each with fields id, deadline, profit
  // Output: selected, slots, skipped, total_profit

  max_d ← max { task.deadline : task ∈ tasks }
  slots[1..max_d] ← NIL                          // O(d) initialisation
  selected ← empty list
  skipped  ← empty list

  // Greedy choice: process tasks in non-increasing profit order
  sort tasks by profit descending                 // O(n log n)

  for each task t in tasks (sorted order) do      // O(n) iterations
    placed ← FALSE
    // Scan backwards from t.deadline to find the latest free slot
    for j ← min(t.deadline, max_d) downto 1 do   // O(d) per task → O(n·d) total
      if slots[j] = NIL then
        slots[j] ← t.id
        APPEND(selected, t.id)
        placed ← TRUE
        break
      end if
    end for
    if placed = FALSE then
      APPEND(skipped, t.id)
    end if
  end for

  total_profit ← Σ { t.profit : t ∈ tasks, t.id ∈ selected }
  return selected, slots, skipped, total_profit

END SCHEDULE-TASKS
```

**Loop invariant:** After processing each task `t`, `slots` holds an optimal
partial schedule for all tasks considered so far; no future high-profit task is
blocked by the current placement because each task is placed in its *latest*
valid slot.

**Complexity summary**

| Step            | Time                | Space    |
| --------------- | ------------------- | -------- |
| Sort            | O(n log n)          | O(1)     |
| Slot placement  | O(n · d)           | O(d)     |
| Profit sum      | O(n)                | O(1)     |
| **Total** | O(n log n + n · d) | O(n + d) |

---

## Edge Cases

### 1. Single Task

**Input:** one task with any deadline ≥ 1 and any profit.

**Behaviour:** The task is always scheduled in its deadline slot (or the latest
available slot ≤ deadline). Total profit equals that task's profit.

**Trace:**

- Task X: deadline 3, profit 50 → placed in Slot 3.
- Selected: X | Skipped: (none) | Profit: 50

### 2. All Tasks Share the Same Deadline

**Input:** n tasks all with deadline = 1 (or any single common deadline d = k).

**Behaviour:** Only one task can be scheduled because there is only one slot
available at or before the shared deadline. The greedy algorithm picks the
highest-profit task; all others are skipped.

**Trace (deadline = 1 for all):**

- Tasks sorted by profit: P=100, Q=80, R=60
- P → Slot 1 (placed). Q → Slot 1 taken, skipped. R → Slot 1 taken, skipped.
- Selected: P | Skipped: Q, R | Profit: 100

### 3. Zero-Profit Tasks

**Input:** tasks where profit = 0 (or negative if the problem allows it).

**Behaviour:** Zero-profit tasks are processed last (they sort to the bottom).
They still get scheduled into any remaining free slots, but they contribute
nothing to total profit. This is correct, the greedy never removes a
scheduled task, so zero-profit tasks never displace positive-profit tasks.

**Trace:**

- Task A: deadline 2, profit 50 → Slot 2.
- Task B: deadline 1, profit 0  → Slot 1 (placed, profit contribution = 0).
- Selected: A, B | Skipped: (none) | Profit: 50

**Note:** If the requirement is to *maximise* profit strictly, zero-profit tasks
can be filtered out before running the algorithm with no change to correctness.

### 4. All Deadlines Equal 1 (Capacity = 1)

**Behaviour:** Equivalent to Case 2 with d = 1. Only one slot exists. Only the
highest-profit task is scheduled regardless of n.

### 5. Deadline Larger Than Number of Tasks

**Input:** tasks where max deadline d > n.

**Behaviour:** Extra trailing slots in the array remain NIL. This does not
affect correctness — the algorithm simply does not use those slots. All n tasks
can potentially be scheduled (one per slot) as long as deadlines are distinct
enough.

**Trace (n = 2, max deadline = 10):**

- Task A: deadline 10, profit 30 → Slot 10.
- Task B: deadline  5, profit 20 → Slot 5.
- Selected: A, B | Skipped: (none) | Profit: 50

---

## References

[1] T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein. 2009.
*Introduction to Algorithms* (3rd ed.). MIT Press, Cambridge, MA, USA.
(See Chapter 16, Section 16.5: "A Task-Scheduling Problem as a Matroid.")

[2] J. Kleinberg and É. Tardos. 2006. *Algorithm Design*. Addison-Wesley,
Boston, MA, USA. (See Chapter 4, Sections 4.1–4.3 on Greedy Algorithms.)

[3] J. M. Moore. 1968. An n Job, One Machine Sequencing Algorithm for
Minimizing the Number of Late Jobs. *Management Science* 15, 1 (1968), 102–109.
https://doi.org/10.1287/mnsc.15.1.102

[4] E. L. Lawler and J. M. Moore. 1969. A Functional Equation and its
Application to Resource Allocation and Sequencing Problems. *Management
Science* 16, 1 (1969), 77–84. https://doi.org/10.1287/mnsc.16.1.77

[5] E. L. Lawler. 1976. *Combinatorial Optimization: Networks and Matroids*.
Holt, Rinehart and Winston, New York, NY, USA.
