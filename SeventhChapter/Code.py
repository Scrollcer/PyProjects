import sys, pickle, shelve


def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file


def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line


def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)

    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    value = next_line(the_file)
    explanation = next_line(the_file)


    return category, question, answers, correct, explanation, value


def welcome(title):
    """Welcome the player and get his/her name."""
    print("Welcome to the Trivia Challenge!\n")
    print("\t\t\t", title, "\n")


def main():
    trivia_file = open_file("mytrivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # get the first block
    category, question, answers, correct, explanation, value = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get an answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += int(value)
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        # get next block
        category, question, answers, correct, explanation, value = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print("You're final score is", score)
    name = input('Please, enter your name: ')
    scores = open("scores_file.txt", "a")
    scores.write(name + "\n")
    scores.write(str(score) + "\n")
    scores.close()
    print("\n\nCurrent score table:")

    scores = open("scores_file.txt", "r", encoding='utf-8')
    name = scores.readline().replace("\n", "")
    while name:
        score = scores.readline().replace("\n", "")
        print(name, ":", score)
        name = scores.readline().replace("\n", "")

    print("\nGoodbye!")


main()


input("\n\nPress the enter key to exit.")
