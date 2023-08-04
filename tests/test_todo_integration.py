from lib.Todo import ToDo
from lib.todo_list import TodoList

def test_add_todo_in_todo_list():
    todo = ToDo()
    todo1 = TodoList("Clean the kitchen")
    todo2 = TodoList("Go for a walk")
    todo.add(todo1)
    todo.add(todo2)
    assert todo.incomplete() == [todo1, todo2]

def test_complete_task_not_in_incomplete_list():
    todo = ToDo()
    todo1 = TodoList("Clean the kitchen")
    todo2 = TodoList("Go for a walk")
    todo.add(todo1)
    todo.add(todo2)
    todo1.mark_complete()
    assert todo.incomplete() == [todo2]

def test_complete_task_in_complete_list():
    todo = ToDo()
    todo1 = TodoList("Clean the kitchen")
    todo2 = TodoList("Go for a walk")
    todo.add(todo1)
    todo.add(todo2)
    todo1.mark_complete()
    assert todo.complete() == [todo1]