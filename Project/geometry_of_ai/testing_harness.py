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
    
    results = []
    
    start_time = time.perf_counter()
    for tp in test_points:
        prediction = knn.predict(tp)
        results.append({
            "id": tp['id'],
            "desc": tp['desc'],
            "predicted": prediction
        })
    end_time = time.perf_counter()
    
    for res in results:
        print(f"[{res['id']}] {res['desc']:35} -> Result: {res['predicted']}")
        
    print(f"Execution Time: {(end_time - start_time)*1000:.4f} ms")
    return results

if __name__ == "__main__":
    # Runs for Stephanie to validate implementation and compile comparison matrix
    for k in [1, 3, 5]:
        run_experiment(k_value=k, metric='euclidean')
        run_experiment(k_value=k, metric='manhattan')
