def knapsack(capacity, items):
    n = len(items)

    # Build DP table: (n+1) rows x (capacity+1) columns
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item = items[i - 1]
        for w in range(capacity + 1):
            # Option 1: skip this item
            dp[i][w] = dp[i - 1][w]
            # Option 2: include this item (if it fits)
            if item["weight"] <= w:
                include = dp[i - 1][w - item["weight"]] + item["profit"]
                if include > dp[i][w]:
                    dp[i][w] = include

    # Backtrack to find selected items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(items[i - 1]["id"])
            w -= items[i - 1]["weight"]

    selected.reverse()
    total_profit = dp[n][capacity]
    total_weight = sum(item["weight"] for item in items if item["id"] in selected)
    return selected, total_profit, total_weight, dp


def print_dp_table(dp, items, capacity):
    header = "       " + "  ".join(f"W={w:2}" for w in range(capacity + 1))
    print(header)
    print("-" * len(header))
    print(f"{'(none)':<8}" + "  ".join(f"{dp[0][w]:5}" for w in range(capacity + 1)))
    for i, item in enumerate(items, start=1):
        label = f"Item {item['id']}"
        print(f"{label:<8}" + "  ".join(f"{dp[i][w]:5}" for w in range(capacity + 1)))


def main():
    items = [
        {"id": "A", "weight": 2, "profit": 6},
        {"id": "B", "weight": 2, "profit": 10},
        {"id": "C", "weight": 3, "profit": 12},
        {"id": "D", "weight": 5, "profit": 15},
    ]
    capacity = 5

    print("Project Title: 0/1 Knapsack Problem Using Dynamic Programming")
    print()
    print("Objective:")
    print("Maximize total profit without exceeding knapsack capacity.")
    print()
    print("Input:")
    print(f"  Knapsack Capacity: {capacity}")
    for item in items:
        print(f"  Item {item['id']} -> Weight: {item['weight']}, Profit: {item['profit']}")
    print()

    selected, total_profit, total_weight, dp = knapsack(capacity, items)

    print("DP Table:")
    print_dp_table(dp, items, capacity)
    print()
    print("Output:")
    print(f"  Selected Items : {', '.join(selected)}")
    print(f"  Total Weight   : {total_weight}")
    print(f"  Total Profit   : {total_profit}")


if __name__ == "__main__":
    main()
