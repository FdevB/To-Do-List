"""
a To_Do List with python==3.13.2
"""

from datetime import datetime
import json

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

    def load_db(self):
        with open('db.json', "r") as db:
            data = json.load(db)
            for item in data:
                task = Task(item['name'], item['description'])
                task.id = item['id']
                task.status = item['status']
                task.date = datetime.fromisoformat(item['date'])
                self.tasks.append(task)

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
        task = Task(name, description)
        task.id = id
        self.tasks[id - 1] = task

    def remove_task(self, id):
        self.tasks.pop(id-1)

    def mark_done(self, id):
        task = self.tasks[id - 1]
        if task.status is False:
            task.status = True
        else:
            self.status = False

        self.tasks[id - 1] = task

    def save_db(self):
        with open('db.json', 'w') as db:
            json.dump([task.__dict__ for task in self.tasks], db, default=str, indent=4)


class CommandLine():
    task_manager = TaskManager()
    
    def load(self):
        self.task_manager.load_db()

    def create(self):
        name = input("give the task name: ")
        description = input("give the task description (optional): ")
        task = self.task_manager.create_task(name, description)
        print(f"your new task --> {task}")
    
    def edit(self):
        id = int(input("give the task id you want edited: "))
        name = input("give the task name: ")
        description = input("give the task description (optional): ")
        self.task_manager.edit_task(id, name, description)
        print(f"succesfuly, your new update of task")

    def mark_down(self):
        id = int(input("give the task id you want mark down: "))
        task = self.task_manager.mark_done(id)
        print(f"succesfuly, your mark down the task")

    def remove(self):
        id = int(input("give the task id you want remove: "))
        self.task_manager.remove_task(id)
        print("succesfully removed")

    def show_all(self):
        self.task_manager.show_tasks()

    def save(self):
        self.task_manager.save_db()


command_line = CommandLine()
command_line.load()

commands = {
    'create': command_line.create,
    'edit': command_line.edit,
    'remove': command_line.remove,
    'mark down': command_line.mark_down,
    'show all': command_line.show_all,
}

print("\nAll task")
command_line.show_all()
while True:
    print()
    user_command = input("what do you want to do? ")
    user_command = user_command.lower()

    if user_command == 'stop':
        break

    try:
        commands[user_command]()
    except:
        print("invalid input")

command_line.save()
