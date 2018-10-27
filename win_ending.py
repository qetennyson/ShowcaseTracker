import time

"""DESCRIPTION - As you make your way up the stairs back to your room, the aroma of fresh pizza rolls fills you with 
joy. It has been a long and dangerous journey, but you've made it and now celebrate your success with some warm, 
well deserved pizza rolls. The delicious pockets of sauce, meat, and cheese are like paradise wrapped in a blanket of 
crust. Your realtives tried to keep you from your pizza roll delights, but you bested them and came out victorious. 
Brave adventurer, i only have one thing to say to you... 

You Win!

Oh hey, glad to see you're still here. I just wanted to let you know this was made by some of our sophmore computer 
science students and we just wanted to recognize them!: *Maddie Tatum *Erin Smith *Kara Morgan *Leah Sneed *Krystal 
Bush *Zachery Renoylds *Joseph Mehne 

If you are at all interested in making things similar to this or making your own games by just your sophmore year of 
highschool then Fern Creek is the perfect place for you! We hope you enjoyed this game and are interested in joining 
the Fern Creek family, have a great day! 

(If you have other questions, feel free to ask Mr. Tennyson)"""

names = ["Maddie Tatum", "Erin Smith", " Kara Morgan", "Leah Sneed", "Krystal Bush", "Zachery Renoylds", "Joseph Mehne"]

ending_1 = "As you make your way up the stairs back to your room, the aroma of fresh pizza rolls fills you with joy."
ending_2 = "It has been a long and dangerous journey but you've made it and now celebrate your success with some " \
           "warm, well deserved pizza rolls. "
ending_3 = "The delicious pockets of sauce, meat, and cheese are like paradise wrapped in a blanket of crust."
ending_4 = "Your realtives tried to keep you from your pizza roll delights, but you bested them and came out " \
           "victorious. "
ending_5 = "Brave adventurer, i only have one thing to say to you...\n\n"
win_txt = "You Win!\n\n"

credits_b = "Oh, hey! Glad to see you're still here!"
credits_m = "I just wanted to let you know this was made by some of our sophmore computer science students and we " \
            "just wanted to recognize them!\n "
credits_e = "If you are interested in making things similar to this or making your own games by just your sophmore " \
            "year of highschool then Fern Creek is the perfect place for you! "
credits_ee = "We hope you enjoyed this game and are interested in joining the Fern Creek family, have a great day!"
par_stu_questions = "(If you have other questions, feel free to ask Mr. Tennyson)"


def name_lst():
    for i in names:
        new_name = i.center(197)
        print(new_name)
        time.sleep(1.5)


def game_ends():
    time.sleep(2)
    print(ending_1.center(200))
    time.sleep(3)
    print(ending_2.center(200))
    time.sleep(2.5)
    print(ending_3.center(200))
    time.sleep(2.5)
    print(ending_4.center(200))
    time.sleep(2.5)
    print(ending_5.center(200))
    time.sleep(2.5)
    print(win_txt.center(200))
    time.sleep(3.5)
    print(credits_b.center(200))
    time.sleep(1.5)
    print(credits_m.center(200))
    time.sleep(2)
    name_lst()
    print("\n" + credits_e.center(200))
    time.sleep(3.5)
    print(credits_ee.center(200))
    time.sleep(2)
    print("\n\n" + par_stu_questions.center(200))


game_ends()
# Message Input
#
#
# Message Quincy Tennyson, Zacharius_uwu, Maddie, Joseph, Kara, Lelu
