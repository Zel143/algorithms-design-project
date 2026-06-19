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
    
    # Separate features and labels for plotting
    train_x = [p['weight'] for p in train_data]
    train_y = [p['sweetness'] for p in train_data]
    train_classes = [p['class'] for p in train_data]
    
    # Map classes to integers for coloring
    class_map = {cls: idx for idx, cls in enumerate(priority)}
    train_colors_idx = [class_map[c] for c in train_classes]
    
    # 2. Setup Classifiers
    knn_euc = KNNClassifier(k=k_value, metric='euclidean', priority=priority)
    knn_euc.fit(train_data)
    
    knn_man = KNNClassifier(k=k_value, metric='manhattan', priority=priority)
    knn_man.fit(train_data)
    
    # 3. Create Grid for Decision Boundary
    # We expand slightly beyond the min/max of our training features
    x_min, x_max = 70, 220
    y_min, y_max = 1.0, 10.0
    
    # Grid resolution (higher resolution = smoother boundaries)
    grid_res = 150
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, grid_res),
                         np.linspace(y_min, y_max, grid_res))
    
    # Prepare grid points for batch prediction
    grid_points = []
    for x, y in zip(xx.ravel(), yy.ravel()):
        grid_points.append({"weight": float(x), "sweetness": float(y)})
        
    # 4. Compute predictions on the grid
    t0 = time.perf_counter()
    pred_euc_labels = [knn_euc.predict(p) for p in grid_points]
    t1 = time.perf_counter()
    pred_man_labels = [knn_man.predict(p) for p in grid_points]
    t2 = time.perf_counter()
    
    print(f"Euclidean grid prediction: {(t1 - t0)*1000:.2f} ms")
    print(f"Manhattan grid prediction: {(t2 - t1)*1000:.2f} ms")
    
    # Map predictions back to indices for plotting
    zz_euc = np.array([class_map[l] for l in pred_euc_labels]).reshape(xx.shape)
    zz_man = np.array([class_map[l] for l in pred_man_labels]).reshape(xx.shape)
    
    # 5. Define Colormaps
    # Priority order is ["Apple", "Banana", "Lemon"]
    # Apple = Red/Pink, Banana = Gold/Yellow-Orange, Lemon = Pale Green/Yellow
    bg_colors = ['#FFCDD2', '#FFE082', '#FFF59D'] # Light Red, Light Gold, Light Yellow
    fg_colors = ['#D32F2F', '#F57C00', '#FBC02D'] # Dark Red, Dark Orange, Dark Yellow
    markers = ['^', 's', 'o'] # Apple, Banana, Lemon
    
    cmap_light = ListedColormap(bg_colors)
    
    # 6. Plotting
    fig, axes = plt.subplots(1, 2, figsize=(15, 7), sharey=True)
    
    metrics = [('Euclidean Distance', zz_euc, knn_euc, axes[0]),
               ('Manhattan Distance', zz_man, knn_man, axes[1])]
    
    for title, zz, model, ax in metrics:
        # Plot decision boundaries
        ax.pcolormesh(xx, yy, zz, cmap=cmap_light, shading='auto', alpha=0.6)
        
        # Plot training dataset points
        for cls_name, color, marker in zip(priority, fg_colors, markers):
            indices = [i for i, c in enumerate(train_classes) if c == cls_name]
            ax.scatter(np.array(train_x)[indices], np.array(train_y)[indices],
                       c=color, marker=marker, edgecolor='k', s=80, label=f"Training: {cls_name}")
            
        # Plot and label test points
        test_x = []
        test_y = []
        test_predictions = []
        for tp in test_points:
            pred = model.predict(tp)
            test_x.append(tp['weight'])
            test_y.append(tp['sweetness'])
            test_predictions.append(pred)
            # Label test point
            ax.annotate(f"{tp['id']}({pred[0]})", (tp['weight'], tp['sweetness']),
                        textcoords="offset points", xytext=(0,10), ha='center',
                        fontsize=8, weight='bold', bbox=dict(boxstyle="round,pad=0.2", fc="white", alpha=0.8, ec="gray"))
            
        # Scatter plot test points
        ax.scatter(test_x, test_y, c='black', marker='X', s=120, edgecolor='white', linewidth=1.5, label='Test Points (T1-T8)')
        
        ax.set_title(f"{title} (k={k_value})", fontsize=14, weight='bold')
        ax.set_xlabel('Weight (grams)', fontsize=12)
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.grid(True, linestyle='--', alpha=0.3)
        
    axes[0].set_ylabel('Sweetness (1-10)', fontsize=12)
    
    # Place a single legend outside
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 0.96), ncol=4, fontsize=11)
    
    plt.tight_layout(rect=[0, 0, 1, 0.90])
    
    # Save image
    output_filename = f"decision_boundaries_k{k_value}.png"
    output_path = os.path.join(os.path.dirname(__file__), output_filename)
    plt.savefig(output_path, dpi=150)
    plt.close()
    
    print(f"Visualization successfully saved to: {output_path}")

def run_predictions_printout(k_value):
    train_data = get_training_data()
    test_points = get_test_points()
    priority = get_priority()
    
    knn_euc = KNNClassifier(k=k_value, metric='euclidean', priority=priority)
    knn_euc.fit(train_data)
    
    knn_man = KNNClassifier(k=k_value, metric='manhattan', priority=priority)
    knn_man.fit(train_data)
    
    print(f"\n=============================================")
    print(f"   PREDICTIONS COMPARISON TABLE FOR k={k_value}")
    print(f"=============================================")
    print(f"{'ID':4} | {'Description':30} | {'Euclidean':10} | {'Manhattan':10} | {'Match?'}")
    print("-" * 75)
    
    for tp in test_points:
        p_euc = knn_euc.predict(tp)
        p_man = knn_man.predict(tp)
        match = "Yes" if p_euc == p_man else "NO (Metric Disagreement!)"
        print(f"{tp['id']:4} | {tp['desc']:30} | {p_euc:10} | {p_man:10} | {match}")
    print("=" * 75)

if __name__ == "__main__":
    k_val = 3
    if len(sys.argv) > 1:
        try:
            k_val = int(sys.argv[1])
        except ValueError:
            print("Invalid k value specified, using default k=3.")
            
    run_predictions_printout(k_val)
    plot_boundaries(k_val)
