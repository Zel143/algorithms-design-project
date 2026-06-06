# Project Report

## Problem
We need to schedule a set of tasks so that each task is completed before its deadline and the total profit is as large as possible.

## Inputs
- A list of tasks
- Each task has an id, a deadline, and a profit

## Outputs
- The selected tasks
- The time slots assigned to each task
- The total profit

## Algorithm Choice
Use a greedy algorithm:
1. Sort tasks by profit in descending order.
2. For each task, place it in the latest available slot before its deadline.
3. Skip the task if no valid slot exists.

## Why This Approach
This route is simple to explain, easy to implement, and matches the project rules for clarity and complexity analysis.

## Time Complexity
If there are n tasks and d time slots, the worst-case time complexity is O(n * d) after sorting.

## Space Complexity
The space complexity is O(d) for the slot array.

## Alternative Approach
A brute-force search could check every possible task combination, but it would be much slower and less practical for a class project.

## Test Case
The sample input used in this demo is:
- Task A: Deadline 4, Profit 20
- Task B: Deadline 1, Profit 10
- Task C: Deadline 1, Profit 40
- Task D: Deadline 1, Profit 30

Expected result:
- Selected Tasks: C, A
- Total Profit: 60
- Schedule: Slot 1 -> C, Slot 4 -> A
