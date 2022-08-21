# Critter Caretaker
# A virtual pet to take care for
import random

class Critter(object):
    """A virtual pet"""

    def __init__(self, name):
        hunger = random.randint(0, 4)
        boredom = random.randint(0, 4)
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        return str(self.name)

    def getvalues(self):
        print(f"Name: {self.name}, Hunger value - {self.hunger}, Boredom value - {self.boredom}")

    def pass_time(self, hunger=1, boredom=1):
        self.hunger += hunger
        self.boredom += boredom
        if self.hunger > 4:
            self.hunger = 4
        if self.boredom > 4:
            self.boredom = 4

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = 'happy'
        elif 5 <= unhappiness <= 10:
            m = 'okay'
        elif 11 <= unhappiness <= 15:
            m = 'frustrated'
        else:
            m = 'mad'
        return m

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.pass_time()

    def eat(self, food=4):
        if food > 4:
            food = 4
        print("Brrruppp. Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.pass_time(boredom=(food-1), hunger=0)

    def play(self, fun=4):
        if fun > 4:
            fun = 4
        print("Wheeee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.pass_time(hunger=(fun-1), boredom=0)

def crittercaretaker(maincrit, secondcrit, thirdcrit):
    choice = None
    while choice != '0':
        print("""
        Critter Caretaker

        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Returning to all critters.")

        # listen to your critter
        elif choice == "1":
            maincrit.talk()
            secondcrit.pass_time()
            thirdcrit.pass_time()

        # feed your critter
        elif choice == "2":
            value = input(f"How much food would you wish to give to {maincrit.name}? ")
            maincrit.eat(int(value))
            secondcrit.pass_time()
            thirdcrit.pass_time()

        # play with your critter
        elif choice == "3":
            value = input(f"How much time would you like to spend with {maincrit.name}? ")
            maincrit.play(int(value))
            secondcrit.pass_time()
            thirdcrit.pass_time()
        # secret
        elif choice == "4":
            maincrit.getvalues()

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

def main():
    firstcritter = Critter("Pig"); secondcritter = Critter("Goat"); thirdcritter = Critter("Horse")
    list = [firstcritter, secondcritter, thirdcritter]
    print(f"You have these critters: {list[0]}, {list[1]}, {list[2]}")
    choice = None
    while choice != '0':
        print("""
        With which critter would you like to spend time?

        0 - Quit
        1 - Pig
        2 - Goat
        3 - Horse
        """)

        choice = input("Choice: ")
        print()

        if choice == "0":
            print("Goodbye.")
        elif choice == "1":
            crittercaretaker(list[0], list[1], list[2])
        elif choice == "2":
            crittercaretaker(list[1], list[0], list[2])
        elif choice == "3":
            crittercaretaker(list[2], list[0], list[1])

main()