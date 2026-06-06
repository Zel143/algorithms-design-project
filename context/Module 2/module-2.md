# Module 2 Study Note

## 1. Decrease-and-Conquer

### Problem summary
Solve one problem by reducing it to one smaller instance, then extend the smaller solution back to the original input.

Common forms in this module:
- Decrease by 1: selection sort, insertion sort, linear search, topological sort by vertex removal.
- Decrease by k: batch maximum, counting, partial sum, block equality check, k-step search.
- Decrease by a factor: binary search, fast exponentiation, tournament maximum, interval halving, power-of-two check.

### Idea
The key idea is that only one recursive or iterative subproblem remains at each step.

The algorithm usually does one of these:
- Remove one item or vertex.
- Remove a fixed block of k items.
- Cut the input size in half.

The useful invariant is simple: the processed part is already fixed, and the remaining part is the smaller instance we still need to solve.

### Correctness argument
If each step really produces an equivalent smaller instance, then solving the smaller instance and extending it preserves correctness.

For these examples, the correctness argument depends on a local invariant:
- Selection sort: the left prefix is already sorted after each pass.
- Linear search: every skipped element has already been checked and is not the key.
- Topological sort: every removed vertex has in-degree 0, so it can safely appear next.
- Binary search: the target, if it exists, stays inside the retained half.
- Fast exponentiation: the exponentiation identity lets us reuse the result of the smaller power.

### Complexity
The recurrence depends on how much the problem shrinks:
- Decrease by 1: often T(n) = T(n - 1) + f(n).
- Decrease by k: often T(n) = T(n - k) + f(n).
- Decrease by half: often T(n) = T(n / 2) + f(n).

Typical costs from the lecture:
- Selection sort: O(n^2) time, O(1) space.
- Linear search: O(n) time, O(1) space.
- Topological sort by vertex removal: O(V + E) with the right bookkeeping.
- Binary search: O(log n) time, O(1) iterative space.
- Fast exponentiation: O(log n) time.

### Edge cases
- Empty input: return immediately or report failure.
- Size 1: this is usually the base case.
- Already sorted input: selection sort still does the same comparisons.
- Duplicate values: search and equality-based examples must define what counts as a match.
- Non-DAG graph: topological sort fails because no valid order exists.
- Odd-sized inputs in k-step or halving examples: the last block may be smaller than k.

## 2. Divide-and-Conquer

### Problem summary
Split a problem into multiple subproblems, solve them recursively, and combine their answers.

Examples from the lecture:
- Maximum element in an array.
- Sum of an array.
- Count occurrences of a value.
- Merge sort.
- Closest pair of points.
- Majority element.

### Idea
Divide-and-conquer always has three steps:
1. Divide the input.
2. Conquer the smaller subproblems.
3. Combine the results.

The main difference from decrease-and-conquer is that there are multiple subproblems, not just one.

### Correctness argument
The proof is usually a small induction.

If the divide step partitions the input correctly and the combine step correctly merges the sub-results, then the whole algorithm is correct.

Useful invariants from the examples:
- Merge sort: each half is sorted before the merge step.
- Maximum element: the max of the whole array is the larger of the two half-maxima.
- Count occurrences: the total count is the sum of the left and right counts.
- Closest pair: after checking each half, only the strip can improve the answer.
- Majority element: a global majority must also survive the recursive comparison and final count.

### Complexity
The general recurrence is:

T(n) = aT(n/b) + f(n)

Here:
- a is the number of subproblems.
- n/b is the size of each subproblem.
- f(n) is the work for dividing and combining.

Common lecture results:
- Merge sort: O(n log n).
- Maximum, sum, and count-occurrence examples: usually O(n log n) if solved recursively with partitioning, or O(n) if the combine step is linear and the recursion is shallow.
- Closest pair: the standard divide-and-conquer version is O(n log n).

### Edge cases
- Empty array: return the identity value or error, depending on the problem.
- Size 1: this is the base case for most array problems.
- Odd-sized arrays: one side may have one extra item.
- Duplicate values: important for majority element and counting problems.
- Non-unique answers: top-level reasoning should allow more than one valid output when the problem permits it.

## 3. AVL Trees

### Problem summary
An AVL tree is a binary search tree that stays balanced so search, insert, and delete remain fast in the worst case.

The balance factor is:

height(left subtree) - height(right subtree)

For AVL trees, the balance factor at every node must stay in {-1, 0, 1}.

### Idea
Maintain the BST property and rebalance with rotations after insertions and deletions.

The main cases are:
- LL rotation
- RR rotation
- LR rotation
- RL rotation

The key invariant is local: after rebalancing a node, the subtree rooted there is again a valid AVL tree and still a valid BST.

### Correctness argument
Rotations only rearrange local pointers; they do not change the in-order ordering of keys.

That means rotations preserve the BST property while reducing the height difference that violated AVL balance.

After insertion or deletion:
- Recompute heights.
- Check the balance factor.
- Rotate at the first unbalanced ancestor.
- Repeat upward if needed.

That is why the algorithm stays correct: each repair restores the AVL condition without breaking ordering.

### Complexity
- Search: O(log n) when balanced.
- Insert: O(log n).
- Delete: O(log n).
- Rotations themselves are O(1).

The lecture's comparison with an unbalanced BST is the important contrast: a plain BST can degrade to O(n), while AVL trees keep height logarithmic.

### Edge cases
- Empty tree: insert becomes the first node.
- Single node: balance factor is 0.
- Duplicate keys: the tree policy must be defined in advance.
- Deletion of root or repeated deletions: can trigger multiple rebalances.
- All four rotation cases must be identified correctly.

## 4. Fast comparisons to remember

- Decrease-and-conquer uses one smaller subproblem.
- Divide-and-conquer uses several smaller subproblems.
- AVL trees are for ordered search.
- Heaps are for priority access, not ordered search.
- Selection sort is a decrease-by-1 idea.
- Binary search is a decrease-by-a-factor idea.
- Merge sort is divide-and-conquer.

## 5. One-line exam checklist

- What is the input and output?
- What smaller problem is created?
- What invariant stays true after each step?
- What is the recurrence or runtime?
- What are the base cases and edge cases?
