# Geometry of AI Decisions - Starter Kit

This folder contains the initial Python scaffold for the Group 3 Algorithms Project.

## File Structure

- `data_loader.py`: Contains the 18-point fruit dataset and 8 test points (Ranzel).
- `knn_engine.py`: Core logic for Euclidean/Manhattan distances and the KNN class skeleton (Jon).
- `testing_harness.py`: Script to run experiments across different k-values and metrics (Stephanie).
- `main.py`: (To be created) The final entry point with visualization.

## Teammate Instructions

### Jon (Algorithm Architect)
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
3. Coordinate with Jon to get the boundary data points.

### Melprin (Complexity)
1. Analyze `knn_engine.py` for time and space complexity.
2. Use the `Execution Time` printout in `testing_harness.py` for empirical data.

## How to Run
```bash
python testing_harness.py
```
*(Note: Predictions will show "Not Implemented" until Jon completes the engine.)*
