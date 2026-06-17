# Team Workflow & Handoff Guide

**Project:** The Geometry of AI Decisions (k-NN Classifier)
**Status:** Proposal Submitted. Scaffolding Created.

## Group Roles & Starter Tasks

| Assignee | Role | Starter Task | Expected Output |
| :--- | :--- | :--- | :--- |
| **Jon Luigi L. Ariola** | Lead Algorithm Architect | Complete logic in `knn_engine.py` | Functional `predict()` with tie-breaking |
| **Stephanie Keith Sison** | Test & Validation | Run `testing_harness.py` | Comparison table (Euclidean vs Manhattan) |
| **Fiona Hailey L. Maraña** | Documentation & Viz | Draft report & Viz | `report_draft.md` + Plotting logic |
| **Melprin O. Correa** | Complexity Reporter | Profile `knn_engine.py` | Big O analysis (Time/Space) |
| **David Solano** | Mathematical Engineer | Verify distance formulas | Formal proof of metric behavior |
| **Ranzel Jude M. Virtucio** | Data & Edge Cases | (COMPLETED) Curate dataset | `data_loader.py` implementation |

---

## Handoff Guide (Update 2026-06-17)

Starter files are available in the `geometry_of_ai/` directory. Use these to begin parallel implementation.

### 1. JON (Algorithm)
- **File:** `geometry_of_ai/knn_engine.py`
- **Task:** Implement the `predict()` and `_tie_break()` methods. 
- **Rule:** Use deterministic tie-breaking (Vote count -> Average Distance -> Class Priority).

### 2. STEPHANIE (Testing)
- **File:** `geometry_of_ai/testing_harness.py`
- **Task:** Run the script with `python testing_harness.py`.
- **Goal:** Once Jon finishes the engine, record the outputs for T1-T8 across Euclidean and Manhattan metrics.

### 3. FIONA & MELPRIN (Report)
- **File:** `geometry_of_ai/README.md`
- **Task:** Use the technical details in the README and code comments to draft the "Methodology" and "Complexity" sections of the report.

### 4. DAVID (Mathematics)
- **Task:** Review the `euclidean_distance` and `manhattan_distance` functions in `knn_engine.py` to ensure they match the project's geometric requirements.

---

## Technical Resources
- **Dataset:** `geometry_of_ai/data_loader.py`
- **Rules & Constraints:** `ranzel_dataset_and_edge_cases.md`
- **Project Requirements:** `context/karpathy-rules.md`
