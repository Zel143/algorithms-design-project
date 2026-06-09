-----WORKLOAD ASSIGNMENT & DOCUMENTATION ROLES

[📌 GROUPMATES: Please write your name over the "ASSIGNEE NEEDED" placeholders below and flesh out your section immediately for submission today!]


1. RANZEL JUDE M. VIRTUCIO (Data Curator & Edge-Case Manager)
Proposal / Project Duty: Responsible for detailing the design of the 2D mock dataset. Defines the coordinate system for the data points and strategically maps out test cases near decision boundaries. Drafts the exact logical constraints and tie-breaking rules that handle equidistant points or split votes within the proposal.
2. JON LUIGI L. ARIOLA (Lead Algorithm Architect)
Proposal / Project Duty: Responsible for outlining the high-level framework of the primary k-NN classification loop. Drafts the structural flow chart or pseudocode showing how the algorithm accepts datasets, coordinates loops, and executes voting mechanics.
3. [DAVID SOLANO] (Mathematical Engineer)
Proposal / Project Duty: Responsible for documenting the low-level geometric math functions. Drafts the formal mathematical definitions for both the Euclidean and Manhattan distance formulas that will be implemented from scratch.
4. [STEPHANIE KEITH SISON] (Parameters & Testing Analyst)
Proposal / Project Duty: Responsible for creating the experimental testing matrix. Outlines the methodology for changing hyperparameter configurations (such as k=1 versus k=5) and defines how metric-based boundary shifts will be isolated and recorded.
5. MELPRIN O. CORREA (Complexity & Technical Reporter)
Proposal / Project Duty: Responsible for drafting the initial theoretical complexity analysis. Outlines how data scaling will impact execution speed based on the O(n * d) time and space bounds, establishing the formal baseline for the final technical report.
6. FIONA HAILEY L. MARAÑA (Documentation & Presentation Designer)
Proposal / Project Duty: Responsible for compiling, formatting, and proofreading the final proposal document. Standardizes the layout structure, ensures clear organization of team sections, and establishes the visual framework for submission.



-----STARTER HANDOFF GUIDE

Use this section to help each member begin their assigned work without waiting for the whole project to be finished.

1. RANZEL JUDE M. VIRTUCIO
Start with:
- Define the 2D dataset theme, such as fruit classification using Weight and Sweetness.
- Prepare at least 12-20 labeled training points.
- Prepare 5-8 test points, including points near class boundaries.
- List edge cases: tied neighbor votes, equal distances, duplicate points, invalid k, and out-of-range test points.

Expected output:
- Dataset table with columns: point id, x-value, y-value, class label.
- Test-case table with expected observations.
- Tie-breaking rule proposal.

Started output:
- See `ranzel_dataset_and_edge_cases.md` for the initial fruit dataset, boundary test points, edge cases, and deterministic tie-breaking rules.

Give to:
- Jon for algorithm flow.
- Stephanie for testing matrix.
- Fiona for documentation.

2. JON LUIGI L. ARIOLA
Start with:
- Draft the k-NN algorithm flow from input to prediction.
- Write pseudocode for distance calculation, neighbor sorting, selecting k nearest neighbors, voting, and returning the class.
- Identify where the metric toggle is used.

Expected output:
- Pseudocode or flowchart.
- Short explanation of each major algorithm step.
- List of functions needed in the source code.

Give to:
- David for formula integration.
- Melprin for complexity analysis.
- Fiona for report structure.

3. DAVID R. SOLANO
Start with:
- Write the Euclidean distance formula.
- Write the Manhattan distance formula.
- Add a short explanation of how the formulas differ geometrically.

Expected output:
- Formula section for the report.
- Example calculation using one training point and one test point.
- Notes for implementation accuracy.

Give to:
- Jon for source code.
- Stephanie for test comparison.
- Fiona for documentation.

4. STEPHANIE KEITH F. SISON
Start with:
- Choose k values to test, such as k=1, k=3, and k=5.
- Build a testing matrix comparing Euclidean vs. Manhattan predictions.
- Include normal cases, boundary cases, and tie cases.

Expected output:
- Testing table with columns: test point, k, metric, predicted class, notes.
- Short method for comparing boundary shifts.
- Initial list of sample outputs needed.

Give to:
- Melprin for runtime/complexity observations.
- Fiona for report and presentation.

5. MELPRIN O. CORREA
Start with:
- Analyze basic k-NN per-query complexity.
- Use n for number of training points and d for number of features.
- Note that distance computation is O(n * d), full sorting is O(n log n), and total per-query time is O(n * d + n log n).

Expected output:
- Time complexity section.
- Space complexity section.
- Short comparison between Euclidean and Manhattan cost.
- Note on possible optimization using partial selection instead of full sorting.

Give to:
- Fiona for report.
- Jon for implementation notes.

6. FIONA HAILEY L. MARANA
Start with:
- Create the report skeleton.
- Prepare sections for topic discussion, inputs, outputs, algorithm design, formulas, testing, complexity, results, and references.
- Standardize member names and formatting.

Expected output:
- Report outline.
- Presentation outline.
- Checklist of missing sections from each member.

Give to:
- Entire team for review.

-----FIRST TEAM CHECKPOINT

Before coding starts, collect these from the team:
- Dataset and edge cases from Ranzel.
- Pseudocode from Jon.
- Distance formulas from David.
- Testing matrix from Stephanie.
- Complexity baseline from Melprin.
- Report outline from Fiona.

After this checkpoint, the implementation can start with fewer blockers.
