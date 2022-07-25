# Word Jumble
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("purple", "jumble", "easy", "difficult", "answer", "xylophone")

# pick one word randomly from the sequence
word = random.choice(WORDS)

# create a variable to uses later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble = ''
tip = ""
tipNumber = -1
score = 10
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
    """
                Welcome to Word Jumble!
        Unscramble the letters to make a word.
    (Press the enter key at the prompt to quit.)
    """
)
print("The jumble is:", jumble)

guess = input("Your guess?: ")

while guess != correct and guess != "":
    if guess == 'help':
        tipNumber += 1; score -= 1
        tip += correct[tipNumber]
        print("Word starts with following letters: " + tip)
    else:
        print("Sorry, that's not it.\n")
    guess = input("Your guess (input 'help' for a tip): ")
    guess = guess.lower()

if guess == correct:
    print("That's it! You guessed it!\n")
    print("Your score is ", + score)

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")