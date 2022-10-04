# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
import enchant
from random import choice
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
d = enchant.Dict("en_US")


def wordle(word):

    def enter_action(guess):
        if d.check(guess) or guess == word: # This line is here because when the system chose COOEY as a word, the Enchant package didn't think it was one.
            result = colorCheck(word, guess)
            gw.show_message("Nice guess" + " " + result[0] + " " + guess)
        else:
            gw.show_message("Not a valid word")

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
    for char in guess:
        if wordTemp.find(char) >= 0:
            guessScore[index] = "yellow"
            wordTemp = wordTemp[:index] + "_" + wordTemp[index + 1:]
            print(wordTemp + " yellow check")
        index = index + 1

    # Checking for GRAY
    index = 0
    for color in guessScore:
        if color == "white":
            guessScore[index] = "gray"
        index = index + 1
    return guessScore


# Startup code

if __name__ == "__main__":
    TheWordle = choice(FIVE_LETTER_WORDS)
    wordle(TheWordle.upper())
    
    print(TheWordle)
    # print(colorCheck("phage", "scoff"))
