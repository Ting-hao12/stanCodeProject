"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    while not front_is_clear():
        turn_left()
        move()
        turn_right()
    # alternative defination
    """
    turn_left()
    while not front_is_clear():
        move()
    """
def down():
    turn_right()
    while front_is_clear():
        move()
    turn_left()

#def cross():

def main():
    """
    pre-condition Karel is at the north side of the pole and facing east
    post-cndi1tion Karel is on the south side of the pole
    """
    for i in range(19):
        if front_is_clear():
            move()
            down()
        else:
            jump()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
