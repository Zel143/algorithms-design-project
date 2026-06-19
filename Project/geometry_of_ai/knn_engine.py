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
        Predicts the class of a single test point.
        TODO (Jon): Implement the full k-NN logic here.
        1. Calculate distances to all training points.
        2. Sort by distance.
        3. Handle ties in distance using the priority rules.
        4. Select top k.
        5. Count votes.
        6. Return winning class.
        """
        # Placeholder for implementation
        return "Not Implemented"

    def _tie_break(self, tied_classes, neighbor_details):
        """
        TODO (Jon): Implement tie-breaking logic.
        1. Average distance among tied classes.
        2. Final fallback to CLASS_PRIORITY.
        """
        pass
