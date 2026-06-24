# Geometry of AI Decisions - Starter Kit

This folder contains the initial Python scaffold for the Group 3 Algorithms Project.

## File Structure

- `data_loader.py`: Contains the 18-point fruit dataset and 8 test points (Ranzel).
- `knn_engine.py`: Core logic for Euclidean/Manhattan distances and the KNN class skeleton (Luigi).
- `testing_harness.py`: Script to run experiments across different k-values and metrics (Stephanie).
- `main.py`: (To be created) The final entry point with visualization.

## Teammate Instructions

### Luigi (Algorithm Architect)
1. Complete the `predict` method in `knn_engine.py`.
2. Ensure you implement the deterministic tie-breaking rules:
   - Vote count first.
   - Average distance of tied classes second.
   - Fixed priority (`Apple > Banana > Lemon`) last.
3. Handle edge cases: invalid k, test point matches training point, etc.

### Stephanie (Test Specialist)
1. Use `testing_harness.py` to run the 8 test cases.
2. Compare results between Euclidean and Manhattan metrics.
3. Focus on T4-T8 to see where metrics disagree.
4. Document any failures or unexpected classifications.

### Fiona (Documentation & Viz)
1. Start planning the scatter plot visualization.
2. You will need to use `matplotlib` (if allowed) or simple text-based plotting.
3. Coordinate with Luigi to get the boundary data points.

### Melprin (Complexity)
1. Analyze `knn_engine.py` for time and space complexity.
2. Use the `Execution Time` printout in `testing_harness.py` for empirical data.

## How to Run
```bash
python testing_harness.py
```
*(Note: Predictions will show "Not Implemented" until Luigi completes the engine.)*

---

## Methodology (by Fiona)

Our zero-dependency k-Nearest Neighbors implementation uses a structured tie-breaking approach to guarantee deterministic boundaries.
1. Compute pairwise distances using either Euclidean or Manhattan metrics.
2. Identify the `k` nearest neighbors.
3. Determine the class via majority vote.
4. Tie-breaking rule: if two or more classes tie, pick the one with the lowest *average distance* among its neighbors. If they still tie, use the hardcoded priority (`Apple > Banana > Lemon`).

We plot the decision boundaries for both Euclidean (circular contours) and Manhattan (diamond contours) to visually assess how the distance metric influences misclassifications on our test points.
