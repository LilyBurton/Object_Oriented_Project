from lib.todo_list import TodoList

def test_construct_task():
    todo = TodoList("Clean the kitchen")
    assert todo.task == "Clean the kitchen"

def test_task_is_incomplete():
    todo = TodoList("Clean the kitchen")
    assert todo.complete == False
    
def test_task_is_complete():
    todo = TodoList("Clean the kitchen")
    todo.mark_complete()
    assert todo.complete == True