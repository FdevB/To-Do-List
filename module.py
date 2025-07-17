"""
some module for To-Do list app
"""

def auto_number():
    number = 1
    while True:
        yield number
        number += 1
