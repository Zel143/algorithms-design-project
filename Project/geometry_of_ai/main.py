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
    
    knn_euc = KNNClassifier(k=k_value, metric='euclidean', priority=priority)
    knn_euc.fit(train_data)
    
    knn_man = KNNClassifier(k=k_value, metric='manhattan', priority=priority)
    knn_man.fit(train_data)
    
    # Map classes to integers
    class_map = {'Lemon': 0, 'Apple': 1, 'Banana': 2}
    colors = ['yellow', 'red', 'green']
    cmap_light = ListedColormap(['#FFFF99', '#FF9999', '#99FF99'])
    
    # Grid
    x_min, x_max = 60, 220
    y_min, y_max = 1, 10.1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 2), np.arange(y_min, y_max, 0.2))
    
    grid_points = [{'weight': x, 'sweetness': y} for x, y in zip(xx.ravel(), yy.ravel())]
    
    Z_euc = np.array([class_map[knn_euc.predict(p)] for p in grid_points])
    Z_euc = Z_euc.reshape(xx.shape)
    
    Z_man = np.array([class_map[knn_man.predict(p)] for p in grid_points])
    Z_man = Z_man.reshape(xx.shape)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    ax1.pcolormesh(xx, yy, Z_euc, cmap=cmap_light, shading='auto')
    ax1.set_title(f'Euclidean Distance Decision Boundary (k={k_value})')
    
    ax2.pcolormesh(xx, yy, Z_man, cmap=cmap_light, shading='auto')
    ax2.set_title(f'Manhattan Distance Decision Boundary (k={k_value})')
    
    for ax in (ax1, ax2):
        for p in train_data:
            ax.scatter(p['weight'], p['sweetness'], c=colors[class_map[p['class']]], edgecolors='k', marker='o', s=50)
        for p in test_points:
            ax.scatter(p['weight'], p['sweetness'], c='white', edgecolors='k', marker='^', s=100)
        ax.set_xlabel('Weight (g)')
        ax.set_ylabel('Sweetness (1-10)')
        
    plt.savefig(f'decision_boundaries_k{k_value}.png')
    print(f"Saved plot to decision_boundaries_k{k_value}.png")

def run_predictions_printout(k_value):
    train_data = get_training_data()
    test_points = get_test_points()
    priority = get_priority()

    knn_euc = KNNClassifier(k=k_value, metric='euclidean', priority=priority)
    knn_euc.fit(train_data)
    
    knn_man = KNNClassifier(k=k_value, metric='manhattan', priority=priority)
    knn_man.fit(train_data)
    
    print(f"\nPrediction Comparison Table for k={k_value}")
    print(f"{'Test ID':<10} | {'Euclidean':<15} | {'Manhattan':<15} | {'Match?':<10}")
    print("-" * 55)
    for p in test_points:
        pred_euc = knn_euc.predict(p)
        pred_man = knn_man.predict(p)
        match = "Yes" if pred_euc == pred_man else "No"
        print(f"{p['id']:<10} | {pred_euc:<15} | {pred_man:<15} | {match:<10}")
    print("\n")

if __name__ == "__main__":
    k_val = 3
    if len(sys.argv) > 1:
        try:
            k_val = int(sys.argv[1])
        except ValueError:
            print("Invalid k value specified, using default k=3.")
            
    run_predictions_printout(k_val)
    plot_boundaries(k_val)

