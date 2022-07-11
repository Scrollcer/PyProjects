import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")
print("You have 10 tries.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop
while guess != the_number:
    if tries > 10:
        print("You did not manage to guess in 10 tries. Game over.")
        break
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")

    guess = int(input("Take a guess: "))
    tries += 1

print("The thought number was", the_number)

input("\n\nPress the enter key to exit.")