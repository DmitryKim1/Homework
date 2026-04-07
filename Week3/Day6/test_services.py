from services import (
    get_next_id,
    add_task,
    find_task_by_id,
    mark_task_done,
    delete_task
)

def test_get_next_id():
    assert get_next_id([]) == 1
    assert get_next_id([{"id":1}, {"id":2}])

def test_add_task():
    tasks = []
    task = add_task(tasks, "Test", "high")

    assert len(tasks) == 1
    assert task["title"] == "Test"
    assert task["done"] is False

def test_find_task():
    tasks = [{"id": 1, "title": "A", "done": False}]

    task = find_task_by_id(tasks, 1)

    assert task is not None
    assert task["title"] == "A"

def test_mark_done():
    tasks = [{"id": 1, "title": "A", "done": False}]

    result = mark_task_done(tasks, 1)

    assert result is True
    assert tasks[0]["done"] is True

def test_delete_task():
    tasks = [{"id": 1, "title": "A", "done": False}]
    
    result = delete_task(tasks, 1)
    
    assert result is True
    assert len(tasks) == 0

if __name__ == "__main__":
    test_get_next_id()
    test_add_task()
    test_find_task()
    test_mark_done()
    test_delete_task()