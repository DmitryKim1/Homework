import json

def load_tasks(filename = "tasks.json"):
    try:
        with open(filename, "r", encoding = "utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    
def save_tasks(tasks, filename = "tasks.json"):
    with open(filename, "w", encoding = "utf-8") as file:
        json.dump(tasks, file, ensure_ascii = False, indent=2 )