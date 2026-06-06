# Karpathy Rules for Algorithm Review

Use these rules while studying algorithms and complexity:

1. Be concrete.
   - State the problem, input, output, and constraints before solving.
   - Prefer one clear example over vague summaries.

2. Build from first principles.
   - Explain why the algorithm works, not just what it does.
   - Derive complexity from loops, recursion depth, and data structure costs.

3. Keep notation consistent.
   - Define variables once and reuse them.
   - Distinguish worst-case, average-case, and best-case complexity.

4. Use invariants.
   - Identify what remains true at each step of the algorithm.
   - Use invariants to justify correctness.

5. Check edge cases early.
   - Empty input, size 1, duplicates, sorted input, reverse-sorted input, and extreme values.

6. Favor small proofs.
   - Split correctness into claims you can verify independently.
   - If a proof feels too large, reduce it to a lemma.

7. Compare alternatives.
   - Mention a simpler baseline and why the chosen method is better.
   - Note time/space tradeoffs when they matter.

8. Write the final answer in this order.
   - Problem summary
   - Idea
   - Correctness argument
   - Complexity
   - Edge cases
