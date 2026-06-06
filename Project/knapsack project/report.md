# Project Report

## Problem
We need to select items from a list, each with a weight and a profit, to fit
into a knapsack of fixed capacity, such that the total profit is maximized
without exceeding the capacity. Each item may be taken at most once (0/1).

## Inputs
- A list of items, each with an id, a weight, and a profit
- A knapsack capacity W

## Outputs
- The selected items
- Total weight used
- Total profit achieved
- The DP table used to derive the solution

## Algorithm Choice
Use Dynamic Programming (bottom-up tabulation):
1. Build a 2D table `dp[i][w]` = best profit using the first `i` items with
   capacity `w`.
2. For each item, either skip it (`dp[i-1][w]`) or include it if it fits
   (`dp[i-1][w - weight] + profit`), taking the maximum.
3. Backtrack through the table to recover the selected items.

## Why This Approach
Greedy (e.g., always pick highest profit) fails for 0/1 Knapsack because a
locally optimal choice can prevent a globally better combination. DP guarantees
the optimal solution by considering all sub-problems.

Example: Greedy picks Item D (profit 15, weight 5) with no room left.
DP finds B + C (profit 22, weight 5) as a better solution.

## Time Complexity
O(n × W) where n is the number of items and W is the knapsack capacity.
After building the DP table, backtracking takes O(n).

## Space Complexity
O(n × W) for the DP table. Can be reduced to O(W) with a 1D rolling array,
but the 2D version is used here to allow backtracking and table display.

## Test Case
The sample input used in this demo is:
- Item A: Weight 2, Profit 6
- Item B: Weight 2, Profit 10
- Item C: Weight 3, Profit 12
- Item D: Weight 5, Profit 15
- Knapsack Capacity: 5

Expected result:
- Selected Items : B, C
- Total Weight   : 5
- Total Profit   : 22
