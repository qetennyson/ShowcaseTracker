import time

start_1 = "In the process of your gaming session filled with joy and entertainment your stomach begins to rumble like " \
          "the thousand thunders of Zeus himself! \n "
start_2 = "Adorning your armor (a thrasher hoodie... for shame... you don't even skate!) \n"
start_3 = "poser... \n"
start_4 = "You swiftly but quietly begin your descent down the stairs as you say a silent prayer that you make it out " \
          "alive. \n "
start_5 = "A cacophony of noises erupt from the downstairs living room and kitchen alike. \n"
start_6 = "Fear strikes you to the core, but you proceed on. Your hunger is far too strong to be vanquished by a " \
          "mortal fear like mere socializing. \n "
start_7 = "Reaching the ground floor of your house the microwave is in sight. \n"
start_8 = "You make a mad dash for the freezer and all but throw open the door.\n"
start_9 = "Grabbing your bounty you toss the PIZZA ROLLS™ on the plate and gently escort them to the " \
          "microwave."
start_10 = "Then... \n"
start_11 = "You begin your approach. \n"
dir_1 = "*** DIRECTIONS *** \n"
dir_2 = "In this game you must approach your various relatives in order to pass the time on the microwave for your " \
           "pizza rolls. \n "
dir_3 = "Failure to pass the time will lead to a game over with your parents forcing you to stay downstairs and " \
           "eat your pizza rolls in front of everyone. \n "
dir_4 = "As well as the overhanging feelings of eternal shame. \n"
dir_5 = "Have fun! ~ FCHS Computer Science"
lst = [start_1, start_2, start_3, start_4, start_5, start_6, start_7, start_8, start_9, start_10, start_11, dir_1,
       dir_2, dir_3, dir_4, dir_5]


def begin_main():
    for text in lst[0:10]:
        print(text.center(225))
        time.sleep(3)
    for dir in lst[11:]:
        print(dir.center(225))
        time.sleep(5)


if __name__ == '__main__':
    begin_main()
