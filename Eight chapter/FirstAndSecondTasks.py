# Critter Caretaker
# A virtual pet to take care for

class Critter(object):
    """A virtual pet"""

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        return f"Name: {self.name}, Hunger value - {self.hunger}, Boredom value - {self.boredom}"

    def __pass_time(self, hunger=1, boredom=1):
        self.hunger += hunger
        self.boredom += boredom

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
        self.__pass_time()

    def eat(self, food=4):
        if food > 4:
            food = 4
        print("Brrruppp. Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time(boredom=(food-1), hunger = 0)

    def play(self, fun=4):
        if fun > 4:
            fun = 4
        print("Wheeee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time(hunger=(fun-1), boredom=0)


def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

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
            print("Goodbye.")

        # listen to your critter
        elif choice == "1":
            crit.talk()

        # feed your critter
        elif choice == "2":
            value = input(f"How much food would you wish to give to {crit_name}? ")
            crit.eat(int(value))

        # play with your critter
        elif choice == "3":
            value = input(f"How much time would you like to spend with {crit_name}? ")
            crit.play(int(value))

        # secret
        elif choice == "4":
            print(crit)

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")


main()
("\n\nPress the enter key to exit.")