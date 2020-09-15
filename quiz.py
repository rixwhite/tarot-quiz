import random


def main():
    # Start the journey with a choice
    selection = main_menu()

    # Follow the path their choice leads them down
    # Get the lines from DeckMeaning.txt that match their choice
    deck = quiz_method(selection)

    # Now shuffle the deck
    random.shuffle(deck)

    # Start the quiz
    score = 0
    for card in deck:
        # We'll get a one or zero back from the quiz function.
        # Add it to the score tally
        score += quiz(card)

    # Variables for the math
    questions = len(deck)
    rate = score / questions * 100

    # Grade their quiz
    summary(score, questions, rate)


def summary(score, questions, rate):
    """
        Print out their grade
        Ask if they want another round
    """
    print("You got {0:d} out of {1:d} correct. {2:.1f}%"
          .format(score, questions, rate))
    again = valid_input("Would you like to go again? (yes/no) ",
                        ["yes", "no", 'y', 'n'])
    if again in ("YES", "Y"):
        main()
    else:
        print("Thanks for practicing!\nGood bye!")
        exit()


def main_menu():
    """
        Main menu
        The menuOptions can be edited to add to the menu. Just make sure you
        extend the elif statements in quiz_method to match anything you add here
    """
    header("Main Menu")
    menuOptions = ("Full deck", "Major Arcana", "Minor Aracana", "Court Cards"
                  ,"Minor Arcana and Court Cards", "Exit the game")
    for ordinal, option in enumerate(menuOptions, start=1):
        print(f"    {ordinal}) {option}")

    waiting = True
    while waiting:
        selection = valid_input("What would you like to do? ", "int")
        if 1 <= int(selection) <= len(menuOptions):
            waiting = False
        else:
            print("Choose an option by number.")
    return int(selection)


def quiz_method(option):
    """
        Reduce the deck per the user's choice
    """
    if option == 1:
        partialDeck = get_deck(["Major", "Minor", "Court"])
    elif option == 2:
        partialDeck = get_deck(["Major"])
    elif option == 3:
        partialDeck = get_deck(["Minor"])
    elif option == 4:
        partialDeck = get_deck(["Court"])
    elif option == 5:
        partialDeck = get_deck(["Minor", "Court"])
    elif option == 6:
        raise Exception("End Program")
    return partialDeck


def header(message):
    """ stars / message / stars """
    print('*' * 70)
    print("{0:^70}".format(message))
    print('*' * 70)


def quiz(card):
    """
        The heart of the program
        Tell them their card. Get their response. Score accordingly.
        There are also options for getting help and exiting the quiz.
    """
    print("Your card is #{0}: {1}.".format(card[0], card[1]))
    waiting = True
    while waiting:
        answer = input("What is its meaning? ")
        if answer.strip() == "exit":
            score = 0
            main()
        elif answer.strip() in card[-1]:
            print("Correct! {0} means {1}.".format(card[1], ", ".join(card[-1])))
            score = 1
            waiting = False
        else:
            print("Inorrect! {0} means {1}.".format(card[1], ", ".join(card[-1])))
            score = 0
            waiting = False
    return score


def valid_input(inputMessage, inputType):
    """
        Stay in a while loop until you get the type of input you want.
        The elif that deals with itterables converts everything to upper()
        for comparison.
    """
    waitingOnInput = True
    while waitingOnInput:
        # Integers
        if inputType == "int":
            try:
                output = int(input(inputMessage))
            except:
                print("Please enter an integer.")
            else:
                waitingOnInput = False
        # Floats
        elif inputType == "float":
            try:
                output = float(input(inputMessage))
            except:
                print("Please enter a number.")
            else:
                waitingOnInput = False
        # Itterables
        elif isinstance(inputType, (list, tuple, dict, set)):
            inputList = [item.upper() for item in inputType]
            output = input(inputMessage).upper()
            if output in inputList:
                waitingOnInput = False
            else:
                print("Please enter one of the following:", ', '.join(inputList))
        # Strings
        elif inputType == "string":
            output = input(inputMessage)
            waitingOnInput = False
        else:
            print("Something went wrong with valid_input()")
            output = "unknown"
            break
    return output


def get_deck(section):
    """
        Buld the deck based on the user's choice
        The section parameter expects a list
    """
    deck = []
    with open("DeckMeaning.txt", 'r') as inFile:
        for line in inFile:
            cardList = list(line.rstrip().split(" | "))
            if cardList[3] in section:
                card = [cardList[0], cardList[1], cardList[2], cardList[3],
                        cardList[5], list(cardList[4].split(", "))]
                deck.append(card)
    return deck


# Now that the header function has been read in, let's use it before we call
# main so that we can print something out before we get into the loop.
header("Get ready to learn tarot!")

# Now the main show
main()
