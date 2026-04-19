from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    done: bool

task = Task(1, "Learn Python", False)
task2 = Task(2, "Write code", True)

print(task.title)
print(task2.done)