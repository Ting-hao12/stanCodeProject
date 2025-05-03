"""
File: MoveToTheEnd.py
Name:Ting-Hao Chang
------------------------
This file shows how to use while loop
to walk to the end of a certain row in
karel world
"""

from karel.stanfordkarel import *



def main():
    while front_is_clear():
        move()
    """
    Karel will move to the end of the first Street in any world
    """
    pass
# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
