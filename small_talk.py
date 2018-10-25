import time

time_left = 300

time_stats = {
    'aunt_kara': 60,
    'uncle joe': 30,
    'granny lelu': 90,
    'grandpappy aaron': 70,
}

# Relative Intros
intros = {
    'aunt_kara': "you hear a squeal, like a deflating balloon, as your aunt hugs you from behind, almost crushing you "
                 "with *the force*\n",
    'uncle_joe': "\n*you make eye contact and Uncle Joe roams towards you and the microwave*\n",
    'granny_lelu': "\n*a warm smile consumes her face as she scoots towards the microwave in her bunny slippers*\n",
    'grandpappy_aaron': "\n*he hobbles over to you and sits in the broken bar stool*\n",
}

# Main questions from Relatives
main_questions = {
    'aunt_kara': "Hey sweetie, you got so big! I remember when you were a little baby. Oh, it makes me feel so old. How "
                 "is school?\n a. Awful\n b. Pretty good...\n c. Great, thanks for asking!\n d. *awkwardly avoid*\n",
    'uncle_joe': "What's up kid! It's been years since I've seen you. I really need to take you out to the lake, "
                 "it's a family tradition! How was summer camp?\n a. Fun! I got to go fishing\n b. I didn't go\n c. "
                 "Please go away\n d. *awkwardly avoid*\n",

    'granny_lelu': "Oh hello honey, they put me in charge of dessert this year. I tried something different: black "
                   "licorice, candy corn, raisins, and you see those colorful little bits on the top...sugar free Haribo "
                   "gummy bears. You wanna try some?\n a. I'll try a little of your dish later \n b. Um I don't think "
                   "I'll have room for dessert this year granny, sorry. \n c.I don't really care Granny. \n d. * "
                   "awkwardly avoid *",

    'grandpappy_aaron': "Hey whipper snapper! Either you're getting bigger or my eyes are getting even worse. At least my "
                        "eyes weren't this bad during the war! Speaking of which did I ever tell you about how I carried "
                        "five guys over enemy lines and destroyed a tank using nothing but a roll of toilet paper? I "
                        "almost blew my leg off too, that is when they could catch me! Though the war pays some good "
                        "money and will give you as much money as I have! In fact I think you should join the army, "
                        "teaches you some pretty good stuff and you'll only almost die two-thirds of the time! But then "
                        "again I was the best soldier out there so maybe you will be too. What'da say?\n a. Sounds "
                        "interesting, I'll gladly check it out! \n b. I wasn't thinking about it about it but I'll see. "
                        "\n c. I think I'll hide in my room instead. \n d. * awkwardly avoid *",
}

# TODO: What is this?
answers = {
    'aunt_kara': 'c',
    'uncle_joe': 'a',
    'granny_lelu': 'a',
    'grandpappy_aaron': 'b',
}

# Relative responses based on player answers.
responses = {
    'aunt_kara': {
        'a': "Aw, that's too bad, I hope everything turns out alright. I'm sure things will be fine.\n",
        'b': "Whats with the hesitation. Are you failing your classes? Are you making plenty of friends?\n",
        'c': "Good! Nice to see you're doing well. I remember you going to your first day of Kindergarten!\n",
        'd': "Is school really that bad? No need to be rude\n",
        'outro_a': "*Sees Karen at the cookies and runs to stop her from taking all the gluten-free oatmeal raisin "
                   "cookies*\n",
        'outro_b': "*Walks away to talk to your Mom about how your doing in school*\n",
        'outro_c': "*Walks away scrolling through your 'Back To School' pictures on Facebook*\n",
        'outro_d': "*Walks away in a passive aggressive stride to go talk to your Mother*\n",
    },
    'uncle_joe': {
        'a': "That's great kiddo! I used to love fishing. I would live on the lake if it weren't for that darn knee "
             "replacement. Well, I'm gonna find your sister, nice to chat with you!\n",
        'b': "Oh, well that's too bad. I bet you still had a blast of a summer. Nice to see you champ.\n",
        'c': "Aw come on, what's the matter? I guess if you want me to go that badly, I will. Still nice to see you "
             "kiddo.\n",
        'd': "Not much of a talker? You never were, no need to be rude though.\n",
        'outro_a': "*he hops away*\n",
        'outro_b': "*he leaves*\n",
        'outro_c': "*he slumps into the living room*\n",
        'outro_d': "*he stomps away angrily*\n",

    },
    'granny_lelu': {
        'a': "No, Sweetie you should try it right now so I can get your opinion on it.\n",
        'b': "Oh it's okay darling I'll save some for you in the fridge.\n",
        'c': "*Awkward* Um alright I'll see you later *walks away*\n",
        'd': "Hey! I'm talking to you please listen. You know I'm not gonna be around for long you better lighten up.\n",
        'outro_a': "",
        'outro_b': "",
        'outro_c': "",
        'outro_d': "",

    },
    'grandpappy_aaron': {
        'a': "Really? Never thought you were that interested in the army...doesn't seem like you either. What made you "
             "change? Ah nevermind, at least you're interested in it.\n",
        'b': "I'll send you some papers so you can read up on it! Glad I got you interested!\n",
        'c': "I know you don't like the military but you don't have to be so rude about it. Ah well, at least you're "
             "being honest, even if it harsh.\n",
        'd': "Hey I'm talking to you! Maybe you should join the army after all, it'll teach you some manners for once.",
        'outro_a': "",
        'outro_b': "",
        'outro_c': "",
        'outro_d': "",

    },

}

time_factor = {
    'aunt_kara': {
        'a':30,
        'b':45,
        'c':60,
        'd':10,
    },
    'uncle_joe': {
        'a':30,
        'b':25,
        'c':20,
        'd':10,
    },
    'granny_lelu':{
        'a':90,
        'b':85,
        'c':70,
        'd':85,
    },
    'grandpappy_aaron':{
        'a':65,
        'b':70,
        'c':60,
        'd':55,
    }
}


def get_question(relative):
    return main_questions[relative]


def relative_intro(relative):
    time.sleep(1)

    print(f"\n {intros.get(relative)}")

    time.sleep(2)


def get_player_answer(relative, answer):
    time.sleep(1)

    relative_response = responses[relative]
    print(relative_response[answer])

    time.sleep(2)

    print(relative_response[f'outro_{answer}'])

    return get_time(answer, relative)


def get_time(answer, relative):
    relative_time = time_factor[relative]
    return relative_time[answer]


choice = input("Who would you like to talk to, Uncle Joe, Aunt Kara, Grandpappy Aaron, or Granny Lelu? ")

# TODO: refactor for error handling
# Clean the choice string from the player and add the underscore for key search

current_relative = choice.lower().strip().replace(' ', '_')

# Display the corresponding relative "intro"

relative_intro(current_relative)

# Display the corresponding relative "question"

print(get_question(current_relative))

# TODO: refactor for error handling
user_answer = input()

# Gets relative response and outro based on question, and increments time based on response.

get_player_answer(current_relative, user_answer)


#     if answer == 'a':
#         time.sleep(1)
#         print("That's great kiddo! I used to love fishing. I would live on the lake if it weren't for that darn knee "
#               "replacement. Well, I'm gonna find your sister, nice to chat with you!\n")
#         time.sleep(2)
#         print("*he hops away*\n")
#         seconds += 30
#     elif answer == 'b':
#         time.sleep(1)
#         print("Oh, well that's too bad. I bet you still had a blast of a summer. Nice to see you champ.\n")
#         time.sleep(2)
#         print("*he leaves*\n")
#         seconds += 25
#     elif answer == 'c':
#         time.sleep(1)
#         print("Aw come on, what's the matter? I guess if you want me to go that badly, I will. Still nice to see you "
#               "kiddo.\n")
#         time.sleep(2)
#         print("*he slumps into the living room*\n")
#         seconds += 20
#     elif answer == 'd':
#         time.sleep(1)
#         print("Not much of a talker? You never were, no need to be rude though.\n")
#         time.sleep(2)
#         print("*he stomps away angrily*\n")
#         seconds += 10
# elif choice.lower() == 'aunt kara':
#     time.sleep(1)
#     print("\n*you hear a squeal, like a deflating balloon, as your aunt hugs you from behind, almost crushing you with "
#           "the force*\n")
#     time.sleep(2)
#     answer = input(small_talk('Aunt_Kara'))
#     if answer == 'a':
#         time.sleep(1)
#         print("Aw, that's too bad, I hope everything turns out alright. I'm sure things will be fine.\n")
#         time.sleep(2)
#         print(
#             "*Sees Karen at the cookies and runs to stop her from taking all the gluten-free oatmeal raisin cookies*\n")
#         seconds += 30
#     elif answer == 'b':
#         time.sleep(1)
#         print("Whats with the hesitation. Are you failing your classes? Are you making plenty of friends?\n")
#         time.sleep(2)
#         print("*Walks away to talk to your Mom about how your doing in school*\n")
#         seconds += 45
#     elif answer == 'c':
#         time.sleep(1)
#         print("Good! Nice to see you're doing well. I remember you going to your first day of Kindergarten!\n")
#         time.sleep(2)
#         print("*Walks away scrolling through your 'Back To School' pictures on Facebook*\n")
#         seconds += 60
#     elif answer == 'd':
#         time.sleep(1)
#         print("Is school really that bad? No need to be rude\n")
#         time.sleep(2)
#         print("*Walks away in a passive aggressive stride to go talk to your Mother*\n")
#         seconds += 10
# elif choice.lower() == 'grandpappy aaron':
#     time.sleep(1)
#     print("\n*he hobbles over to you and sits in the broken bar stool*\n")
#     time.sleep(2)
#     answer = input(small_talk('Grandpappy Aaron'))
#     if answer == 'a':
#         time.sleep(1)
#         print(
#             "Really? Never thought you were that interested in the army...doesn't seem like you either. What made you "
#             "change? Ah nevermind, at least you're interested in it.")
#         seconds += 65
#     elif answer == 'b':
#         time.sleep(1)
#         print("I'll send you some papers so you can read up on it! Glad I got you interesred!")
#         seconds += 70
#     elif answer == 'c':
#         time.sleep(1)
#         print("I know you don't like the military but you don't have to be so rude about it. Ah well, at least you're "
#               "being honest, even if it harsh.")
#         seconds += 60
#     elif answer == 'd':
#         time.sleep(1)
#         print(
#             "Hey I'm talking to you! Maybe you should join the army after all, it'll teach you some manners for once.")
#         seconds += 55
# elif choice.lower() == 'granny lelu':
#     time.sleep(1)
#     print("\n*a warm smile consumes her face as she scoots towards the microwave in her bunny slippers*\n")
#     time.sleep(2)
#     answer = input(small_talk('Granny Lelu'))
#     if answer == 'a':
#         time.sleep(1)
#         print("No, Sweetie you should try it right now so I can get your opinion on it.")
#         time.sleep(2)
#         print("")
#         seconds += 90
#     elif answer == 'b':
#         time.sleep(1)
#         print("Oh it's okay darling I'll save some for you in the fridge.")
#         seconds += 85
#     elif answer == 'c':
#         time.sleep(1)
#         print("*Akward* Um alright I'll see you later *walks away*")
#         seconds += 80
#     elif answer == 'd':
#         time.sleep(1)
#         print("Hey! I'm talking to you please listen. You know I'm not gonna be around for long you better lighten up.")
#         seconds += 75
