"""
Evaluation Suite for "The Geometry of AI Decisions"

Addresses reviewer feedback on the original prediction-comparison-only
evaluation:

1. Feature normalization is run as part of the main evaluation (raw vs.
   min-max scaled features), not just noted as a future recommendation.
2. Quantitative accuracy metrics: accuracy, per-class precision/recall/F1,
   and a confusion matrix, computed on a held-out labeled test split
   (the original data_loader.py test points have no ground-truth label,
   only a description, so they cannot support these metrics).
3. External validation: predictions and accuracy are cross-checked against
   scikit-learn's KNeighborsClassifier on the identical train/test split.
4. Scalability check: runtime is measured across dataset sizes generated
   from the same three fruit clusters to see how the brute-force O(n)
   search actually scales.

Run with:
    python evaluation.py
"""

import time
import numpy as np
from sklearn.neighbors import KNeighborsClassifier as SKKNeighbors
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split

from knn_engine import KNNClassifier
from data_loader import get_priority

CLASS_LABELS = ["Apple", "Banana", "Lemon"]
RNG_SEED = 42

# Cluster parameters (mean, std) reused from the curated 18-point dataset in
# data_loader.py, so the synthetic data represents the same three fruits.
CLUSTER_PARAMS = {
    "Lemon":  {"weight": (105, 20), "sweetness": (3.2, 0.8)},
    "Apple":  {"weight": (165, 22), "sweetness": (6.7, 0.6)},
    "Banana": {"weight": (145, 22), "sweetness": (8.6, 0.5)},
}


def generate_synthetic_dataset(n_per_class, seed=RNG_SEED):
    """Generate a labeled dataset by sampling each fruit cluster from a
    Gaussian centered on the original data_loader.py points. Deterministic
    given `seed`, so results are reproducible across runs."""
    rng = np.random.default_rng(seed)
    data = []
    idx = 0
    for cls, params in CLUSTER_PARAMS.items():
        weights = rng.normal(params["weight"][0], params["weight"][1], n_per_class)
        sweetness = rng.normal(params["sweetness"][0], params["sweetness"][1], n_per_class)
        for w, s in zip(weights, sweetness):
            idx += 1
            data.append({
                "id": f"{cls[0]}{idx}",
                "weight": round(max(1.0, float(w)), 1),
                "sweetness": round(min(10.0, max(1.0, float(s))), 1),
                "class": cls,
            })
    return data


def to_xy(data):
    X = np.array([[p["weight"], p["sweetness"]] for p in data])
    y = np.array([p["class"] for p in data])
    return X, y


def rows_to_dicts(X, y=None):
    if y is None:
        return [{"weight": float(x[0]), "sweetness": float(x[1])} for x in X]
    return [{"weight": float(x[0]), "sweetness": float(x[1]), "class": c} for x, c in zip(X, y)]


# --- 2. Quantitative metrics -------------------------------------------------

def compute_metrics(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, labels=CLASS_LABELS, average=None, zero_division=0)
    recall = recall_score(y_true, y_pred, labels=CLASS_LABELS, average=None, zero_division=0)
    f1 = f1_score(y_true, y_pred, labels=CLASS_LABELS, average=None, zero_division=0)
    cm = confusion_matrix(y_true, y_pred, labels=CLASS_LABELS)
    return acc, precision, recall, f1, cm


def print_metrics(title, y_true, y_pred):
    acc, precision, recall, f1, cm = compute_metrics(y_true, y_pred)
    print(f"\n--- {title} ---")
    print(f"Accuracy: {acc:.4f}")
    print(f"{'Class':<10} | {'Precision':<10} | {'Recall':<10} | {'F1':<10}")
    for i, cls in enumerate(CLASS_LABELS):
        print(f"{cls:<10} | {precision[i]:<10.4f} | {recall[i]:<10.4f} | {f1[i]:<10.4f}")
    print(f"Confusion Matrix (rows=true, cols=predicted), labels={CLASS_LABELS}")
    header = " " * 10 + "".join(f"{c:>10}" for c in CLASS_LABELS)
    print(header)
    for cls, row in zip(CLASS_LABELS, cm):
        print(f"{cls:<10}" + "".join(f"{v:>10}" for v in row))
    return acc


# --- 1 & 3. Normalization + scikit-learn cross-check -------------------------

def evaluate_configuration(X_train, y_train, X_test, y_test, k, metric, normalize):
    priority = get_priority()
    train_data = rows_to_dicts(X_train, y_train)
    test_dicts = rows_to_dicts(X_test)

    custom = KNNClassifier(k=k, metric=metric, priority=priority, normalize=normalize)
    custom.fit(train_data)
    custom_preds = np.array([custom.predict(p) for p in test_dicts])

    # scikit-learn reference model on the identical split, with matching
    # feature scaling so the comparison isolates algorithmic agreement.
    if normalize:
        mn, mx = X_train.min(axis=0), X_train.max(axis=0)
        span = np.where(mx - mn == 0, 1, mx - mn)
        X_train_sk = (X_train - mn) / span
        X_test_sk = (X_test - mn) / span
    else:
        X_train_sk, X_test_sk = X_train, X_test

    sk_model = SKKNeighbors(n_neighbors=k, metric=metric)
    sk_model.fit(X_train_sk, y_train)
    sk_preds = sk_model.predict(X_test_sk)

    label = f"k={k}, metric={metric}, normalize={normalize}"
    print(f"\n{'=' * 70}\n{label}\n{'=' * 70}")

    custom_acc = print_metrics(f"Custom KNNClassifier ({label})", y_test, custom_preds)
    sk_acc = print_metrics(f"scikit-learn KNeighborsClassifier ({label})", y_test, sk_preds)

    agreement = float(np.mean(custom_preds == sk_preds))
    print(f"\nCustom vs. scikit-learn prediction agreement: {agreement:.2%} "
          f"({int(agreement * len(y_test))}/{len(y_test)} test points)")
    print(f"Accuracy delta (custom - sklearn): {custom_acc - sk_acc:+.4f}")

    return custom_acc, sk_acc, agreement


def run_main_evaluation():
    """Held-out evaluation across k, metric, and normalization on a
    stratified 80/20 split of a 450-point synthetic dataset (150/class)."""
    data = generate_synthetic_dataset(n_per_class=150)
    X, y = to_xy(data)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=RNG_SEED
    )
    print(f"Held-out evaluation set: {len(X_train)} train / {len(X_test)} test "
          f"points (stratified 80/20 split, seed={RNG_SEED})")

    results = []
    for k in (1, 3, 5):
        for metric in ("euclidean", "manhattan"):
            for normalize in (False, True):
                custom_acc, sk_acc, agreement = evaluate_configuration(
                    X_train, y_train, X_test, y_test, k, metric, normalize
                )
                results.append((k, metric, normalize, custom_acc, sk_acc, agreement))

    print(f"\n{'=' * 70}\nSummary: raw vs. normalized features\n{'=' * 70}")
    print(f"{'k':<4} | {'Metric':<10} | {'Normalized':<11} | {'Custom Acc':<11} | "
          f"{'sklearn Acc':<12} | {'Agreement':<10}")
    for k, metric, normalize, custom_acc, sk_acc, agreement in results:
        print(f"{k:<4} | {metric:<10} | {str(normalize):<11} | {custom_acc:<11.4f} | "
              f"{sk_acc:<12.4f} | {agreement:<10.2%}")

    return results


# --- 4. Scalability test -----------------------------------------------------

def run_scalability_test():
    """Time custom KNN prediction across growing dataset sizes to confirm
    the expected O(n) per-query scaling of brute-force search."""
    print(f"\n{'=' * 70}\nScalability test (brute-force O(n) search)\n{'=' * 70}")
    sizes_per_class = [6, 50, 300, 1000]
    query_count = 100
    priority = get_priority()

    print(f"{'Train size':<12} | {'Total time (s)':<16} | {'Avg per query (ms)':<20}")
    for n_per_class in sizes_per_class:
        data = generate_synthetic_dataset(n_per_class=n_per_class, seed=RNG_SEED)
        queries = generate_synthetic_dataset(n_per_class=max(1, query_count // 3), seed=RNG_SEED + 1)
        queries = rows_to_dicts(*to_xy(queries))[:query_count]

        knn = KNNClassifier(k=3, metric="euclidean", priority=priority)
        knn.fit(data)

        start = time.perf_counter()
        for q in queries:
            knn.predict(q)
        elapsed = time.perf_counter() - start

        avg_ms = (elapsed / len(queries)) * 1000
        print(f"{len(data):<12} | {elapsed:<16.6f} | {avg_ms:<20.4f}")


if __name__ == "__main__":
    run_main_evaluation()
    run_scalability_test()
