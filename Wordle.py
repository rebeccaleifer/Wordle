# File: Wordle.py

"""
IS405 Project 4 
Group 5: Rebecca Leifer, Brayden Buhler, YunChen Lee, Levi Morse, Ransom Allphin


"""

import random
from random import choice
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import CORRECT_COLOR, WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        gw.show_message("You have to implement this method.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # set white color as default for keys as users play the game
    # set white color as default til users click ENTER

    # change the key color based on the validation
    # embedded in the loop of validation
    gw.set_key_color("Q", CORRECT_COLOR)
    gw.get_key_color("Q")


# Startup code

if __name__ == "__main__":
    wordle()
    # TheWordle = choice(FIVE_LETTER_WORDS)
    # print(TheWordle)