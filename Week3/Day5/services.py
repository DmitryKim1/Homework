def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def add_task(tasks, title,priority):
    task = {
        "id": get_next_id(tasks),
        "title": title,
        "done": False,
        "priority": priority
    }
    tasks.append(task)
    return task
