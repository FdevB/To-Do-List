"""
a To_Do List with python==3.13.2
"""

from datetime import datetime

from module import auto_num_gen


class Task():
    """
    create Task object
    """
    def __init__(self, name, descriptionn=None):
        self.id = next(auto_num_gen)
        self.name = name
        self.status = False
        self.date = datetime.now()
        self.descriptionn = descriptionn

    def __str__(self):
        return f"the {self.name} with id {self.id} created at {self.date} |" + (" YES" if self.status is True else " NO")
