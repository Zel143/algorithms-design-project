# Geometry of AI Decisions

Group 3 — k-Nearest Neighbors implementation comparing Euclidean and Manhattan decision boundaries on a custom 2D fruit-classification dataset.

**Status: Implementation complete. All tests passing. Ready for final report packaging.**

---

## File Structure

| File | Purpose |
|------|---------|
| `data_loader.py` | 18-point fruit dataset, 8 boundary test points, and class priority (Ranzel) |
| `knn_engine.py` | Euclidean/Manhattan distance functions, KNNClassifier with deterministic tie-breaking and optional min-max normalization (Luigi) |
| `testing_harness.py` | Runs all test points across k=1,3,5 and both metrics; prints comparison tables (Stephanie) |
| `evaluation.py` | Quantitative evaluation on a held-out labeled split: accuracy/precision/recall/F1/confusion matrix, raw-vs-normalized comparison, scikit-learn cross-check, and a scalability test |
| `test_knn.py` | 10 automated unit tests covering distances, edge cases, tie-breaking, and normalization (10/10 passing) |
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

**Quantitative evaluation (metrics, normalization, scikit-learn check, scalability):**
```bash
python evaluation.py
```
Requires `numpy` and `scikit-learn` in addition to `matplotlib`.

---

## Methodology

Zero-dependency k-NN implementation using a structured tie-breaking approach to guarantee deterministic boundaries.

1. Compute pairwise distances using either Euclidean or Manhattan metrics.
2. Identify the `k` nearest neighbors.
3. Determine the class via majority vote.
4. Tie-breaking: if two or more classes tie on vote count, pick the one with the lowest *average distance* among its neighbors. If still tied, fall back to the hardcoded priority (`Apple > Banana > Lemon`).

We plot decision boundaries for both Euclidean (circular contours) and Manhattan (diamond contours) to assess how the distance metric influences classifications on boundary test points.

---

## Quantitative Evaluation

The 8 hand-picked boundary test points in `data_loader.py` have descriptions
but no ground-truth label, so they can only support prediction *comparisons*
(Euclidean vs. Manhattan), not accuracy metrics. `evaluation.py` addresses
this and the review feedback below by evaluating on a stratified 80/20
holdout of a 450-point synthetic dataset (150 points per class, sampled from
the same three fruit clusters as the curated dataset, seed=42).

- **Feature normalization as part of the main evaluation.** `KNNClassifier`
  now accepts `normalize=True`, which fits min-max scaling on the training
  set and applies it to both training and query points. `evaluation.py` runs
  every `k` × metric combination with and without normalization, rather than
  only recommending it. Normalization improves accuracy on this dataset from
  ~0.86–0.91 (raw) to ~0.93–0.98 (normalized), because sweetness (range ~1–10)
  would otherwise be dwarfed by weight (range ~60–260g) in the distance
  calculation.
- **Quantitative accuracy metrics.** For every configuration, `evaluation.py`
  reports accuracy, per-class precision/recall/F1, and a confusion matrix
  (via `sklearn.metrics`), instead of only a side-by-side prediction table.
- **External validation against scikit-learn.** Each configuration is also
  run through `sklearn.neighbors.KNeighborsClassifier` on the identical
  train/test split and feature scaling. Custom and scikit-learn predictions
  agree on 100% of test points in nearly all configurations; the one
  exception (k=5, Euclidean, unnormalized) agrees on 98.9%, which traces to
  a tie-breaking difference rather than a distance-computation bug.
- **Scalability.** `evaluation.py` times prediction across training sets of
  18, 150, 900, and 3,000 points. Per-query latency grows roughly linearly
  (~0.03ms → ~7.4ms), consistent with the documented O(n) brute-force search
  and confirming the implementation has no hidden superlinear cost.

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
