# Filled Topic Review

Source workbook: CSS131-1_BM2 Alternating-Week-Instructional-Plan.xlsx

Use this file as the filled version of [topic-review-template.md](topic-review-template.md) for the topics listed in the workbook.

## Week 4 - BRUTE FORCE

### Topic
- Name: BRUTE FORCE
- Category: Algorithm design technique
- Prerequisites: Problem definition, candidate generation, basic complexity counting

### Problem Statement
- Input: A problem with a finite candidate space
- Output: A valid or best candidate solution
- Constraints: Search space may grow quickly, so this is usually a baseline approach

### Core Idea
- Enumerate every possible candidate solution and test each one directly.

### Algorithm
1. Generate a candidate.
2. Test whether it satisfies the constraints or objective.
3. Keep the first valid solution or the best one found so far.

### Correctness
- Invariant: every candidate is treated by the same rule.
- Why it works: if a solution exists in a finite search space, exhaustive enumeration will eventually reach it.
- Termination: the search stops when the candidate space is exhausted or a target candidate is found.

### Complexity
- Time: $O(N \cdot C)$ where $N$ is the number of candidates and $C$ is the cost of testing one candidate.
- Space: typically $O(1)$ unless candidate generation stores extra state.
- Bottleneck: the size of the candidate space.

### Edge Cases
- Empty input.
- No valid solution.
- Multiple valid solutions.

### Review Notes
- Source row: Week 4, Meeting 1, ASYNC, Video Lecture, Individual

## Week 4 - RECURSIVE AND NON-RECURSIVE ALGORITHM

### Topic
- Name: RECURSIVE AND NON-RECURSIVE ALGORITHM
- Category: Problem-solving styles
- Prerequisites: Function calls, loop control, base cases, stack behavior

### Problem Statement
- Input: A computational problem that can be expressed recursively or iteratively
- Output: A correct solution using either self-referential calls or loops
- Constraints: Recursive solutions must define a base case; iterative solutions must manage state explicitly

### Core Idea
- Recursive version: solve a smaller instance and combine the result.
- Non-recursive version: use loops and explicit state updates instead of self-calls.

### Algorithm
1. Identify the base case or stopping condition.
2. Define how the problem reduces to a smaller instance.
3. Implement either a recursive call or an equivalent loop-based process.

### Correctness
- Invariant: each step preserves the problem state needed to reach the final answer.
- Why it works: recursion mirrors the mathematical structure of the problem; iteration reproduces the same state transitions without call-stack dependence.
- Termination: the base case or loop condition guarantees progress toward completion.

### Complexity
- Time: depends on the recurrence or loop structure; often $O(n)$ for linear processes.
- Space: recursion uses call stack space, while iteration often uses $O(1)$ extra space.
- Bottleneck: recursion depth or repeated subproblem work.

### Edge Cases
- Base case omitted or wrong.
- Deep recursion causing stack overflow.
- Mismatched recursive and iterative states.

### Review Notes
- Source rows: Week 4, Meeting 2 and 3, ASYNC/SYNC

## Week 5 - Module 1 Summary

### Topic
- Name: Module 1 Summary
- Category: Review / consolidation
- Prerequisites: Brute force, recursion, iteration

### Problem Statement
- Input: The topics from Module 1
- Output: A consolidated understanding of the main concepts
- Constraints: Focus on recall, comparison, and explanation rather than new techniques

### Core Idea
- Revisit the key ideas from the first module and connect them into one mental model.

### Algorithm
1. Review each topic definition.
2. Compare the strengths and weaknesses of each approach.
3. Restate the main correctness and complexity ideas in your own words.

### Correctness
- Invariant: the summary should preserve the meaning of the original topics without adding unsupported claims.
- Why it works: retrieval plus comparison strengthens retention and reveals gaps.
- Termination: the review ends when each topic can be explained clearly.

### Complexity
- Time: depends on the number of topics being reviewed.
- Space: minimal, unless notes are expanded.
- Bottleneck: weak recall of earlier definitions.

### Edge Cases
- Confusing similar terms.
- Mixing up recursion and iteration.
- Missing the distinction between idea and implementation.

### Review Notes
- Source row: Week 5, Meeting 1, F2F, Discussion and Seatwork, Individual

## Week 5 - CO1 Module 1 Quiz

### Topic
- Name: CO1 Module 1 Quiz
- Category: Assessment
- Prerequisites: Module 1 concepts

### Problem Statement
- Input: Questions covering Module 1
- Output: Demonstrated mastery of CO1
- Constraints: Answers should be concise, correct, and justified when needed

### Core Idea
- Use recall, reasoning, and problem solving to show understanding of the module.

### Algorithm
1. Read each item carefully.
2. Identify the relevant concept.
3. Answer directly and check for justification requirements.

### Correctness
- Invariant: each response should match the concept being assessed.
- Why it works: correct answers follow from the definitions, examples, or procedures learned in Module 1.
- Termination: complete all questions within the exam time.

### Complexity
- Time: bounded by quiz duration.
- Space: minimal.
- Bottleneck: time pressure.

### Edge Cases
- Ambiguous wording.
- Similar-looking answer choices.
- Partial recall of a definition.

### Review Notes
- Source row: Week 5, Meeting 2, F2F, Summative written exam, Individual

## Week 5 - Discuss Module 1 Quiz

### Topic
- Name: Discuss Module 1 Quiz
- Category: Post-assessment review
- Prerequisites: Quiz solutions and module concepts

### Problem Statement
- Input: Quiz questions and answers
- Output: Explanation of why the chosen answers are right or wrong
- Constraints: Focus on justification, not only final answers

### Core Idea
- Review mistakes and correct them by tracing the supporting concept.

### Algorithm
1. Revisit each missed or uncertain item.
2. Identify the exact concept behind the answer.
3. Explain the reasoning step by step.

### Correctness
- Invariant: each explanation must be grounded in the original lesson material.
- Why it works: error review converts mistakes into durable knowledge.
- Termination: every important quiz item is explained.

### Complexity
- Time: proportional to the number of questions discussed.
- Space: minimal.
- Bottleneck: unclear reasoning from the quiz.

### Edge Cases
- Correct answer with weak reasoning.
- Multiple plausible but incorrect choices.

### Review Notes
- Source row: Week 5, Meeting 3, F2F, Discussion of Module 1 Quiz, Individual

## Week 6 - DECREASE-AND-CONQUER

### Topic
- Name: DECREASE-AND-CONQUER
- Category: Algorithm design technique
- Prerequisites: Recurrence, problem size reduction, base cases

### Problem Statement
- Input: A problem that can be reduced to a smaller instance of itself
- Output: A correct solution built from the smaller instance
- Constraints: Each step must strictly reduce the problem size

### Core Idea
- Solve a smaller version of the same problem, then extend the result to the original instance.

### Algorithm
1. Reduce the problem size by one or by a fixed factor.
2. Solve the smaller problem.
3. Reconstruct the full answer from the smaller solution.

### Correctness
- Invariant: the reduced problem remains equivalent to the original objective.
- Why it works: repeated reduction eventually reaches a base case.
- Termination: size strictly decreases, so the process cannot continue forever.

### Complexity
- Time: often expressed with a recurrence such as $T(n) = T(n-1) + f(n)$.
- Space: depends on recursion depth and whether the method is recursive or iterative.
- Bottleneck: the cost of repeated reductions and reconstructions.

### Edge Cases
- Reduction fails to shrink the input.
- Base case is not defined.
- Reconstruction step changes the answer incorrectly.

### Review Notes
- Source rows: Week 6, Meetings 1-3, ASYNC/SYNC, Video Lecture / Summary Discussion and Seatwork

## Week 7 - DIVIDE-AND-CONQUER

### Topic
- Name: DIVIDE-AND-CONQUER
- Category: Algorithm design technique
- Prerequisites: Recursion, splitting, combining results

### Problem Statement
- Input: A problem that can be split into smaller subproblems
- Output: A solution formed by combining subproblem results
- Constraints: Subproblems must be easier than the original problem

### Core Idea
- Divide the problem, solve each part recursively, and combine the partial solutions.

### Algorithm
1. Split the instance into smaller subproblems.
2. Solve each subproblem recursively.
3. Combine the sub-results into the final answer.

### Correctness
- Invariant: each subproblem represents a valid decomposition of the original problem.
- Why it works: if the subproblems are solved correctly and the combine step is correct, the overall answer is correct.
- Termination: recursive splitting eventually reaches base cases.

### Complexity
- Time: often modeled by recurrences such as $T(n) = aT(n/b) + f(n)$.
- Space: recursion stack plus any combine-step storage.
- Bottleneck: the combine step or excessive subproblem overlap.

### Edge Cases
- Uneven splits.
- Base case too large or too small.
- Combine step double-counts or omits values.

### Review Notes
- Source rows: Week 7, Meetings 1-3, F2F, Discussion / Summary Discussion and Seatwork

## Week 8 - AVL TREE - HEAP

### Topic
- Name: AVL TREE - HEAP
- Category: Data structures
- Prerequisites: Search trees, balancing, priority queues

### Problem Statement
- Input: Keys or priorities that need efficient organization
- Output: Fast search, insertion, deletion, or priority access depending on the structure
- Constraints: AVL trees must stay balanced; heaps must preserve heap order

### Core Idea
- AVL trees maintain near-balanced height for fast ordered operations.
- Heaps support quick access to the minimum or maximum element.

### Algorithm
1. Insert or remove elements while preserving the structural invariant.
2. Rebalance an AVL tree with rotations when needed.
3. Restore heap order by bubbling up or down after updates.

### Correctness
- Invariant: AVL height balance or heap-order property is preserved after each update.
- Why it works: local repairs restore the global property.
- Termination: rotations and swaps are finite and reduce the violation.

### Complexity
- Time: AVL operations are typically $O(\log n)$; heap insert and delete are typically $O(\log n)$, and peek is $O(1)$.
- Space: $O(n)$ to store the structure.
- Bottleneck: rebalancing after updates.

### Edge Cases
- Duplicate keys.
- Empty tree or heap.
- Repeated insertions causing imbalance.

### Review Notes
- Source row: Week 8, Meeting 1, ASYNC, Video Lecture, Individual

## Week 8 - Simple Linear Regression

### Topic
- Name: Simple Linear Regression
- Category: Statistical modeling
- Prerequisites: Scatter plots, least squares, line interpretation

### Problem Statement
- Input: Paired numerical data points
- Output: A best-fit line relating the variables
- Constraints: The model is simple and assumes a linear relationship

### Core Idea
- Fit a line that minimizes the squared error between predicted and observed values.

### Algorithm
1. Plot the data as a scatter diagram.
2. Estimate the line parameters with the least-squares criterion.
3. Use the line to describe the relationship and make predictions.

### Correctness
- Invariant: the chosen line minimizes squared residual error among candidate lines.
- Why it works: least squares gives the line that best fits the data under that objective.
- Termination: parameter estimation completes after solving the formula or optimization.

### Complexity
- Time: typically $O(n)$ once the summary statistics are computed.
- Space: $O(1)$ or $O(n)$ depending on how data are stored.
- Bottleneck: collecting clean data and interpreting the fit.

### Edge Cases
- Nonlinear data.
- Outliers.
- Very small sample size.

### Review Notes
- Source row: Week 8, Meeting 2, ASYNC, Video Lecture, Individual

## Week 8 - Summary

### Topic
- Name: Summary
- Category: Review / consolidation
- Prerequisites: AVL trees, heaps, and regression basics

### Problem Statement
- Input: The concepts covered during the week
- Output: A consolidated understanding of the week’s material
- Constraints: Focus on the key idea of each topic, not every detail

### Core Idea
- Reinforce the major concepts and check that the terminology is clear.

### Algorithm
1. Restate the main idea of each topic.
2. Compare data-structure ideas with the regression concept.
3. Identify any confusion and close the gaps.

### Correctness
- Invariant: each summary point should remain faithful to the source topic.
- Why it works: review strengthens recall and makes later problem solving easier.
- Termination: the week’s concepts are explainable without notes.

### Complexity
- Time: proportional to the number of ideas reviewed.
- Space: minimal.
- Bottleneck: mixing unrelated topics.

### Edge Cases
- Overgeneralizing a concept.
- Forgetting one topic entirely.

### Review Notes
- Source row: Week 8, Meeting 3, SYNC, Summary Discussion and Seatwork, Individual

## Week 9 - Module 2 Summary

### Topic
- Name: Module 2 Summary
- Category: Review / consolidation
- Prerequisites: Decrease-and-conquer, divide-and-conquer, AVL trees, heaps, regression, and related ideas

### Problem Statement
- Input: The topics from Module 2
- Output: A clear integrated summary of the module
- Constraints: Keep the focus on important ideas and comparative understanding

### Core Idea
- Revisit the module as a whole and connect the methods, structures, and examples.

### Algorithm
1. Review each concept in the module.
2. Compare how the techniques differ.
3. State the most important takeaways in one coherent summary.

### Correctness
- Invariant: the summary should not distort the underlying topic definitions.
- Why it works: consolidation exposes gaps and improves recall.
- Termination: the summary is complete when each topic can be explained simply.

### Complexity
- Time: proportional to the number of topics reviewed.
- Space: minimal.
- Bottleneck: confusing similar techniques.

### Edge Cases
- Reusing the wrong recurrence idea.
- Mixing up tree properties and heap properties.

### Review Notes
- Source row: Week 9, Meeting 1, F2F, Discussion and Seatwork, Individual

## Week 9 - CO2 Module 2 Quiz

### Topic
- Name: CO2 Module 2 Quiz
- Category: Assessment
- Prerequisites: Module 2 concepts

### Problem Statement
- Input: Questions on Module 2 material
- Output: Demonstrated mastery of CO2
- Constraints: Accuracy and speed both matter

### Core Idea
- Show that the concepts from Module 2 can be recalled and applied under exam conditions.

### Algorithm
1. Read the question carefully.
2. Match it to the correct topic or technique.
3. Answer and verify the reasoning if required.

### Correctness
- Invariant: the answer should reflect the current concept being tested.
- Why it works: correct responses come from understood definitions and procedures.
- Termination: complete the exam within the allotted time.

### Complexity
- Time: bounded by quiz duration.
- Space: minimal.
- Bottleneck: distinguishing closely related techniques.

### Edge Cases
- Distractor choices that sound technically correct.
- Questions involving multiple concepts.

### Review Notes
- Source row: Week 9, Meeting 2, F2F, Summative written exam, Individual

## Week 9 - Discuss Module 2 Quiz

### Topic
- Name: Discuss Module 2 Quiz
- Category: Post-assessment review
- Prerequisites: Quiz answers and module topics

### Problem Statement
- Input: Quiz items and solutions
- Output: A clear explanation of the correct reasoning
- Constraints: Discussion should focus on evidence and logic

### Core Idea
- Turn quiz results into a deeper understanding of the module.

### Algorithm
1. Review each problematic item.
2. Explain the supporting concept.
3. Correct any mistaken reasoning.

### Correctness
- Invariant: the explanation must be grounded in the module content.
- Why it works: discussing errors helps solidify the right mental model.
- Termination: every important item has been resolved.

### Complexity
- Time: proportional to the number of questions discussed.
- Space: minimal.
- Bottleneck: unclear justification.

### Edge Cases
- The answer is right but the reasoning is weak.
- Multiple concepts are tested at once.

### Review Notes
- Source row: Week 9, Meeting 3, F2F, Discussion of Module 2 Quiz, Individual

## Week 10 - GREEDY TECHNIQUE

### Topic
- Name: GREEDY TECHNIQUE
- Category: Algorithm design technique
- Prerequisites: Optimization problems, local choices, correctness arguments

### Problem Statement
- Input: An optimization problem with a sequence of decisions
- Output: A good or optimal solution built from locally chosen steps
- Constraints: Greedy choice must be justified; local optimality does not always imply global optimality

### Core Idea
- Make the best local choice available at each step and trust the structure of the problem to preserve global optimality.

### Algorithm
1. Choose the locally best available option.
2. Update the remaining problem.
3. Repeat until the solution is complete.

### Correctness
- Invariant: the partial solution remains extendable to an optimal solution.
- Why it works: the problem must satisfy a greedy-choice property and optimal substructure.
- Termination: the problem size shrinks after each choice.

### Complexity
- Time: often efficient, commonly $O(n \log n)$ or better depending on the data structure.
- Space: depends on whether extra ordering structures are needed.
- Bottleneck: sorting or priority management.

### Edge Cases
- Greedy choice is not globally optimal.
- Ties between candidate choices.
- Missing proof of optimality.

### Review Notes
- Source rows: Week 10, Meetings 1-3, ASYNC/SYNC, Video Lecture / Summary Discussion and Seatwork

## Week 11-13 - PROJECT

### Topic
- Name: PROJECT
- Category: Applied problem solving
- Prerequisites: Algorithm design strategies, implementation, and evaluation

### Problem Statement
- Input: A computational problem chosen for the project
- Output: A working solution and supporting documentation
- Constraints: Must show design choices, implementation, and evaluation clearly

### Core Idea
- Apply the algorithmic techniques from the course to a larger problem and justify the solution.

### Algorithm
1. Define the project scope.
2. Choose appropriate algorithm design strategies.
3. Implement, test, and refine the solution.

### Correctness
- Invariant: the implementation should match the stated design.
- Why it works: the solution is validated by testing, explanation, and consultation.
- Termination: the project is complete when the solution and documentation are ready.

### Complexity
- Time: depends on the chosen project problem and implementation.
- Space: depends on the chosen data structures.
- Bottleneck: integration and debugging.

### Edge Cases
- Unclear problem scope.
- Missing evaluation criteria.
- Implementation does not match the proposal.

### Review Notes
- Source rows: Week 11-12, ASYNC/SYNC, proposal, feedback, development, and consultation

## Week 13 - PROJECT SUBMISSION / PROJECT PRESENTATION

### Topic
- Name: PROJECT SUBMISSION / PROJECT PRESENTATION
- Category: Deliverable and defense
- Prerequisites: Completed project and written explanation

### Problem Statement
- Input: Final project solution and report
- Output: Submitted report and oral presentation
- Constraints: The explanation must be clear, defensible, and complete

### Core Idea
- Present the final work, explain the decisions, and justify the algorithmic choices.

### Algorithm
1. Prepare the written report.
2. Present the solution and its rationale.
3. Answer questions about correctness and efficiency.

### Correctness
- Invariant: the report and presentation should agree with the implemented solution.
- Why it works: a clear defense shows that the solution was understood, not just built.
- Termination: submission and presentation are completed.

### Complexity
- Time: limited by presentation and review time.
- Space: minimal.
- Bottleneck: explaining tradeoffs clearly.

### Edge Cases
- Missing evidence in the report.
- Inconsistent explanation during presentation.

### Review Notes
- Source rows: Week 13, Meetings 1-3, F2F, written report and presentation

## Week 14 - Administrative Items

### Topic
- Name: Verification of Grades / Remedial Exam / Check Final Grade in BB
- Category: Course administration
- Prerequisites: Final course records

### Problem Statement
- Input: Final grade records and any needed follow-up assessment
- Output: Verified course standing
- Constraints: These items are administrative, not algorithm topics

### Core Idea
- Confirm final results and complete any required end-of-term steps.

### Algorithm
1. Check the posted grade.
2. Complete any remedial or verification process if needed.
3. Confirm final status in Blackboard.

### Correctness
- Invariant: the posted information matches the official record.
- Why it works: the process resolves discrepancies before the term closes.
- Termination: the final grade is confirmed.

### Complexity
- Time: minimal.
- Space: minimal.
- Bottleneck: waiting for official confirmation.

### Edge Cases
- Missing grade posting.
- Need for remedial exam.
- Blackboard mismatch.

### Review Notes
- Source rows: Week 14, Meetings 1-3, F2F/ASYNC