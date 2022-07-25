# ---------------------------------------------------------------------
# First task
# ---------------------------------------------------------------------
import random

list = ["Apple", "Pineapple", "Cake", "Plugs"]
output = []
while len(output) != len(list):
    random_index = random.randrange(len(list))
    if list[random_index] not in output:
        output.append(list[random_index])
print(output)
# ---------------------------------------------------------------------
# Second task
# ---------------------------------------------------------------------
choice = 0; availablePoints = 30; check = 0
character = {"Strength": 0,"Health": 0, "Intelligence": 0, "Agility": 0 }
print("Welcome to character generator game.\nThere are 4 characteristics you need to distribute:\nStrength\nHealth"
      "\nIntelligence\nAgility")
while choice != str(5):
    print("Your current characteristics:")
    print(character)
    print("Current available points: " + str(availablePoints))
    choice = input("Menu:\n1-Edit Strength\n2-Edit Health\n3-Edit Intelligence\n4-Edit Agility\n5-Finish creation\nYour choice: ")
    if int(choice) == 1:
        value = input("Enter new value of strength: ")
        default = character["Strength"]
        character["Strength"] = value
        for i in character.values():
            check += int(i)
        if check > 30 or check < 0:
            print("Sorry you are off limits of 30 points, returning to previous value.")
            character["Strength"] = default
        else:
            print("Changed!")
            availablePoints = 30 - check
        check = 0
    elif int(choice) == 2:
        value = input("Enter new value of health: ")
        default = character["Health"]
        character["Health"] = value
        for i in character.values():
            check += int(i)
        if check > 30 or check < 0:
            print("Sorry you are off limits of 30 points, returning to previous value.")
            character["Health"] = default
        else:
            print("Changed!")
            availablePoints = 30 - check
        check = 0
    elif int(choice) == 3:
        value = input("Enter new value of intelligence: ")
        default = character["Intelligence"]
        character["Intelligence"] = value
        for i in character.values():
            check += int(i)
        if check > 30 or check < 0:
            print("Sorry you are off limits of 30 points, returning to previous value.")
            character["Intelligence"] = default
        else:
            print("Changed!")
            availablePoints = 30 - check
        check = 0
    elif int(choice) == 4:
        value = input("Enter new value of agility: ")
        default = character["Agility"]
        character["Agility"] = value
        for i in character.values():
            check += int(i)
        if check > 30 or check < 0:
            print("Sorry you are off limits of 30 points, returning to previous value.")
            character["Agility"] = default
        else:
            print("Changed!")
            availablePoints = 30 - check
        check = 0
print("Your final character:")
print (character)
