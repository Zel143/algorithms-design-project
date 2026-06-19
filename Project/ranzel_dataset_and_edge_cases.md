# Ranzel Starter Output: Dataset and Edge Cases

Project: The Geometry of AI Decisions  
Role: Data Curator & Edge-Case Manager  
Assignee: Ranzel Jude M. Virtucio

## Dataset Theme

The project will use a custom 2D fruit-classification dataset.

- x-axis: Weight in grams
- y-axis: Sweetness rating from 1 to 10
- Class labels: Lemon, Apple, Banana

This theme is easy to explain visually because each point can be plotted on a scatter plot. The dataset intentionally includes overlapping regions so Euclidean and Manhattan distance can produce different nearest-neighbor behavior near boundaries.

## Training Dataset

| Point ID | Weight (g) | Sweetness | Class |
|----------|------------|-----------|-------|
| L1 | 80 | 2.0 | Lemon |
| L2 | 95 | 2.5 | Lemon |
| L3 | 110 | 3.0 | Lemon |
| L4 | 120 | 4.0 | Lemon |
| L5 | 135 | 3.5 | Lemon |
| L6 | 150 | 4.5 | Lemon |
| A1 | 130 | 6.0 | Apple |
| A2 | 145 | 6.5 | Apple |
| A3 | 160 | 7.0 | Apple |
| A4 | 175 | 6.2 | Apple |
| A5 | 190 | 7.5 | Apple |
| A6 | 205 | 6.8 | Apple |
| B1 | 115 | 8.0 | Banana |
| B2 | 130 | 8.5 | Banana |
| B3 | 145 | 9.0 | Banana |
| B4 | 160 | 8.2 | Banana |
| B5 | 175 | 9.3 | Banana |
| B6 | 190 | 8.7 | Banana |

## Test Points

| Test ID | Weight (g) | Sweetness | Purpose | Expected Observation |
|---------|------------|-----------|---------|----------------------|
| T1 | 100 | 2.8 | Normal lemon case | Should classify as Lemon for most k values. |
| T2 | 155 | 6.8 | Normal apple case | Should classify as Apple for most k values. |
| T3 | 150 | 8.7 | Normal banana case | Should classify as Banana for most k values. |
| T4 | 135 | 5.2 | Lemon-Apple boundary | Useful for checking boundary sensitivity. |
| T5 | 145 | 7.6 | Apple-Banana boundary | May shift depending on k and distance metric. |
| T6 | 122 | 6.2 | Three-class mixed area | Useful for comparing Euclidean vs. Manhattan votes. |
| T7 | 140 | 4.0 | Near Lemon and Apple by different dimensions | Good candidate for metric disagreement. |
| T8 | 160 | 7.6 | Near Apple and Banana clusters | Good candidate for split-vote testing. |

## Edge Cases To Handle

| Edge Case | Example | Required Handling |
|-----------|---------|-------------------|
| Invalid k | k = 0 or k < 0 | Reject with a clear error message. |
| k larger than dataset | k = 25 with 18 training points | Reject or cap k at the dataset size; choose one rule before coding. |
| Even-k split vote | k = 4 with two Apple and two Banana neighbors | Apply the tie-breaking rule below. |
| Exact distance tie | Two or more neighbors have the same distance from the test point | Sort by distance, then class priority, then point ID for deterministic output. |
| Duplicate coordinates | Two points share the same x and y but have different labels | Keep both points and let voting resolve the conflict. |
| Test point equals training point | T = A3 coordinates | The exact matching point should become the nearest neighbor with distance 0. |
| Out-of-range sweetness | Sweetness = 11 or -1 | Reject as invalid input because the scale is defined as 1 to 10. |
| Negative weight | Weight = -20 | Reject as invalid input because fruit weight cannot be negative. |

## Proposed Tie-Breaking Rules

Use deterministic rules so repeated runs always produce the same classification.

1. Count the class votes among the k nearest neighbors.
2. If one class has the highest vote count, return that class.
3. If there is a vote tie among multiple classes:
   - For each tied class, compute the average distance from the query point to its k nearest neighbors.
   - Select the tied class with the smallest average distance.
4. If tie persists (rare edge case), use fixed class priority: Apple, Banana, Lemon (final fallback).

**Rationale:** This rule is insertion-order independent and geometrically sound. Shuffling the training data produces identical predictions. It leverages the distance metrics at the core of our comparison study.

## Handoff Notes

For Jon:
- Use the tables above as the initial hardcoded dataset while drafting the k-NN algorithm flow.
- Include input validation for k, weight, and sweetness.
- Implement sorting so tied distances produce deterministic output.

For Stephanie:
- Start the testing matrix with k = 1, k = 3, and k = 5.
- Run each test point once with Euclidean distance and once with Manhattan distance.
- Mark T4, T5, T6, T7, and T8 as boundary-sensitive cases.

For Fiona:
- Include the dataset table and edge-case table in the report appendix or methodology section.
- Use the dataset theme to explain the scatter plot axes clearly.

## References

See [ranzel_dataset_references.md](ranzel_dataset_references.md) for ACM-style source citations.
