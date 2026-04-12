# ==============================
# DATA INITIALIZATION
# ==============================

tasks = [
    {"name": "Estudar Python", "done": True},
    {"name": "Treinar", "done": False},
    {"name": "Ler livro", "done": True},
    {"name": "Estudar scraping", "done": False}
]

raw_tasks = [
    "Estudar Python - DONE",
    "Treinar - PENDING",
    "Ler livro - DONE",
    "Estudar scraping - PENDING"
]


# ==============================
# BUSINESS LOGIC
# ==============================

def group_tasks(tasks):
    """
    Groups tasks into 'done' and 'pending'.
    Also returns summary statistics.
    """
    pending_tasks = []
    done_tasks = []

    for task in tasks:
        if task['done']:
            done_tasks.append(task)
        else:
            pending_tasks.append(task)
    
    return {
        "done": done_tasks,
        "pending": pending_tasks,
        "total": len(tasks),
        "done_count": len(done_tasks),
        "pending_count": len(pending_tasks)
    }


def organize_raw_tasks(raw_tasks):
    """
    Converts raw task strings into structured dictionaries.
    Example: "Task - DONE" -> {"name": ..., "done": True}
    """
    pending_tasks = []
    done_tasks = []

    for task in raw_tasks:
        parts = task.split("-")

        # Skip invalid formats
        if len(parts) < 2:
            continue

        name = parts[0].strip()
        status = parts[1].strip()

        task_dict = {
            "name": name,
            "done": True if status == "DONE" else False
        }

        if task_dict["done"]:
            done_tasks.append(task_dict)
        else:
            pending_tasks.append(task_dict)

    return {
        "done": done_tasks,
        "pending": pending_tasks
    }


# ==============================
# OUTPUT (CLI DISPLAY)
# ==============================

print("\n=== TASK SUMMARY ===")

grouped = group_tasks(tasks)

print(f"Total tasks: {grouped['total']}")
print(f"Completed: {grouped['done_count']}")
print(f"Pending: {grouped['pending_count']}")


print("\n--- COMPLETED TASKS ---")
if grouped["done"]:
    for task in grouped["done"]:
        print(f"- {task['name']}")
else:
    print("No completed tasks.")


print("\n--- PENDING TASKS ---")
if grouped["pending"]:
    for task in grouped["pending"]:
        print(f"- {task['name']}")
else:
    print("No pending tasks.")


# ==============================
# RAW TASKS PROCESSING
# ==============================

print("\n=== ORGANIZED RAW TASKS ===")

organized = organize_raw_tasks(raw_tasks)


print("\n--- COMPLETED (FROM RAW) ---")
if organized["done"]:
    for task in organized["done"]:
        print(f"- {task['name']}")
else:
    print("No completed tasks.")


print("\n--- PENDING (FROM RAW) ---")
if organized["pending"]:
    for task in organized["pending"]:
        print(f"- {task['name']}")
else:
    print("No pending tasks.")