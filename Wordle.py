# File: Wordle.py

"""
IS405 Project 4 
Group 5: Rebecca Leifer, Brayden Buhler, YunChen Lee, Levi Morse, Ransom Allphin


"""

import random
from random import choice
from WordleDictionary import FIVE_LETTER_WORDS

from WordleGraphics import WordleGWindow, N_COLS, N_ROWS


def wordle(word):
    
    def enter_action(guess):
        
        if guess.lower() in FIVE_LETTER_WORDS:
            colorCheck(word, guess)
            gw.show_message("Guess: " + guess + " Correct Word: " + word)
        else:
            gw.show_message("Not a valid word")

    gw = WordleGWindow()
    gw.show_message("Correct word: " + word)
    gw.add_enter_listener(enter_action)

    def colorCheck(word, guess):
        row = gw.get_current_row()
        print(gw.get_square_color(row, 0))
        wordTemp = word
        index = 0
        # Checking for GREEN
        for char in wordTemp:
            gw.set_square_letter(row, index, guess[index])
            if char == guess[index]:
                wordTemp = wordTemp[:index] + "_" + wordTemp[index + 1:]
                guess = guess[:index] + "*" + guess[index + 1:]
                print(wordTemp + " green check")
                gw.set_square_color(row, index, CORRECT_COLOR)
                gw.set_key_color(char, CORRECT_COLOR)
                
            index = index + 1
        
        # Checking for YELLOW
        index = 0
        for char in guess:
            if char != "*":
                if wordTemp.find(guess[index]) >= 0:
                    wordTemp = wordTemp[:wordTemp.find(char)] + "_" + wordTemp[wordTemp.find(char) + 1:]
                    gw.set_square_color(row, index, PRESENT_COLOR)
                    if gw.get_key_color(guess[index]) != CORRECT_COLOR:
                        gw.set_key_color(guess[index], PRESENT_COLOR) 
                    print(wordTemp + " yellow check")
                elif gw.get_key_color(guess[index]) != CORRECT_COLOR and gw.get_key_color(guess[index]) != PRESENT_COLOR:
                    gw.set_key_color(guess[index], MISSING_COLOR)
            index = index + 1

        # Checking for GRAY
        index = 0
        columns = 5
        currentColumn = 0
        while currentColumn < columns:
            if gw.get_square_color(row, currentColumn) == UNKNOWN_COLOR:
                gw.set_square_color(row, currentColumn, MISSING_COLOR)
            index = index + 1
            currentColumn = currentColumn + 1
        print("Current Row: ", gw.get_current_row())
        if gw.get_current_row() < 5:
            gw.set_current_row(row + 1)

        print("Next Row: ", gw.get_current_row())
            
        


# Startup code

if __name__ == "__main__":
    TheWordle = choice(FIVE_LETTER_WORDS)
    # TheWordle = "SACKS"
    wordle(TheWordle.upper())
    
