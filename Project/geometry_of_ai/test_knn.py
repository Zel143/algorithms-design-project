import unittest
import math
from knn_engine import KNNClassifier, euclidean_distance, manhattan_distance

class TestKNNClassifier(unittest.TestCase):
    def setUp(self):
        # Sample training dataset
        self.toy_data = [
            {"id": "L1", "weight": 80,  "sweetness": 2.0, "class": "Lemon"},
            {"id": "L2", "weight": 95,  "sweetness": 2.5, "class": "Lemon"},
            {"id": "A1", "weight": 130, "sweetness": 6.0, "class": "Apple"},
            {"id": "A2", "weight": 145, "sweetness": 6.5, "class": "Apple"},
            {"id": "B1", "weight": 115, "sweetness": 8.0, "class": "Banana"},
            {"id": "B2", "weight": 130, "sweetness": 8.5, "class": "Banana"},
        ]
        self.priority = ["Apple", "Banana", "Lemon"]

    def test_distance_metrics(self):
        p1 = {"weight": 100, "sweetness": 3.0}
        p2 = {"weight": 104, "sweetness": 6.0}
        # Euclidean: sqrt(4^2 + 3^2) = 5.0
        self.assertAlmostEqual(euclidean_distance(p1, p2), 5.0)
        # Manhattan: |4| + |3| = 7.0
        self.assertAlmostEqual(manhattan_distance(p1, p2), 7.0)

    def test_invalid_metric(self):
        with self.assertRaises(ValueError):
            KNNClassifier(k=3, metric='chebyshev', priority=self.priority)

    def test_invalid_k(self):
        # Test negative, zero, and non-integer k
        for bad_k in [0, -3, 2.5, "three"]:
            knn = KNNClassifier(k=bad_k, metric='euclidean', priority=self.priority)
            knn.fit(self.toy_data)
            with self.assertRaises(ValueError):
                knn.predict({"weight": 100, "sweetness": 5.0})

    def test_k_greater_than_dataset(self):
        # dataset size is 6, so k=7 should fail
        knn = KNNClassifier(k=7, metric='euclidean', priority=self.priority)
        knn.fit(self.toy_data)
        with self.assertRaises(ValueError):
            knn.predict({"weight": 100, "sweetness": 5.0})

    def test_out_of_bounds_test_point(self):
        knn = KNNClassifier(k=3, metric='euclidean', priority=self.priority)
        knn.fit(self.toy_data)
        
        # Weight < 0
        with self.assertRaises(ValueError):
            knn.predict({"weight": -5, "sweetness": 5.0})
            
        # Sweetness < 1
        with self.assertRaises(ValueError):
            knn.predict({"weight": 100, "sweetness": 0.5})
            
        # Sweetness > 10
        with self.assertRaises(ValueError):
            knn.predict({"weight": 100, "sweetness": 10.5})

    def test_exact_training_point_match(self):
        # A test point that matches an existing training point exactly
        # should rank that point as nearest neighbor (dist = 0) and classify accordingly
        knn = KNNClassifier(k=1, metric='euclidean', priority=self.priority)
        knn.fit(self.toy_data)
        
        # Test against A1 coordinates (130, 6.0)
        result = knn.predict({"weight": 130, "sweetness": 6.0})
        self.assertEqual(result, "Apple")

    def test_tie_breaking_by_average_distance(self):
        # Construct a scenario where votes tie, and we check average distance.
        # Training data: 
        # Lemon at (10, 2)
        # Apple at (20, 2)
        # Test point at (14, 2)
        # k = 2 (so one Lemon, one Apple)
        # Distances: Lemon (4), Apple (6)
        # Votes: Lemon (1), Apple (1) -> Tie!
        # Average distance: Lemon (4.0), Apple (6.0). Lemon wins.
        train_set = [
            {"id": "L1", "weight": 10, "sweetness": 2.0, "class": "Lemon"},
            {"id": "A1", "weight": 20, "sweetness": 2.0, "class": "Apple"},
        ]
        knn = KNNClassifier(k=2, metric='euclidean', priority=self.priority)
        knn.fit(train_set)
        result = knn.predict({"weight": 14, "sweetness": 2.0})
        self.assertEqual(result, "Lemon")
        
        # Moving test point to (16, 2):
        # Distances: Lemon (6), Apple (4). Apple wins.
        result2 = knn.predict({"weight": 16, "sweetness": 2.0})
        self.assertEqual(result2, "Apple")

    def test_tie_breaking_by_class_priority(self):
        # Construct a scenario where votes tie AND average distances tie.
        # Training data:
        # Lemon at (10, 2)
        # Apple at (20, 2)
        # Test point exactly at (15, 2)
        # k = 2
        # Distances: Lemon (5), Apple (5) -> Tie!
        # Average distance: Lemon (5.0), Apple (5.0) -> Tie!
        # Fallback priority: Apple > Banana > Lemon. Apple wins.
        train_set = [
            {"id": "L1", "weight": 10, "sweetness": 2.0, "class": "Lemon"},
            {"id": "A1", "weight": 20, "sweetness": 2.0, "class": "Apple"},
        ]
        knn = KNNClassifier(k=2, metric='euclidean', priority=self.priority)
        knn.fit(train_set)
        result = knn.predict({"weight": 15, "sweetness": 2.0})
        self.assertEqual(result, "Apple")

        # Let's change priority to Lemon > Apple > Banana
        knn_lemon_first = KNNClassifier(k=2, metric='euclidean', priority=["Lemon", "Apple", "Banana"])
        knn_lemon_first.fit(train_set)
        result_lemon_first = knn_lemon_first.predict({"weight": 15, "sweetness": 2.0})
        self.assertEqual(result_lemon_first, "Lemon")

    def test_normalize_changes_neighbor_geometry(self):
        # Raw weight (range ~110g) numerically dwarfs raw sweetness (range
        # ~6.9), so a small weight gap outweighs a near-perfect sweetness
        # match. Min-max scaling puts both features on [0, 1], letting the
        # close sweetness match win instead -- flipping the prediction.
        train_set = [
            {"id": "L1", "weight": 80,  "sweetness": 2.0, "class": "Lemon"},
            {"id": "B1", "weight": 190, "sweetness": 8.9, "class": "Banana"},
        ]
        query = {"weight": 85, "sweetness": 8.8}

        knn_raw = KNNClassifier(k=1, metric='euclidean', priority=self.priority, normalize=False)
        knn_raw.fit(train_set)
        # Raw: L1 is closer (dist~8.4) than B1 (dist~105) despite the huge sweetness gap.
        self.assertEqual(knn_raw.predict(query), "Lemon")

        knn_norm = KNNClassifier(k=1, metric='euclidean', priority=self.priority, normalize=True)
        knn_norm.fit(train_set)
        # Scaled: B1's near-exact sweetness match now outweighs L1's small weight edge.
        self.assertEqual(knn_norm.predict(query), "Banana")

    def test_normalize_scales_test_point_with_training_bounds(self):
        knn = KNNClassifier(k=1, metric='euclidean', priority=self.priority, normalize=True)
        knn.fit(self.toy_data)
        # Exact match to a training point should still resolve as nearest
        # neighbor (distance 0) after both are scaled identically.
        result = knn.predict({"weight": 130, "sweetness": 6.0})
        self.assertEqual(result, "Apple")


if __name__ == "__main__":
    unittest.main()
