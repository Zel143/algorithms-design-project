# Geometry of AI Decisions

Group 3 — k-Nearest Neighbors implementation comparing Euclidean and Manhattan decision boundaries on a custom 2D fruit-classification dataset.

**Status: Implementation complete. All tests passing. Ready for final report packaging.**

---

## File Structure

| File | Purpose |
|------|---------|
| `data_loader.py` | 18-point fruit dataset, 8 boundary test points, and class priority (Ranzel) |
| `knn_engine.py` | Euclidean/Manhattan distance functions, KNNClassifier with deterministic tie-breaking (Luigi) |
| `testing_harness.py` | Runs all test points across k=1,3,5 and both metrics; prints comparison tables (Stephanie) |
| `test_knn.py` | 8 automated unit tests covering distances, edge cases, and tie-breaking (8/8 passing) |
| `main.py` | Generates side-by-side decision boundary plots and prediction comparison table |
| `test_result.md` | Stephanie's recorded output from testing_harness.py across all k and metric combinations |
| `README.md` | This file |

---

## How to Run

**Decision boundary visualization (default k=3):**
```bash
python main.py
```
Outputs `decision_boundaries_k3.png` and prints a prediction comparison table.

**Run with a different k value:**
```bash
python main.py 5
```

**Experiment harness (k=1, 3, 5 × Euclidean and Manhattan):**
```bash
python testing_harness.py
```

**Unit tests:**
```bash
python -m unittest test_knn.py
```

---

## Methodology

Zero-dependency k-NN implementation using a structured tie-breaking approach to guarantee deterministic boundaries.

1. Compute pairwise distances using either Euclidean or Manhattan metrics.
2. Identify the `k` nearest neighbors.
3. Determine the class via majority vote.
4. Tie-breaking: if two or more classes tie on vote count, pick the one with the lowest *average distance* among its neighbors. If still tied, fall back to the hardcoded priority (`Apple > Banana > Lemon`).

We plot decision boundaries for both Euclidean (circular contours) and Manhattan (diamond contours) to assess how the distance metric influences classifications on boundary test points.

---

## Complexity

| Operation | Complexity |
|-----------|-----------|
| Per-query distance computation | O(n) |
| Neighbor selection (full sort) | O(n log n) |
| Space | O(n) |

Where `n` is the number of training points (18 in the current dataset).

---

## Team Contributions

| Role | Member | Deliverable |
|------|--------|-------------|
| Dataset & Edge Cases | Ranzel | `data_loader.py`, test point design, tie-breaking rules |
| Algorithm Architect | Luigi | `knn_engine.py` — full predict + tie-breaking implementation |
| Test Specialist | Stephanie | `testing_harness.py`, `test_result.md` — validated all k/metric combinations |
| Documentation & Viz | Fiona | `main.py` — decision boundary visualization; methodology writeup |
| Complexity & Reporter | Melprin | Complexity analysis, report compilation |
