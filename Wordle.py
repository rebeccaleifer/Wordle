# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
from random import choice
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS



def wordle():

    def enter_action(s):
        gw.show_message("You have to implement this method.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

def colorCheck(word, guess):
    guessScore = ["white", "white", "white", "white", "white"]
    wordTemp = word
    index = 0
    # Checking for GREEN
    for char in wordTemp:
        if char == guess[index]:
            guessScore[index] = "green"
            wordTemp = wordTemp[:index] + "_" + wordTemp[index + 1:]
            print(wordTemp + " green check")
        index = index + 1
    
    # Checking for YELLOW
    index = 0
    for char in wordTemp:
        if guess.find(char) >= 0:
            guessScore[index] = "yellow"
            wordTemp = wordTemp[:index] + "_" + wordTemp[index + 1:]
            print(wordTemp + " yellow check")
        index = index+ 1

    index = 0
    for color in guessScore:
        if color == "white":
            guessScore[index] = "gray"
        index = index + 1
    return guessScore


# Startup code

if __name__ == "__main__":
    #wordle()
    TheWordle = choice(FIVE_LETTER_WORDS)
    print(TheWordle)
    print(colorCheck("phage", "gauge"))
