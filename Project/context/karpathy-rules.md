# Karpathy Rules Setup

Source: Algorithms_Design_Project_Handout - Tagged.pdf

## Purpose

Use this file as the working rules for the Algorithms and Design Project.

## Core Rules

- Define the problem clearly before coding.
- Identify inputs and outputs explicitly.
- Choose and state the algorithm design technique used.
- Provide pseudocode or a flowchart before implementation.
- Write clean, well-documented code in any programming language.
- Analyze both time and space complexity.
- Compare the chosen approach with at least one alternative.
- Include test cases, edge cases, and sample results.
- Ensure the solution is original.
- Cite references properly using ACM style.

## Required Deliverables

- Written report
- Source code
- Recorded presentation
- Sample inputs and outputs

## Suggested Project Workflow

1. Select a problem from the topic list or propose a similar one.
2. Describe the problem, inputs, outputs, and constraints.
3. Design the algorithm and explain the technique.
4. Implement the solution with readable code and comments where needed.
5. Test normal cases, edge cases, and failure cases.
6. Measure complexity and compare against alternatives.
7. Prepare the report, code, samples, and recorded presentation.

## Evaluation Priorities

- Problem complexity: 20%
- Algorithm design: 25%
- Implementation: 20%
- Analysis: 15%
- Documentation: 10%
- Creativity: 10%

## Topic Areas

- Sorting and searching
- Graph algorithms
- Dynamic programming
- Greedy algorithms
- Backtracking
- Real-world applications such as routing, scheduling, and traffic simulation

## Submission Rules

- Submit before the deadline.
- Follow all formatting instructions.
- Keep references and citations complete.
- Preserve originality throughout the report and code.

---

## Selected Topic (Active)

**Problem:** The Geometry of AI Decisions - comparing how Euclidean and Manhattan distance metrics affect k-Nearest Neighbors classifications and decision boundaries.

**Algorithm Technique:** k-Nearest Neighbors from scratch using distance-based search/classification.

**Inputs:**
- Custom non-linearly separable 2D dataset with labeled points
- Test coordinates positioned on or near decision boundaries
- Configurable k value
- Distance metric toggle: Euclidean or Manhattan

**Outputs:**
- Predicted class for each test point
- 2D scatter plot showing dataset points, test points, and decision boundaries
- Comparative analysis of classification changes, boundary sensitivity, error rates, and execution profiles across metrics and k values

**Complexity:**
- Per query distance computation: O(n), where n is the number of training points
- Neighbor selection by full sorting: O(n log n); may be optimized later with partial selection
- Space: O(n) for computed distances and neighbor records

**Proposal File:** `Algorithms_and_Complexity_Proposal.md`

**Status:** Proposal submitted on 2026-06-09. Implementation, sample outputs, report, and recorded presentation remain as follow-up deliverables.
