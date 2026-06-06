# Project Proposal

## Topic: 0/1 Knapsack Problem Using Dynamic Programming

---

## Brief Discussion

The **0/1 Knapsack Problem** is a classic combinatorial optimization problem.
Given a set of items, each with a weight and a profit, and a knapsack with a
fixed weight capacity, the goal is to select a subset of items that **maximizes
total profit without exceeding the capacity**. Each item can only be taken once
(hence "0/1": either include it or leave it).

A **Greedy approach** cannot guarantee an optimal solution here because locally optimal choices, such as picking the highest-profit item at each step, can block better global combinations.
Dynamic Programming (DP) solves this by building a table of optimal
sub-solutions: for each item and each capacity level, it records the best
achievable profit, then traces back the selected items.

**Algorithm Steps:**

1. Create a 2D DP table of size `(n+1) x (W+1)` where `n` = number of items
   and `W` = knapsack capacity.
2. Fill the table row by row: for each item `i` and capacity `w`, either skip
   the item or include it (if it fits), taking whichever yields higher profit.
3. Backtrack through the table to identify which items were selected.

**Why this topic?**

- Directly maps to the handout's Dynamic Programming topic area.
- Contrasts well with the Greedy sample: shows *when* greedy fails and *why*
  DP is needed.
- Real-world relevance: resource allocation, budget planning, cargo loading.
- Time complexity is tractable for demo: **O(n × W)**.

---

## Input

A list of items and a knapsack capacity:

| Item | Weight | Profit |
| ---- | ------ | ------ |
| A    | 2      | 6      |
| B    | 2      | 10     |
| C    | 3      | 12     |
| D    | 5      | 15     |

**Knapsack Capacity:** `W = 5`

---

## Expected Outcome

| Output Field      | Value          |
| ----------------- | -------------- |
| Selected Items    | B, C           |
| Total Weight Used | 5 (= 2 + 3)    |
| Total Profit      | 22 (= 10 + 12) |

The DP table will show why items B and C together yield a higher profit (22)
than any single item alone or an alternative combination such as A + C (18) or
D alone (15).

---

## Summary

| Property         | Detail                              |
| ---------------- | ----------------------------------- |
| Problem Type     | Combinatorial Optimization          |
| Algorithm Class  | Dynamic Programming                 |
| Time Complexity  | O(n × W)                           |
| Space Complexity | O(n × W) table, O(n) for traceback |
| Language         | Python                              |
| Deliverables     | Code, DP table output, report       |
