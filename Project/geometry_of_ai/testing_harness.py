from knn_engine import KNNClassifier
from data_loader import get_training_data, get_test_points, get_priority
import time

def run_experiment(k_value, metric):
    print(f"\n--- Experiment: k={k_value}, Metric={metric} ---")
    
    train_data = get_training_data()
    test_points = get_test_points()
    priority = get_priority()
    
    knn = KNNClassifier(k=k_value, metric=metric, priority=priority)
    knn.fit(train_data)
    
    start_time = time.perf_counter()
    
    predictions = []
    for point in test_points:
        test_id = point['id']
        pred_class = knn.predict(point)
        predictions.append((test_id, point, pred_class))
        
    end_time = time.perf_counter()
    
    print(f"Total execution time: {end_time - start_time:.6f} seconds")
    for test_id, point, pred_class in predictions:
        print(f"{test_id} (Point {point}): Predicted -> {pred_class}")
        
    return predictions

if __name__ == "__main__":
    # Runs for Stephanie to validate implementation and compile comparison matrix
    for k in [1, 3, 5]:
        run_experiment(k_value=k, metric='euclidean')
        run_experiment(k_value=k, metric='manhattan')
