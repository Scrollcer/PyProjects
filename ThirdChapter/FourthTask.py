import random
input("Hello, think of a number between 1 and 100, I will try to guess it.\nPress Enter when ready.")
currentGuess = random.randint(1, 100)
guessValue = 10
reverse = 0
while True:
    if guessValue == 0:
        guessValue = 1
    print("This number is", str(currentGuess)+"?")
    respond = input("Input y if right or h if higher or l if lower\n")
    if respond == "y":
        break
    elif respond == "h" and (reverse == 0 or reverse == "h"):
        currentGuess += guessValue
        reverse = "h"
    elif respond == "l" and (reverse == 0 or reverse == "l"):
        currentGuess -= guessValue
        reverse = "l"
    elif respond == "h" and reverse == "l":
        guessValue -= 5
        currentGuess += guessValue
        reverse = "h"
    elif respond == "l" and reverse == "h":
        guessValue -= 5
        currentGuess -= guessValue
        reverse = "l"
    else:
        print("Sorry, I don't understand, try again!")
print("Good game!")

