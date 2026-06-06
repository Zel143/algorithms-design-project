def schedule_tasks(tasks):
    max_deadline = max(task["deadline"] for task in tasks)
    slots = [None] * max_deadline
    selected = []

    for task in sorted(tasks, key=lambda item: item["profit"], reverse=True):
        for slot in range(min(task["deadline"], max_deadline) - 1, -1, -1):
            if slots[slot] is None:
                slots[slot] = task["id"]
                selected.append(task["id"])
                break

    total_profit = sum(task["profit"] for task in tasks if task["id"] in selected)
    return selected, slots, total_profit


def main():
    tasks = [
        {"id": "A", "deadline": 4, "profit": 20},
        {"id": "B", "deadline": 1, "profit": 10},
        {"id": "C", "deadline": 1, "profit": 40},
        {"id": "D", "deadline": 1, "profit": 30},
    ]

    selected, slots, total_profit = schedule_tasks(tasks)

    print("Project Title: Task Scheduling with Deadlines and Profits")
    print()
    print("Objective:")
    print("Maximize total profit by scheduling tasks before their deadlines.")
    print()
    print("Input:")
    for task in tasks:
        print(f"Task {task['id']} -> Deadline: {task['deadline']}, Profit: {task['profit']}")
    print()
    print("Output:")
    print(f"Selected Tasks: {', '.join(selected)}")
    print(f"Total Profit: {total_profit}")
    print()
    print("Schedule:")
    for index, task_id in enumerate(slots, start=1):
        label = task_id if task_id is not None else "Empty"
        print(f"Time Slot {index} -> {label}")


if __name__ == "__main__":
    main()
