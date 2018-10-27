import time


def pizza_done():
    pass


def print_header():
    print("Let's get started...")
    for i in range(3):
        print("...".center(200))
        time.sleep(3)
        print("****** DRAMATIC LOADING SEQUENCE ******".center(200))

    print("\n\n\nWelcome to Pizza Roll Panic!!!")
    print(r'\\\\\\\\\\\********///////////' + '\n')
    time.sleep(1.5)


def intro_text(player="Default Person"):
    print(f'\nAre you ready, {player} ...\n')
    time.sleep(3)
    print('FOR THE GREATEST ADVENTURE OF YOUR LIFE?!?\n')
    time.sleep(3)

    print('In the midst of a FAMILY REUNION, swarming with RELATIVES, your tummy gets the rumblies that only pizza\n '
          'rolls can satisfy.\n')

    time.sleep(5)

    print('In order to survive your riveting plunge into the downstairs kitchen, you must talk with your chatty,\n '
          'nosy family members to pass the time while cooking your Tostinos...\n')

    time.sleep(5)

    print('Totinos?\n')
    time.sleep(2)
    print('Tortillas?\n')
    time.sleep(2)
    print('I have just been informed that it is in fact TOTINOS™ pizza rolls...\n')
    time.sleep(3)
    print('Blasphemy.\n')
    time.sleep(5)

    print(
        "Anywho... in order to complete your conquest of tiny pizza pockets, you must successfully cook your pizza\n "
        "rolls in the microwave. This means enduring SMALL TALK with your relatives before the time runs out. \n "
        "\nOtherwise, your chipper and overly social parents will force you to eat your Pizza Rolls™ in front of\n "
        "everyone!\n")
    time.sleep(8)
    print("OH, THE HUMANITY!\n")

    print(
        'You must navigate through this conversation combat and retreat back to the sweet (and savory) solitude of\n '
        'your bedroom.\n')
    time.sleep(5)
    print('DO YOU ACCEPT THE CHALLENGE?! (YES/NO): \n')
    get_acceptance(player)


def get_acceptance(player="Default Person"):
    p_choice = input()
    if p_choice.lower().strip()[0] == 'y':
        print(f"Here we go {player}...")
    elif p_choice.lower().strip()[0] == 'n':
        print(f"Well, {player}, you're doing this anyway.")
    else:
        print(f"No clue what you typed there {player}, no matter, here we go!")


def get_player():
    p_name = input("Please type your player name: ")
    if len(p_name) == 0:
        return "Default Person"
    else:
        return p_name


def intro_main():
    print_header()

    player_name = get_player()
    time.sleep(3)
    intro_text(player_name)


if __name__ == '__main__':
    intro_main()
