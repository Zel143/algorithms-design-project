def schedule_tasks(tasks):
    """
    Greedy Task Scheduling with Deadlines and Profits.

    Steps:
      1. Sort tasks by profit descending (greedy choice).
      2. For each task, place it in the latest free slot at or before its deadline.
      3. Skip the task if no valid slot is available.

    Parameters:
        tasks (list[dict]): Each dict has keys 'id', 'deadline', 'profit'.

    Returns:
        selected (list[str]): IDs of scheduled tasks in slot order.
        slots    (list[str|None]): Slot array, index 0 = time slot 1.
        skipped  (list[str]): IDs of tasks that could not be scheduled.
        total_profit (int): Sum of profits of scheduled tasks.
    """
    max_deadline = max(task["deadline"] for task in tasks)
    slots = [None] * max_deadline
    selected = []
    skipped = []

    for task in sorted(tasks, key=lambda t: t["profit"], reverse=True):
        placed = False
        for slot in range(min(task["deadline"], max_deadline) - 1, -1, -1):
            if slots[slot] is None:
                slots[slot] = task["id"]
                selected.append(task["id"])
                placed = True
                break
        if not placed:
            skipped.append(task["id"])

    total_profit = sum(task["profit"] for task in tasks if task["id"] in selected)
    return selected, slots, skipped, total_profit


def print_greedy_trace(tasks):
    """Print a step-by-step greedy trace showing each decision."""
    max_deadline = max(task["deadline"] for task in tasks)
    slots = [None] * max_deadline
    sorted_tasks = sorted(tasks, key=lambda t: t["profit"], reverse=True)

    print("Greedy Trace:")
    print(f"  {'Task':<6} {'Profit':<8} {'Deadline':<10} {'Assigned Slot'}")
    print(f"  {'-'*4:<6} {'-'*6:<8} {'-'*8:<10} {'-'*13}")

    for task in sorted_tasks:
        placed_slot = None
        for slot in range(min(task["deadline"], max_deadline) - 1, -1, -1):
            if slots[slot] is None:
                slots[slot] = task["id"]
                placed_slot = slot + 1
                break
        status = f"Slot {placed_slot}" if placed_slot else "Skipped (no slot)"
        print(f"  {task['id']:<6} {task['profit']:<8} {task['deadline']:<10} {status}")


def main():
    tasks = [
        {"id": "A", "deadline": 4, "profit": 20},
        {"id": "B", "deadline": 1, "profit": 10},
        {"id": "C", "deadline": 1, "profit": 40},
        {"id": "D", "deadline": 1, "profit": 30},
    ]

    print("=" * 50)
    print("Task Scheduling with Deadlines and Profits")
    print("Algorithm: Greedy (sort by profit, fill latest slot)")
    print("=" * 50)
    print()

    print("Input:")
    print(f"  {'Task':<6} {'Deadline':<10} {'Profit'}")
    print(f"  {'-'*4:<6} {'-'*8:<10} {'-'*6}")
    for task in tasks:
        print(f"  {task['id']:<6} {task['deadline']:<10} {task['profit']}")
    print()

    print_greedy_trace(tasks)
    print()

    # Re-run cleanly for final output
    selected, slots, skipped, total_profit = schedule_tasks(tasks)

    print("Output:")
    print(f"  Selected Tasks : {', '.join(selected)}")
    print(f"  Skipped Tasks  : {', '.join(skipped) if skipped else 'None'}")
    print(f"  Total Profit   : {total_profit}")
    print()

    print("Schedule:")
    for index, task_id in enumerate(slots, start=1):
        label = task_id if task_id is not None else "Empty"
        print(f"  Time Slot {index} -> {label}")


if __name__ == "__main__":
    main()
