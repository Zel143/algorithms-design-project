"""
Main Entry Point with Visualization for "The Geometry of AI Decisions"
Trains Euclidean and Manhattan k-NN classifiers and plots their decision boundaries.
"""

import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from knn_engine import KNNClassifier
from data_loader import get_training_data, get_test_points, get_priority

def plot_boundaries(k_value):
    print(f"Generating decision boundary plot for k={k_value}...")
    
    # 1. Load Data
    train_data = get_training_data()
    test_points = get_test_points()
    priority = get_priority()
    
    # TODO: Fiona - Implement Matplotlib logic here!
    # 1. Setup Classifiers (Euclidean and Manhattan)
    # 2. Create Grid for Decision Boundary (e.g., using np.meshgrid)
    # 3. Compute predictions on the grid
    # 4. Define Colormaps mapping to the priority classes
    # 5. Plot the decision boundaries using pcolormesh
    # 6. Scatter plot the training data and the test points
    # 7. Save the image as decision_boundaries_k{k_value}.png
    
    print(f"TODO: Fiona needs to add the plotting logic to save decision_boundaries_k{k_value}.png")

def run_predictions_printout(k_value):
    # TODO: Fiona - Call the classifiers and print out a comparison table
    # so we can clearly see the predictions for both Euclidean and Manhattan.
    print(f"TODO: Fiona needs to print the prediction comparison table for k={k_value}")

if __name__ == "__main__":
    k_val = 3
    if len(sys.argv) > 1:
        try:
            k_val = int(sys.argv[1])
        except ValueError:
            print("Invalid k value specified, using default k=3.")
            
    run_predictions_printout(k_val)
    plot_boundaries(k_val)

