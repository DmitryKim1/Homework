from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    done: bool

class TaskService:
    def __init__(self):
        self.tasks: list[Task] = []

    def add_task(self, title: str) -> Task:
        new_id = len(self.tasks) + 1
        task = Task(new_id, title, False)
        self.tasks.append(task)
        return task
    
    def get_all_tasks(self) -> list[Task]:
        return self.tasks
    
    def mark_done(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                task.done = True
                return True
        return False
    
service = TaskService()

service.add_task("Learn dataclass")
service.add_task("Read Python")

service.mark_done(1)

for task in service.get_all_tasks():
    print(task)