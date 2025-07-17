"""
a To_Do List with python==3.13.2
"""

from datetime import datetime

from module import auto_num_gen


class Task():
    """
    Represents a task with name, description, status, creation date, and unique id.
    """
    def __init__(self, name, description=None):
        self.id = next(auto_num_gen)
        self.name = name
        self.status = False
        self.date = datetime.now()
        self.description = description

    def __str__(self):
        return f"the {self.name} with id {self.id} created at {self.date} |" + (" YES" if self.status is True else " NO") + f"\ndescription --> {self.description}\n"
    

class TaskManager():
    def __init__(self):
        self.tasks = []

    def create_task(self, name, description=None):
        """create a task"""
        task = Task(name, description)
        self.tasks.append(task)

    def show_tasks(self):
        """show all task"""
        for task in self.tasks:
            print(task)

    def edit_task(self, id, name, description=None):
        """edited a task with id"""
        self.tasks[id - 1] = Task(name, description)

    def remove_task(self, id):
        self.tasks.pop(id-1)

    def mark_done(self, id):
        task = self.tasks[id - 1]
        if task.status is False:
            task.status = True
        else:
            self.status = False

        self.tasks[id - 1] = task
