import math

def euclidean_distance(p1, p2):
    """
    Calculates Euclidean Distance: sqrt((x2-x1)^2 + (y2-y1)^2)
    p1, p2: dictionaries with 'weight' and 'sweetness'
    """
    return math.sqrt((p1['weight'] - p2['weight'])**2 + (p1['sweetness'] - p2['sweetness'])**2)

def manhattan_distance(p1, p2):
    """
    Calculates Manhattan Distance: |x2-x1| + |y2-y1|
    p1, p2: dictionaries with 'weight' and 'sweetness'
    """
    return abs(p1['weight'] - p2['weight']) + abs(p1['sweetness'] - p2['sweetness'])

class KNNClassifier:
    def __init__(self, k=3, metric='euclidean', priority=None):
        self.k = k
        self.metric_name = metric
        self.metric_fn = euclidean_distance if metric == 'euclidean' else manhattan_distance
        self.priority = priority or ["Apple", "Banana", "Lemon"]
        self.train_data = []

    def fit(self, data):
        """Load training data into the classifier."""
        self.train_data = data

    def predict(self, test_point):
        """
        Predicts the class of a single test point using k-NN.

        Tie-breaking: If a vote tie occurs among classes, select the class
        with the smallest average distance to its k neighbors. This is
        deterministic and insertion-order independent.

        Steps:
        1. Calculate distances to all training points.
        2. Sort by distance ascending.
        3. Select top k nearest neighbors.
        4. Count votes per class.
        5. Apply tie-breaking if needed.
        6. Return winning class label.
        """
        # Step 1: Compute distances to all training points
        distances = [
            (self.metric_fn(test_point, point), point['label'])
            for point in self.train_data
        ]

        # Step 2: Sort by distance ascending
        distances.sort(key=lambda t: t[0])

        # Step 3: Take k nearest neighbors
        k_nearest = distances[:self.k]

        # Step 4: Count votes per class
        vote_counts = {}
        for dist, label in k_nearest:
            vote_counts[label] = vote_counts.get(label, 0) + 1

        # Step 5: Find the maximum vote count
        max_votes = max(vote_counts.values())
        top_classes = [label for label, count in vote_counts.items()
                       if count == max_votes]

        # Step 6: Return immediately if no tie
        if len(top_classes) == 1:
            return top_classes[0]

        # Step 7: Tie-break using average distance per tied class
        neighbor_details = [(dist, label) for dist, label in k_nearest]
        return self._tie_break(top_classes, neighbor_details)

    def _tie_break(self, tied_classes, neighbor_details):
        """
        Tie-breaking logic for vote-tied classes.

        1. Compute the average distance for each tied class from its
           neighbors in the k-nearest list.
        2. Select the class with the smallest average distance.
        3. Final fallback to CLASS_PRIORITY if averages are exactly equal.
        """
        # Step 1: Calculate average distance for each tied class
        avg_distances = {}
        for label in tied_classes:
            class_distances = [d for d, l in neighbor_details if l == label]
            avg_distances[label] = (
                sum(class_distances) / len(class_distances)
                if class_distances else float('inf')
            )

        # Step 2: Find the minimum average distance among tied classes
        min_avg = min(avg_distances.values())
        best_classes = [lbl for lbl in tied_classes
                        if avg_distances[lbl] == min_avg]

        # Step 3: Return if unique winner
        if len(best_classes) == 1:
            return best_classes[0]

        # Step 4: Final fallback — fixed class priority: Apple, Banana, Lemon
        for label in self.priority:
            if label in best_classes:
                return label

        # Safety net (should never reach here)
        return best_classes[0]
