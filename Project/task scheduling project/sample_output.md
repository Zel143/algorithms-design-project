# Sample Output

## Project Title
Task Scheduling with Deadlines and Profits

## Objective
Maximize total profit by scheduling tasks before their deadlines using a greedy approach.

## Input

| Task | Deadline | Profit |
|------|----------|--------|
| A    | 4        | 20     |
| B    | 1        | 10     |
| C    | 1        | 40     |
| D    | 1        | 30     |

## Greedy Trace

| Task | Profit | Deadline | Assigned Slot    |
|------|--------|----------|------------------|
| C    | 40     | 1        | Slot 1           |
| D    | 30     | 1        | Skipped (no slot)|
| A    | 20     | 4        | Slot 4           |
| B    | 10     | 1        | Skipped (no slot)|

## Output

- Selected Tasks : C, A
- Skipped Tasks  : D, B
- Total Profit   : 60

## Schedule

| Time Slot | Task  |
|-----------|-------|
| Slot 1    | C     |
| Slot 2    | Empty |
| Slot 3    | Empty |
| Slot 4    | A     |
