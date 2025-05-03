"""
File: PotholeFilling.py
Name:Ting-hao Chang 
TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
from StepUp import *
def go_back():
    turn_left()
    turn_left()
def go_in():
    """
    pre-condition: Karel is lacated at the upper left of the pothole and facing east
    post-condition: Karel is in the pothole and facing south
    """
    move()
    turn_right()
    move()
def go_out():
    """
    pre-condition:Karel is in the pothole and facing south
    post-condition:Karel is the the top of the pothole and facing north
    """
    go_back()
    move()
    turn_right()
    move()


def main():
    """
    TODO:
    """
    for i in range(3):
        go_in()
        put_beeper99()
        go_out()



# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
