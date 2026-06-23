from knn_engine import KNNClassifier
from data_loader import get_training_data, get_test_points, get_priority
import time

def run_experiment(k_value, metric):
    print(f"\n--- Experiment: k={k_value}, Metric={metric} ---")
    
    train_data = get_training_data()
    test_points = get_test_points()
    priority = get_priority()
    
    # TODO: Stephanie - Implement the testing harness here!
    # 1. Initialize the KNNClassifier with the given k_value and metric
    # 2. Fit the train_data
    # 3. Start a timer (time.perf_counter)
    # 4. Loop through test_points and generate predictions
    # 5. Stop the timer and print the total execution time
    # 6. Print the predictions for each test point (T1-T8)
    
    print("TODO: Stephanie needs to write the prediction loop and execution time logging.")
    
    return []

if __name__ == "__main__":
    # Runs for Stephanie to validate implementation and compile comparison matrix
    for k in [1, 3, 5]:
        run_experiment(k_value=k, metric='euclidean')
        run_experiment(k_value=k, metric='manhattan')
