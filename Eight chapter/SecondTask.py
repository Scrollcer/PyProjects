class AllTVs(object):
    def __init__(self, name, volume=0, channel=1):
        self.__volume = volume
        self.__channel = channel
        self.__type = name
        print(f"Congratulations, you acquired new TV type: {name}")

    def __str__(self):
        return f"TV type: {self.__type}\nCurrent channel: {self.__channel}\nCurrent volume: {self.__volume}"

    @property
    def volume(self):
        return self.volume

    @volume.setter
    def volume(self, value):
        if value > 100:
            print("Max volume - 100, neighbors would be mad otherwise!")
            self.__volume = 100
        elif value < 0:
            print("You can't have volume value less than 0!")
            self.__volume = 0
        else:
            self.__volume = value
        print(f"New volume value: {self.__volume}")

    @property
    def channel(self):
        return self.channel

    @channel.setter
    def channel(self, value):
        if value > 50:
            print("Sorry, we have only 50 channels.")
            self.__channel = 50
        elif value < 0:
            print("There are no channels with 0 or negative numbers!")
            self.__channel = 0
        else:
            self.__channel = value

        print(f"Current channel: {self.__channel}")


def main():
    type = input("What TV type do you wish to have? ")
    tv = AllTVs(type)
    answer = " "
    while 1:
        print("""
            Menu:
            1 - Turn off TV
            2 - Change volume
            3 - Change channel
            4 - Show current volume and channel
            """)
        answer = input("Your choice: ")
        if answer == "1":
            break
        elif answer == "2":
            volume = input("Please, enter new value: ")
            tv.volume = int(volume)
        elif answer == "3":
            channel = input("Please, enter new channel: ")
            tv.channel = int(channel)
        elif answer == "4":
            print(tv)
        else:
            print(f"Sorry, I don't know {answer} command.")

    print("Have a nice day!")

main()
