# Module 2 Review

Sources: Module 2 content files in [Module 2](Module%202/)

This review covers the Module 2 topics from the lecture files: decrease-and-conquer, divide-and-conquer, AVL trees, heaps, simple linear regression, and greedy technique.

## 1) Decrease-and-Conquer

What it is: solve the problem by reducing it to a smaller instance of the same problem, then extend the smaller solution.

Think about:
- Does each step reduce the input size?
- What is the base case?
- How is the answer reconstructed?

Correctness hook: the reduced problem must stay equivalent to the original goal, and the size must strictly decrease.

Complexity pattern: often a recurrence like $T(n) = T(n-1) + f(n)$ or $T(n) = T(n/c) + f(n)$.

Common pitfalls:
- The reduction does not actually shrink the problem.
- The base case is missing.
- The reconstruction step changes the answer.

Quick self-check:
1. Explain the difference between decrease-by-one and decrease-by-a-factor.
2. Give one example where this strategy is better than brute force.

## 2) Divide-and-Conquer

What it is: divide the problem into smaller subproblems, solve them recursively, and combine the results.

Think about:
- What are the subproblems?
- How many are there?
- How expensive is the combine step?

Correctness hook: if the subproblems are correct and the combine step is correct, then the whole solution is correct.

Complexity pattern: often written as $T(n) = aT(n/b) + f(n)$.

Common pitfalls:
- Forgetting the combine step.
- Assuming every split is automatically efficient.
- Mixing divide-and-conquer with dynamic programming.

Quick self-check:
1. State the divide, conquer, and combine parts of merge sort.
2. Explain why binary search is a divide-and-conquer idea.

## 3) AVL Tree

What it is: a self-balancing binary search tree that keeps height differences small.

Think about:
- What balance condition must hold?
- When do rotations happen?
- Why does keeping the tree balanced matter?

Correctness hook: rotations repair local imbalance while preserving the binary-search-tree property.

Complexity pattern: search, insert, and delete are typically $O(\log n)$.

Common pitfalls:
- Forgetting to update heights.
- Using the wrong rotation type.
- Confusing AVL balance with heap order.

Quick self-check:
1. What is the AVL balance condition?
2. When would you use a left rotation versus a right rotation?

## 4) Heap

What it is: a tree-based structure used for efficient access to the min or max element.

Think about:
- Is it a min-heap or a max-heap?
- What property must the parent-child relationship satisfy?
- How do insertion and deletion restore the property?

Correctness hook: bubble-up and bubble-down restore heap order after updates.

Complexity pattern: peek is often $O(1)$; insert and delete are typically $O(\log n)$.

Common pitfalls:
- Confusing heap order with sorted order.
- Assuming a heap supports fast arbitrary search.
- Forgetting that a heap is not a binary search tree.

Quick self-check:
1. Why is a heap useful for priority management?
2. How does heapify restore the structure after a change?

## 5) Simple Linear Regression

What it is: a line-fit model that describes the relationship between two numerical variables.

Think about:
- What are the independent and dependent variables?
- Why use the least-squares line?
- How do you interpret slope and intercept?

Correctness hook: the fitted line minimizes the sum of squared residuals among candidate lines.

Complexity pattern: after summary statistics are available, fitting is typically linear in the number of data points.

Common pitfalls:
- Interpreting correlation as causation.
- Ignoring outliers.
- Applying the model to clearly nonlinear data.

Quick self-check:
1. What does the slope tell you?
2. What does a scatter plot show before fitting the line?

## 6) Greedy Technique

What it is: build a solution by repeatedly making the best local choice.

Think about:
- What is the locally best choice?
- Why does that choice remain safe?
- Does the problem have optimal substructure?

Correctness hook: greedy works only when the problem has the greedy-choice property and optimal substructure.

Complexity pattern: often efficient, but the exact cost depends on how choices are selected and maintained.

Common pitfalls:
- Thinking greedy always gives the optimal solution.
- Not proving the greedy choice is safe.
- Using greedy on a problem that needs backtracking or dynamic programming.

Quick self-check:
1. Give one example of a greedy algorithm.
2. Explain why a greedy choice can fail on some problems.

## Module 2 Summary Check

Use this to review the Module 2 summary material:
- Re-state each topic in one sentence.
- Compare decrease-and-conquer vs divide-and-conquer.
- Compare AVL trees vs heaps.
- Explain when greedy is appropriate and when it is not.

## Quiz Prep

For the Module 2 quiz topics, practice answering these kinds of prompts:
- Define the technique or data structure.
- State the main property or invariant.
- Give the typical time complexity.
- Name one common mistake.

## Interactive Practice Quiz

Answer each question before checking the key.

### Questions
1. In one sentence, what is the main idea of decrease-and-conquer? - tackle a problem and look at by batch or the array
2. What must happen to the problem size at each step in decrease-and-conquer?  - decrease number of array or problem to solve for
3. In divide-and-conquer, what are the three core phases? - divide, conquer, merge
4. Why does merge sort fit the divide-and-conquer pattern? - it merges the sort by batches
5. What balance condition must an AVL tree preserve? 
6. Why are rotations needed in an AVL tree? - to balance the tree from its core formula bst
7. What is the main structural property of a heap? dynamic memory allocation
8. What is the typical time complexity of inserting into a heap?
9. What does simple linear regression try to minimize?
10. When is a greedy algorithm safe to use? when problem is truly defined

## Fill-in-the-Blank Practice

Fill in each blank before looking at the answer key.

1. Decrease-and-conquer works by reducing a problem to a shorter instance.
2. In decrease-and-conquer, the problem size must decrease at each step.
3. Divide-and-conquer has three phases: divide, conquer, and combine.
4. Merge sort is a divide-and-conquer algorithm because it merges the array, sorts recursively, and merges the result.
5. An AVL tree is a self-balancing <=1- search tree.
6. AVL rotations restore balance while preserving the BST property.
7. A heap gives efficient access to the minimum or maximum element.
8. Heap insert is typically $O(\logn)$.
9. Simple linear regression minimizes the sum of squared residuals.
10. Greedy algorithms require the greedy-choice property and optimal substructure.

## Harder Exam-Style Problems

Answer these as if they were exam questions. Write full reasoning.

1. Compare decrease-and-conquer and divide-and-conquer using one example for each. Explain how the recurrence and solution strategy differ.
2. Given a recursion that solves a problem by reducing it to a smaller version and then doing extra work, explain how you would determine whether it is decrease-and-conquer or divide-and-conquer.
3. Explain why AVL trees are preferred over ordinary binary search trees in worst-case performance analysis.
4. A priority queue can be implemented with a heap or with a sorted list. Compare their insertion and deletion costs and explain when a heap is the better choice.
5. A data set looks roughly linear but contains a few extreme outliers. Explain how simple linear regression may be affected and what you would mention in your interpretation.
6. Explain how you would justify that a greedy algorithm is correct for a problem, and what you would say if the problem does not satisfy the greedy-choice property.

## Answer Key File

The answers are stored in [module-2-quiz-answers.md](module-2-quiz-answers.md).

## Cheat Sheet

For a condensed one-page version, use [module-2-cheat-sheet.md](module-2-cheat-sheet.md).
