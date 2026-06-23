# Team Workflow & Handoff Guide

**Project:** The Geometry of AI Decisions (k-NN Classifier)
**Status:** Proposal Submitted. Scaffolding Created.

## Group Roles & Starter Tasks

| Assignee | Role | Starter Task | Expected Output |
| :--- | :--- | :--- | :--- |
| **Luigi L. Ariola** | Lead Algorithm Architect | Complete logic in `knn_engine.py` | Functional `predict()` with tie-breaking |
| **Stephanie Keith Sison** | Test & Validation | Run `testing_harness.py` | Comparison table (Euclidean vs Manhattan) |
| **Fiona Hailey L. Maraña** | Documentation & Viz | Draft report & Viz | `report_draft.md` + Plotting logic |
| **Melprin O. Correa** | Complexity Reporter | Profile `knn_engine.py` | Big O analysis (Time/Space) |
| **David Solano** | Mathematical Engineer | Verify distance formulas | Formal proof of metric behavior |
| **Ranzel Jude M. Virtucio** | Data & Edge Cases | (COMPLETED) Curate dataset | `data_loader.py` implementation |

---

## Handoff Guide (Update 2026-06-17)

Starter files are available in the `geometry_of_ai/` directory. Use these to begin parallel implementation.

### 1. LUIGI (Algorithm)
- **File:** `geometry_of_ai/knn_engine.py`
- **Task:** Implement the `predict()` and `_tie_break()` methods. 
- **Rule:** Use deterministic tie-breaking (Vote count -> Average Distance -> Class Priority).

### 2. STEPHANIE (Testing)
- **File:** `geometry_of_ai/testing_harness.py`
- **Task:** Run the script with `python testing_harness.py`.
- **Goal:** Once Luigi finishes the engine, record the outputs for T1-T8 across Euclidean and Manhattan metrics.

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




## log team status
- **June 19, 2026** Hello 

Everyone



Nag-push na ako ng initial setup sa repository para pwede na tayong mag-work nang sabay-sabay nang walang nagkakabanggaang files.



Ito yung status ng code natin ngayon at yung mga susunod nating gagawin:



1. Iniskedyul ko na yung Code (Clean Slate)

Binalik ko muna sa blankong "TODO" placeholders yung `geometry_of_ai/knn_engine.py`. Tinanggal ko muna yung mga nauna kong sinulat para malinis at walang maging merge conflicts habang gumagawa tayo.



2. May Testing Suite na Tayo (`geometry_of_ai/test_knn.py`)

Gumawa ako ng automatic tests para i-check kung tama yung magiging code natin (kasama na yung handling sa errors at tie-breaking). Dahil blanko pa yung code, expected na bagsak pa yung 6 out of 7 tests natin ngayon.

@Luigi: Pwede mong i-run yung `python -m unittest geometry_of_ai/test_knn.py` habang nagre-code ka para makita mo kung anong gumagana at anong kulang.



3. Tool para sa Charts (`geometry_of_ai/main.py`)

Gumawa na rin ako ng script na automatic mag-da-draw ng side-by-side charts para sa Euclidean vs. Manhattan boundaries natin. Kapag gumagana na yung code ni Luigi at pumasa sa tests, i-run lang 'to at automatic nang mase-save yung mga images (`decision_boundaries_k3.png` at `decision_boundaries_k5.png`) sa folder natin.



4. Next Steps & Handoff (Sino ang blocked at sino ang pwede na magsimula?)

• @Luigi (Hindi blocked): Pa-code nung `predict()` at `_tie_break()` sa `knn_engine.py`. Goal natin is makuha yung 7/7 passing score sa tests natin.

• @Stephanie (Blocked kay Luigi): Kapag tapos na si Luigi, pa-run nung `python geometry_of_ai/testing_harness.py` para makuha natin yung mga numero at accuracy scores para sa table ng report natin.

• @Fiona (Blocked kay Luigi): Pa-run ng `main.py` kapag okay na yung tests ni Luigi para ma-download mo yung mga charts na ilalagay natin sa docs.

• @Melprin (Hindi blocked): Pwede mo nang simulan i-analyze at isulat kung gaano kabilis tumakbo at gaano kalaking memory ang kinakain ng k-NN search at sorting parts natin (Big-O analysis).

• @David (Hindi blocked): Pwede mo nang simulan i-draft yung math side ng report natin—pa-explain kung bakit pabilog yung shape ng boundary kapag Euclidean distance ang gamit, at hugis diamond naman kapag Manhattan distance. By tuesday i'm hoping nakagawa na lahat ganon para formatting na lang ng paper alalalahanin for next week.



Mag-chat lang kayo dito sa thread natin kung may nagka-error sa inyo o kung may tanong kayo sa pag-run ng mga scripts! Btw yung sa docs pakitignan na rin yung Project draft na subdraft under project and pakidagdagan in research about the topic., ayun lang thanks.





eto yung git repository ulit: GitHub - Zel143/algorithms-design-project