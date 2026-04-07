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

def get_all_tasks(tasks):
    return tasks

def get_undone_tasks(tasks):
    return [task for task in tasks if not task["done"]]

def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

def search_tasks(tasks, keyword):
    keyword = keyword.lower()
    return [task for task in tasks if keyword in task["title"].lower()]

def mark_task_done(tasks, task_id):
    task = find_task_by_id(tasks, task_id)
    if task is None:
        return False
    if task["done"]:
        return "already_done"
    task["done"] = True
    return True

def delete_task(tasks, task_id):
    task = find_task_by_id(tasks, task_id)
    if task is None:
        return False
    tasks.remove(task)
    return True

def get_statistics(tasks):
    stats = {
        "total": len(tasks),
        "done": 0,
        "undone": 0,
        "by_priority": {
            "low": 0,
            "medium": 0,
            "high": 0
        }
    }

    for task in tasks:
        if task["done"]:
            stats["done"] += 1
        else:
            stats["undone"] += 1

        priority = task["priority"]
        if priority in stats["by_priority"]:
            stats["by_priority"][priority] += 1

    return stats