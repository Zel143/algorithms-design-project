# ALGORITHMS AND COMPLEXITY

## PROJECT PROPOSAL: THE GEOMETRY OF AI DECISIONS

**Presented By Group 3 - BM2:**
- Jon Luigi L. Ariola
- Melprin O. Correa
- Fiona Hailey L. Maraña
- Stephanie Keith F. Sison
- David R. Solano
- Ranzel Jude M. Virtucio

**Presented To:**
- Mr. Joel De Goma

---

## BRIEF DISCUSSION ABOUT TOPIC

The core of this project is to implement a k-Nearest Neighbors (k-NN) machine learning classifier from scratch, entirely avoiding external libraries like Scikit-Learn [cite: 8]. The k-NN algorithm, originally introduced by Cover and Hart, relies on spatial geometry, classifying an unknown data point based on the majority vote of its closest neighbors in a vector space [cite: 9, 24].

Our research focuses on how altering the fundamental geometric formulas used to calculate distance, specifically contrasting Euclidean Distance against Manhattan Distance, shifts the algorithm's boundary decisions, judgment, and overall accuracy [cite: 10]. Euclidean distance measures the straight-line distance ("as the crow flies"), while Manhattan distance measures distance along axes at right angles ("taxi driving through city blocks") [cite: 11, 26]. 

We will evaluate the execution dynamics and mathematical tradeoffs of these metrics across a custom 2D dataset, analyzing the algorithm's time complexity and addressing architectural edge cases such as exact equidistant ties or split votes [cite: 12, 27].

---

## INPUT AND OUTCOME OF PROPOSAL

### Inputs
* A custom-curated, non-linearly separable 2D mock dataset featuring items classified by two distinct numerical features, such as Weight vs. Sweetness to classify a fruit category [cite: 15].
* Coordinate arrays representing strategic test data points positioned directly on or near the decision boundary lines [cite: 16].
* Configurable hyperparameter variables, specifically the value of k (number of neighbors) and the selection toggle for the distance metric formula (Euclidean vs. Manhattan) [cite: 17, 29].

### Outcomes
* A functional, zero-dependency 2D k-NN classification engine built completely from scratch [cite: 20].
* A visual 2D scatter plot mapping the dataset coordinates, decision boundaries, and test point classifications [cite: 21, 25].
* A comparative empirical analysis documenting shifting classification results, boundary sensitivity, error rates, and algorithmic execution profiles when swapping geometric metrics across varying k values [cite: 22, 26].

---

## REFERENCES

1. Cover, T. and Hart, P. 1967. Nearest neighbor pattern classification. *IEEE Transactions on Information Theory*, 13(1), 21-27 [cite: 24].
2. Altman, N. S. 1992. An introduction to kernel and nearest-neighbor nonparametric regression. *The American Statistician*, 46(3), 175-185 [cite: 25].
3. Wilson, D. R. and Martinez, T. R. 1997. Improved heterogeneous distance functions. *Journal of Artificial Intelligence Research*, 6, 1-34 [cite: 26].
4. Beyer, K., Goldstein, J., Ramakrishnan, R., and Shaft, U. 1999. When is "nearest neighbor" meaningful? In *Proceedings of the 7th International Conference on Database Theory (ICDT '99)*, 217-235 [cite: 27, 28].
5. Bishop, C. M. 2006. *Pattern Recognition and Machine Learning*. Springer-Verlag [cite: 29].
