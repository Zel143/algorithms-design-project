"""
Data Loader for "The Geometry of AI Decisions"
Contains the training dataset and test points curated by Ranzel.
"""

# Training Dataset: Weight (g), Sweetness (1-10), Class
TRAINING_DATA = [
    {"id": "L1", "weight": 80,  "sweetness": 2.0, "class": "Lemon"},
    {"id": "L2", "weight": 95,  "sweetness": 2.5, "class": "Lemon"},
    {"id": "L3", "weight": 110, "sweetness": 3.0, "class": "Lemon"},
    {"id": "L4", "weight": 120, "sweetness": 4.0, "class": "Lemon"},
    {"id": "L5", "weight": 135, "sweetness": 3.5, "class": "Lemon"},
    {"id": "L6", "weight": 150, "sweetness": 4.5, "class": "Lemon"},
    {"id": "A1", "weight": 130, "sweetness": 6.0, "class": "Apple"},
    {"id": "A2", "weight": 145, "sweetness": 6.5, "class": "Apple"},
    {"id": "A3", "weight": 160, "sweetness": 7.0, "class": "Apple"},
    {"id": "A4", "weight": 175, "sweetness": 6.2, "class": "Apple"},
    {"id": "A5", "weight": 190, "sweetness": 7.5, "class": "Apple"},
    {"id": "A6", "weight": 205, "sweetness": 6.8, "class": "Apple"},
    {"id": "B1", "weight": 115, "sweetness": 8.0, "class": "Banana"},
    {"id": "B2", "weight": 130, "sweetness": 8.5, "class": "Banana"},
    {"id": "B3", "weight": 145, "sweetness": 9.0, "class": "Banana"},
    {"id": "B4", "weight": 160, "sweetness": 8.2, "class": "Banana"},
    {"id": "B5", "weight": 175, "sweetness": 9.3, "class": "Banana"},
    {"id": "B6", "weight": 190, "sweetness": 8.7, "class": "Banana"},
]

# Test Points: Weight (g), Sweetness (1-10), Description
TEST_POINTS = [
    {"id": "T1", "weight": 100, "sweetness": 2.8, "desc": "Normal lemon case"},
    {"id": "T2", "weight": 155, "sweetness": 6.8, "desc": "Normal apple case"},
    {"id": "T3", "weight": 150, "sweetness": 8.7, "desc": "Normal banana case"},
    {"id": "T4", "weight": 135, "sweetness": 5.2, "desc": "Lemon-Apple boundary"},
    {"id": "T5", "weight": 145, "sweetness": 7.6, "desc": "Apple-Banana boundary"},
    {"id": "T6", "weight": 122, "sweetness": 6.2, "desc": "Three-class mixed area"},
    {"id": "T7", "weight": 140, "sweetness": 4.0, "desc": "Metric sensitivity (Lemon/Apple)"},
    {"id": "T8", "weight": 160, "sweetness": 7.6, "desc": "Split-vote (Apple/Banana)"},
]

# Class Priority for Tie-Breaking
CLASS_PRIORITY = ["Apple", "Banana", "Lemon"]

def get_training_data():
    return TRAINING_DATA

def get_test_points():
    return TEST_POINTS

def get_priority():
    return CLASS_PRIORITY
