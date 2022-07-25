import random
WORDS = ("apple", "pancake", "python", "backend", "frontend", "pineapple")
correct = random.choice(WORDS)
guess = ""
count = 0
wordInCorrect = 0

print("I think of a word with " + str(len(correct)) + " words, try to guess it!")
for i in range(5):
    print("You have " + str(5 - i) + " tries remaining to guess correct letters before guessing word.")
    guess = input("Try to guess a letter: ").lower()
    for j in correct:
        if correct[count] == guess:
            wordInCorrect = 1
        else:
            count += 1
    if wordInCorrect == 0:
        print("There are no such letters in a guessable word.\n")
    else:
        print("Yes, you can find this letter in a guessable word.\n")
    count = 0; wordInCorrect = 0;
finalGuess = input("So, your guess of a word is: ")
if finalGuess == correct:
    print("Congratulations, you guessed correctly!\n")
else:
    print("Sorry, the right word was " + correct + "\n")
print("Thank you for playing!")