#--------------------------------------------------------------------------------
# First task - work with non-nested list, second task - upgrade from non-nested list to nested list
#--------------------------------------------------------------------------------
relativesList = {"Denis": ("Sergey", "Alexander"), "Ivan": ("Alexander", "Efraim"), "Petya": ("Arseniy", "Vsevolod")}
name = "None"
while 1:
    name = input("Please, enter name of a person, whose father's (and grandfather's) name you want to know: ").capitalize()
    if name == "":
        print("Goodbye!")
        break
    elif name not in relativesList:
        print("Sorry, I don't know this person.")
    else:
        print("Father name: " + relativesList[name][0] + "\nGrandfather name: " + relativesList[name][1])
