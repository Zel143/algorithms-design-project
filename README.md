# Algorithms Design Project

Welcome to the **Algorithms and Complexity** project repository. This repository
contains the active project implementation and reference materials for the course.

---

## Repository Structure

```
.
├── Project/
│   ├── task scheduling project/    # Active Project Delivery
│   │   ├── README.md
│   │   ├── task_scheduling.py      # Greedy implementation with trace output
│   │   ├── proposal.md             # Topic proposal with input and outcome
│   │   ├── sample_output.md        # Verified code output
│   │   └── report.md               # Full written analysis and complexity report
│   │
│   ├── knapsack project/           # Previous draft (DP), kept for reference
│   │
│   ├── sample project/             # Professor's reference demo (same topic)
│   │   ├── task_scheduling.py
│   │   ├── sample_output.md
│   │   └── report.md
│   │
│   └── context/                    # Handouts and workflow instructions
```

---

## Active Topic: Task Scheduling with Deadlines and Profits

The main design project solves the **Task Scheduling with Deadlines and Profits**
problem using a **Greedy Algorithm**: sort tasks by profit descending, then place
each in the latest available slot before its deadline to maximize total profit.

### Deliverables Quick Links

1. **Proposal:** [proposal.md](Project/task%20scheduling%20project/proposal.md) -- topic discussion, input, and expected outcome.
2. **Code:** [task_scheduling.py](Project/task%20scheduling%20project/task_scheduling.py) -- greedy implementation with step-by-step trace.
3. **Output:** [sample_output.md](Project/task%20scheduling%20project/sample_output.md) -- verified schedule and profit result.
4. **Report:** [report.md](Project/task%20scheduling%20project/report.md) -- full analysis including complexity and greedy correctness argument.

---

## Running the Code

```bash
python "Project/task scheduling project/task_scheduling.py"
```
