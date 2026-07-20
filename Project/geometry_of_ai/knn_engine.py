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
    def __init__(self, k=3, metric='euclidean', priority=None, normalize=False):
        metric_functions = {
            'euclidean': euclidean_distance,
            'manhattan': manhattan_distance,
        }
        if metric not in metric_functions:
            raise ValueError(f"unsupported metric '{metric}'. Use 'euclidean' or 'manhattan'.")

        self.k = k
        self.metric_name = metric
        self.metric_fn = metric_functions[metric]
        self.priority = priority or ["Apple", "Banana", "Lemon"]
        self.normalize = normalize
        self.train_data = []
        self._feature_min = None
        self._feature_max = None

    def fit(self, data):
        """Load training data into the classifier. If normalize=True, fits
        min-max scaling on the training features and stores it for use on
        both training and query points, so distance is computed on a
        comparable 0-1 scale for weight and sweetness."""
        if self.normalize:
            self._feature_min = {
                'weight': min(p['weight'] for p in data),
                'sweetness': min(p['sweetness'] for p in data),
            }
            self._feature_max = {
                'weight': max(p['weight'] for p in data),
                'sweetness': max(p['sweetness'] for p in data),
            }
            self.train_data = [self._scale_point(p) for p in data]
        else:
            self.train_data = data

    def _scale_point(self, point):
        """Min-max scale weight/sweetness into [0, 1] using training-set bounds,
        preserving any other keys (id, class, desc) unchanged."""
        scaled = dict(point)
        for feature in ('weight', 'sweetness'):
            lo, hi = self._feature_min[feature], self._feature_max[feature]
            span = hi - lo
            scaled[feature] = (point[feature] - lo) / span if span > 0 else 0.0
        return scaled

    def predict(self, test_point):
        """
        Predicts the class of a single test point.
        1. Calculate distances to all training points.
        2. Sort by distance.
        3. Select top k.
        4. Count votes.
        5. Break ties if needed.
        6. Return winning class.
        """
        # --- Input validation ---
        if not isinstance(self.k, int) or self.k <= 0:
            raise ValueError(f"k must be a positive integer, got {self.k}")
        if self.k > len(self.train_data):
            raise ValueError(f"k ({self.k}) cannot exceed training data size ({len(self.train_data)})")
        if test_point['weight'] < 0:
            raise ValueError("weight must be >= 0")
        if test_point['sweetness'] < 1 or test_point['sweetness'] > 10:
            raise ValueError("sweetness must be between 1 and 10")

        # --- Scale query point to match training feature space, if enabled ---
        query_point = self._scale_point(test_point) if self.normalize else test_point

        # --- Compute distances and sort ---
        distances = []
        for point in self.train_data:
            dist = self.metric_fn(query_point, point)
            distances.append((dist, point))
        distances.sort(key=lambda x: x[0])

        # --- Select top k neighbors ---
        neighbors = distances[:self.k]

        # --- Count votes ---
        votes = {}
        for dist, point in neighbors:
            cls = point['class']
            if cls not in votes:
                votes[cls] = 0
            votes[cls] += 1

        max_votes = max(votes.values())
        top_classes = [cls for cls, count in votes.items() if count == max_votes]

        if len(top_classes) == 1:
            return top_classes[0]

        # --- Tie-break ---
        return self._tie_break(top_classes, neighbors)

    def _tie_break(self, tied_classes, neighbor_details):
        """
        Tie-breaking logic:
        1. Pick class with lowest average distance among tied classes.
        2. If still tied, fall back to CLASS_PRIORITY order.
        """
        # Compute average distance per tied class
        avg_dist = {}
        for cls in tied_classes:
            dists = [dist for dist, point in neighbor_details if point['class'] == cls]
            avg_dist[cls] = sum(dists) / len(dists)

        min_avg = min(avg_dist.values())
        closest = [cls for cls in tied_classes if avg_dist[cls] == min_avg]

        if len(closest) == 1:
            return closest[0]

        # Fall back to priority order
        for cls in self.priority:
            if cls in closest:
                return cls
