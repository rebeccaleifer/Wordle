correctWord = "slass"
guessedWord = "sassy"
colors = ["gray", "gray", "gray", "gray", "gray"]

for letter in range(0, len(guessedWord)):
    guessLetter = guessedWord[letter]
    correctLetter = correctWord[letter]
    if(guessLetter == correctLetter):
        colors[letter] = "green"
    elif(correctWord.count(guessLetter) > 0):
        colors[letter] = "yellow"

    if((guessedWord.count(guessLetter) > correctWord.count(guessLetter)) and colors[letter] != "green"):
        for check in range(0, letter):
            if (guessedWord[check] == guessedWord[letter] and colors[check] != "green"):
                colors[letter] = "gray"

print(colors)
