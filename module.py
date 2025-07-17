"""
some module for To-Do list app
"""

def auto_number():
    """
    a genarator for create auto number

    input --> None
    output --> number
    """
    number = 1
    while True:
        yield number
        number += 1
auto_num_gen = auto_number()

# --------------------------
