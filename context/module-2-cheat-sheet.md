# Module 2 Deep Dive Cheat Sheet

Sources: [Module 2](Module%202/), especially the decrease-and-conquer, divide-and-conquer, AVL, heap, regression, and greedy lecture files.

## Fast ID Guide

| Topic | Core idea | Invariant | Usual cost | Common trap |
|---|---|---|---|---|
| Decrease-and-conquer | Shrink one problem to a smaller one | Size strictly decreases | Often $T(n)=T(n-1)+f(n)$ or $T(n)=T(n/c)+f(n)$ | Reduction does not really shrink |
| Divide-and-conquer | Split, solve, combine | Subproblems cover the original problem | Often $T(n)=aT(n/b)+f(n)$ | Forgetting the combine step |
| AVL tree | Balanced BST | Height difference at each node is at most 1 | Search/insert/delete: $O(\log n)$ | Wrong rotation or stale heights |
| Heap | Priority tree | Parent is ordered above children | Peek: $O(1)$; insert/delete: $O(\log n)$ | Treating heap like a BST |
| Simple linear regression | Best-fit line for paired data | Least-squares residual minimum | Usually linear after stats are ready | Outliers and nonlinear data |
| Greedy technique | Best local choice each step | Greedy-choice property + optimal substructure | Depends on how choices are selected | Assuming greedy is always optimal |

## What To Say In An Exam

- Decrease-and-conquer: “One smaller instance, then extend the answer.”
- Divide-and-conquer: “Many smaller subproblems, then combine their answers.”
- AVL tree: “A BST that stays balanced using rotations.”
- Heap: “A priority structure with fast min/max access.”
- Simple linear regression: “A line chosen by least squares.”
- Greedy technique: “A local-choice strategy that needs a proof of safety.”

## High-Yield Differences

- Decrease-and-conquer vs divide-and-conquer: one recursive subproblem versus several.
- AVL tree vs heap: AVL is for ordered search; heap is for priority access.
- Heap vs sorted list: heap gives cheaper repeated updates.
- Greedy vs divide-and-conquer: greedy commits now; divide-and-conquer explores subproblems first.

## Rotation And Rebalance Reminder

- AVL rotations fix local imbalance while preserving the BST property.
- Bubble up fixes a heap after insert.
- Bubble down fixes a heap after delete.

## 1-Line Checks

- Does the problem size strictly shrink?
- Are there multiple recursive subproblems?
- Is the tree still balanced after update?
- Is the priority order preserved after insert or delete?
- Is the regression line really appropriate for the data?
- Is the greedy choice provably safe?