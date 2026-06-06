# Sample Project Output

## Project Title
0/1 Knapsack Problem Using Dynamic Programming

## Objective
Maximize total profit without exceeding knapsack capacity.

## Input
- Knapsack Capacity: 5
- Item A -> Weight: 2, Profit: 6
- Item B -> Weight: 2, Profit: 10
- Item C -> Weight: 3, Profit: 12
- Item D -> Weight: 5, Profit: 15

## DP Table

|        | W=0 | W=1 | W=2 | W=3 | W=4 | W=5 |
|--------|-----|-----|-----|-----|-----|-----|
| (none) | 0   | 0   | 0   | 0   | 0   | 0   |
| Item A | 0   | 0   | 6   | 6   | 6   | 6   |
| Item B | 0   | 0   | 10  | 10  | 16  | 16  |
| Item C | 0   | 0   | 10  | 12  | 16  | 22  |
| Item D | 0   | 0   | 10  | 12  | 16  | 22  |

## Output
- Selected Items : B, C
- Total Weight   : 5
- Total Profit   : 22
