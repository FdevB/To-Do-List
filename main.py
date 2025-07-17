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
        self._id = next(auto_num_gen)
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
        return task

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


class CommandLine():
    task_manager = TaskManager()
    def create(self):
        name = input("give the task name: ")
        description = input("give the task description (optional): ")
        task = self.task_manager.create_task(name, description)
        print(f"your new task --> {task}")
    
    def edit(self):
        id = int(input("give the task id you want edited: "))
        name = input("give the task name: ")
        description = input("give the task description (optional): ")
        task = self.task_manager.edit_task(id, name, description)
        print(f"succesfuly, your new update of task --> {task}")

    def mark_down(self):
        id = int(input("give the task id you want edited: "))
        task = self.task_manager.mark_done(id)
        print(f"succesfuly, your new update of task --> {task}")

    def remove(self):
        id = int(input("give the task id you want edited: "))
        self.task_manager(id)
        print("succesfully removed")

    def show_all(self):
        self.task_manager.show_tasks()
