# Module 2 Quiz Answers

## Interactive Practice Quiz Answers

1. It solves a problem by reducing it to a smaller instance and extending the smaller solution.
2. The size must strictly decrease so the process reaches a base case.
3. Divide, conquer, and combine.
4. It splits the array, sorts the parts recursively, and combines them by merging.
5. The height difference between left and right subtrees must stay small, typically at most 1.
6. Rotations restore balance while preserving the binary search tree property.
7. The parent-child ordering property must hold, depending on whether it is a min-heap or max-heap.
8. $O(\log n)$.
9. The sum of squared residuals.
10. When the problem has the greedy-choice property and optimal substructure.

## Fill-in-the-Blank Answers

1. smaller
2. decrease
3. divide
4. splits
5. binary
6. balance
7. minimum
8. log n
9. squared
10. optimal

## Harder Exam-Style Sample Answers

1. Decrease-and-conquer reduces one instance to a smaller instance of the same problem, such as insertion sort-style reasoning or binary search-like shrinking, while divide-and-conquer splits into multiple subproblems, such as merge sort. The recurrence for decrease-and-conquer often has one recursive subproblem, while divide-and-conquer often has several. The combination step is usually lighter in decrease-and-conquer and more central in divide-and-conquer.
2. If the method reduces the problem to one smaller instance, it is decrease-and-conquer. If it splits the problem into two or more subproblems and combines their results, it is divide-and-conquer. The key test is whether the recursive structure has one subproblem or multiple subproblems.
3. AVL trees guarantee $O(\log n)$ worst-case height, so search, insert, and delete remain logarithmic even when keys arrive in bad order. Ordinary binary search trees can degrade to a linear chain, making operations $O(n)$. AVL trees are preferred when predictable worst-case performance matters.
4. A heap supports insertion and deletion in $O(\log n)$ and gives fast access to the minimum or maximum in $O(1)$. A sorted list gives very fast access at one end but usually costs $O(n)$ to insert because elements must be shifted. A heap is better when there are many updates and repeated priority operations.
5. Simple linear regression will try to fit a line that minimizes squared error, so outliers can pull the line away from the main cluster of points. I would mention that the slope may be distorted and that the fit may not represent the typical trend well. I would also note that the data should be inspected for whether a linear model is actually appropriate.
6. To justify greedy correctness, I would prove that the locally best choice is always safe and that the problem has optimal substructure. If the greedy-choice property does not hold, then greedy may fail even if it seems intuitive. In that case I would say a different strategy such as dynamic programming or backtracking may be needed.