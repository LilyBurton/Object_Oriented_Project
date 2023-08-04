class ToDo:

    def __init__(self):
        self._tasklist = []

    def add(self, task):
        self._tasklist.append(task)
    
    def incomplete(self):
        return [task for task in self._tasklist if not task.complete]
        

    def complete(self):
        return [task for task in self._tasklist if task.complete == True]