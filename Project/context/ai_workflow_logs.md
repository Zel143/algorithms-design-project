# AI Workflow Logs

Use this file to track important workflow actions for the Algorithms and Design Project.

## Log Template

- Date:
- Action:
- Files:
- Validation:
- Notes:

## Entries
- Date: 2026-06-01
- Action: Added a sample project output file for the task scheduling topic in the sample project folder.
- Files: sample project/sample_output.md
- Validation: Confirmed the target folder was empty before creating the file.
- Notes: Kept the content aligned with the existing workflow and project topic.
- Date: 2026-06-01
- Action: Added a runnable source code sample for task scheduling with deadlines and profits.
- Files: sample project/task_scheduling.py
- Validation: Pending runtime check.
- Notes: The script is intended to produce the same schedule shown in sample_output.md.
- Date: 2026-06-01
- Action: Added a package README and short report to organize the demo in problem, code, output, report order.
- Files: sample project/README.md; sample project/report.md
- Validation: Pending folder check.
- Notes: The README now points to the code, output, and report files.
- Date: 2026-06-06
- Action: Created project proposal for 0/1 Knapsack using Dynamic Programming.
- Files: knapsack project/proposal.md
- Validation: Reviewed input/outcome alignment with prof's required format (brief discussion, input, outcome).
- Notes: Topic chosen as a DP alternative to the Greedy sample project.
- Date: 2026-06-06
- Action: Scaffolded full knapsack project folder mirroring sample project structure.
- Files: knapsack project/README.md; knapsack project/knapsack.py; knapsack project/sample_output.md; knapsack project/report.md
- Validation: Ran knapsack.py — output confirmed: Selected Items B, C; Total Weight 5; Total Profit 22.
- Notes: Removed misplaced proposal.md from Project root. DP table display added for visual clarity.
- Date: 2026-06-06
- Action: Updated context folder files to reflect the active knapsack project.
- Files: context/ai_workflow.md; context/ai_workflow_logs.md; context/karpathy-rules.md
- Validation: All three context files reviewed and updated with current project state.
- Notes: ai_workflow.md now lists active project files and algorithm class. karpathy-rules.md notes the selected topic.
- Date: 2026-06-06
- Action: Switched active project topic from 0/1 Knapsack (DP) to Task Scheduling with Deadlines and Profits (Greedy).
- Files: task scheduling project/proposal.md; task scheduling project/task_scheduling.py; task scheduling project/sample_output.md; task scheduling project/report.md; task scheduling project/README.md
- Validation: Ran task_scheduling.py -- output confirmed: Selected C, A; Skipped D, B; Total Profit 60.
- Notes: knapsack project/ kept as reference. Context files and root README updated to reflect the new active topic.
- Date: 2026-06-09
- Action: Updated project context after submitting the Algorithms and Complexity proposal for "The Geometry of AI Decisions."
- Files: Algorithms_and_Complexity_Proposal.md; context/ai_workflow.md; context/karpathy-rules.md; context/current_instructions.md; context/ai_workflow_logs.md
- Validation: Reviewed submitted proposal content and aligned active project metadata with its topic, inputs, outcomes, references, and follow-up deliverables.
- Notes: Active project is now the zero-dependency k-NN distance-metric comparison using Euclidean and Manhattan distance. Previous task-scheduling and knapsack work should be treated as reference only.
- Date: 2026-06-09
- Action: Logged unrelated pre-existing worktree deletions observed during context update.
- Files: sample project/README.md; sample project/knapsack project/knapsack.py; sample project/knapsack project/md_to_pdf.py; sample project/knapsack project/proposal.md; sample project/knapsack project/report.md; sample project/knapsack project/sample_output.md; sample project/report.md; sample project/sample_output.md; sample project/task_scheduling.py; task scheduling project/README.md; task scheduling project/presentation_plan.md; task scheduling project/proposal.md; task scheduling project/report.md; task scheduling project/sample_output.md; task scheduling project/task_scheduling.py
- Validation: Confirmed through `git status --short` that these files were already marked deleted and unrelated to the context-file update.
- Notes: Deletions were not reverted or modified. They remain separate from the submitted k-NN proposal context update.
- Date: 2026-06-09
- Action: Assigned remaining team workflow roles using the unassigned members from the submitted proposal team list.
- Files: team_workflow.md; context/ai_workflow_logs.md
- Validation: Filled both `ASSIGNEE NEEDED` placeholders with proposal-listed members who did not already have roles: Jon Luigi L. Ariola and Melprin O. Correa.
- Notes: Jon Luigi L. Ariola is assigned Lead Algorithm Architect. Melprin O. Correa is assigned Complexity & Technical Reporter.


- Date: 2026-06-09
- Action: Added a starter handoff guide so each groupmate can begin their assigned project duty.
- Files: team_workflow.md; context/ai_workflow_logs.md
- Validation: Added concrete start tasks, expected outputs, dependencies, and a first team checkpoint aligned with the k-NN proposal.
- Notes: The guide is intended to unblock parallel work before implementation starts.
- Date: 2026-06-09
- Action: Completed Ranzel's starter task for dataset curation and edge-case planning.
- Files: ranzel_dataset_and_edge_cases.md; team_workflow.md; context/ai_workflow.md; context/ai_workflow_logs.md
- Validation: Created an 18-point fruit-classification training dataset, 8 boundary-focused test points, edge-case handling table, deterministic tie-breaking rules, and handoff notes for algorithm, testing, and documentation roles.
- Notes: Dataset uses Weight and Sweetness as 2D features with Lemon, Apple, and Banana classes.
- Date: 2026-06-09
- Action: Split ACM-style references into a separate file and added a root `.gitignore`.
- Files: ranzel_dataset_references.md; ranzel_dataset_and_edge_cases.md; .gitignore; context/ai_workflow_logs.md
- Validation: Added a dedicated reference file for the k-NN context and a sensible ignore list for editor, log, temporary, and Python artifact files.
- Notes: The dataset handoff remains original material; the new references file provides academic context only.
- Date: 2026-06-17
- Action: Created project scaffolding and starter files for the k-NN implementation.
- Files: geometry_of_ai/data_loader.py; geometry_of_ai/knn_engine.py; geometry_of_ai/testing_harness.py; geometry_of_ai/README.md; team_workflow.md
- Validation: Verified dataset integrity in data_loader.py and structure of the testing harness.
- Notes: Scaffolding unblocks Jon (Algorithm), Stephanie (Testing), and Fiona/Melprin (Documentation) to work in parallel. Logic implementation remains as a follow-up for the Lead Architect.
- Date: 2026-06-19
- Action: Implemented geometric tie-breaking in knn_engine.py and updated tie-breaking documentation in ranzel_dataset_and_edge_cases.md per CHANGES_TO_IMPLEMENT.md.
- Files: geometry_of_ai/knn_engine.py; ranzel_dataset_and_edge_cases.md
- Validation: Ran `git push` — commit 3b2fbed pushed to main. Both files confirmed updated. No syntax errors.
- Notes: predict() and _tie_break() methods fully implemented. Tie-breaking now selects the tied class with the smallest average distance to its k neighbors (deterministic, insertion-order independent). Fixed class priority (Apple, Banana, Lemon) retained as last-resort fallback only.
