import time

creators = ["Maddie Tatum", "Erin Smith", " Kara Morgan", "Leah Sneed", "Krystal Bush", "Zachery Reynolds",
            "Joseph Mehne"]

ending_1 = "As you make your way up the stairs back to your room, the aroma of fresh pizza rolls fills you with joy."
ending_2 = "It has been a long and dangerous journey but you've made it and now celebrate your success with some " \
           "warm, well deserved pizza rolls. "
ending_3 = "The delicious pockets of sauce, meat, and cheese are like paradise wrapped in a blanket of crust."
ending_4 = "Your relatives tried to keep you from your pizza roll delights, but you bested them and came out " \
           "victorious. "
ending_5 = "Brave adventurer, I have only one thing to say to you...\n\n"
win_str = "You Win!\n\n"

win_texts = [ending_1, ending_2, ending_3, ending_4, ending_5, win_str]

ending_6 = "So we are here at the Game Over screen. You have failed young adventurer."
ending_7 = "You have not only let yourself down but your stomach as well."
ending_8 = "Are you filled with shame."
ending_9 = "Despair?"
ending_10 = "Hunger?"
ending_11 = "Return when you have trained harder."
lose_str = "YOU LOSE!\n\n"

lose_texts = [ending_6, ending_7, ending_8, ending_9, ending_10, ending_11, lose_str]

credits_b = "Oh, hey! Glad to see you're still here!"
credits_m = "I just wanted to let you know this was made by some of our sophomore computer science students and we " \
            "just wanted to recognize them!\n "
credits_e = "If you are interested in making things similar to this or making your own games then Fern Creek is the " \
            "perfect place for you! "
credits_ee = "We hope you enjoyed this game and are interested in joining the Fern Creek family, have a great day!"
par_stu_questions = "(If you have other questions, feel free to ask Mr. Tennyson)"

final_credits = [credits_b, credits_m, credits_e, credits_ee, par_stu_questions]


def name_lst(names):
    for i in names:
        new_name = i.center(197)
        print(new_name)
        time.sleep(1.5)


def roll_loss(lose):
    for text in lose:
        print(text.center(200))
        time.sleep(3)


def roll_win(win):
    for text in win:
        print(text.center(200))
        time.sleep(3)


def roll_credits(names):
    time.sleep(3.5)
    print(credits_b.center(200))
    time.sleep(1.5)
    print(credits_m.center(200))
    time.sleep(2)
    name_lst(names)
    print("\n" + credits_e.center(200))
    time.sleep(3.5)
    print(credits_ee.center(200))
    time.sleep(2)
    print("\n\n" + par_stu_questions.center(200))


roll_win(win_texts)
roll_credits(creators)


