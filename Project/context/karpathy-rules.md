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

**Problem:** Task Scheduling with Deadlines and Profits

**Algorithm Technique:** Greedy (sort by profit descending, fill latest valid slot)

**Inputs:**
- List of tasks, each with an id, a deadline, and a profit
- (Implicit) number of time slots = maximum deadline across all tasks

**Outputs:**
- Selected tasks and their assigned time slots
- Skipped tasks (no valid slot available)
- Total profit of scheduled tasks

**Complexity:**
- Sorting: O(n log n)
- Slot placement: O(n * d), where d is the maximum deadline
- Overall: O(n log n + n * d), simplifies to O(n^2) when d is bounded by n
- Space: O(d) for the slot array

**Project Folder:** `task scheduling project/`

**Status:** Proposal submitted. Code implemented and verified. Report drafted.
