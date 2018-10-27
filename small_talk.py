import time

time_left = 90

relatives_proper = ['Aunt Kara', 'Uncle Joe', 'Granny Lelu', 'Grandpappy Aaron']

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
    'aunt_kara': " Hey sweetie, you got so big! I remember when you were a little baby. Oh, it makes me feel so old. How "
                 "is school?\n\n a. Awful\n b. Pretty good...\n c. Great, thanks for asking!\n d. *awkwardly avoid*\n",
    'uncle_joe': " What's up kid! It's been years since I've seen you. I really need to take you out to the lake, "
                 "it's a family tradition! How was summer camp?\n\n a. Fun! I got to go fishing\n b. I didn't go\n c. "
                 "Please go away\n d. *awkwardly avoid*\n",

    'granny_lelu': " Oh hello honey, they put me in charge of dessert this year. I tried something different: black "
                   "licorice, candy corn, raisins, and you see those colorful little bits on the top...sugar free Haribo "
                   "gummy bears. You wanna try some?\n\n a. I'll try a little of your dish later \n b. Um I don't think "
                   "I'll have room for dessert this year granny, sorry. \n c. I don't really care Granny. \n d. * "
                   "awkwardly avoid *",

    'grandpappy_aaron': " Hey whipper snapper! Either you're getting bigger or my eyes are getting even worse. At least my\n "
                        "eyes weren't this bad during the war! Speaking of which did I ever tell you about how I carried\n "
                        "five guys over enemy lines and destroyed a tank using nothing but a roll of toilet paper? I\n "
                        "almost blew my leg off too, that is when they could catch me! Though the war pays some good\n "
                        "money and will give you as much money as I have! In fact I think you should join the army,\n "
                        "teaches you some pretty good stuff and you'll only almost die two-thirds of the time! But then\n "
                        "again I was the best soldier out there so maybe you will be too. What'da say?\n\n a. Sounds "
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
        'outro_a': "\n*she's going to try to make you a slice, pray that your pizza rolls finish soon*\n",
        'outro_b': "\n*she's happy, just hope that she forgets about it before she leaves*\n",
        'outro_c': "\n*you don't know if she is confused or offended, either way, she's not happy*\n",
        'outro_d': "\n*you feel awful as she looks like she's about to cry, poor granny*\n",

    },
    'grandpappy_aaron': {
        'a': "Really? Never thought you were that interested in the army...doesn't seem like you either. What made you "
             "change? Ah nevermind, at least you're interested in it.\n",
        'b': "I'll send you some papers so you can read up on it! Glad I got you interested!\n",
        'c': "I know you don't like the military but you don't have to be so rude about it. Ah well, at least you're "
             "being honest, even if it harsh.\n",
        'd': "Hey I'm talking to you! Maybe you should join the army after all, it'll teach you some manners for once.",
        'outro_a': "\n*your response didn't effect him much, he walks off*\n",
        'outro_b': "\n*you seem to have made him overjoyed, he trots away to find his old uniforms*\n",
        'outro_c': "\n*he looks slightly disappointed and stumbles away, seemingly to find your brother*\n",
        'outro_d': "\n*your mom won't be happy about this, get ready to hear about this until Christmas*\n",

    },

}

time_factor = {
    'aunt_kara': {
        'a': 30,
        'b': 45,
        'c': 60,
        'd': 10,
    },
    'uncle_joe': {
        'a': 30,
        'b': 25,
        'c': 20,
        'd': 10,
    },
    'granny_lelu': {
        'a': 80,
        'b': 70,
        'c': 60,
        'd': 10,
    },
    'grandpappy_aaron': {
        'a': 65,
        'b': 70,
        'c': 60,
        'd': 10,
    }
}


def get_question(relative):
    return main_questions[relative]


def relative_intro(relative):
    time.sleep(1)

    print(f"\n {intros.get(relative)}")

    time.sleep(2)


def get_relative(relatives_available):
    while True:
        print("Who would you like to talk to?\n")

        for char in relatives_available:
            print(f"* {char}")

        print("\n")

        # Character choice menu
        choice = input("Type the name of the relative you'll speak to: ")
        try:
            if 'auntkara' in choice.lower().strip().replace(' ', ''):
                relatives_proper.remove('Aunt Kara')
                return 'aunt_kara'
            elif 'unclejoe' in choice.lower().strip().replace(' ', ''):
                relatives_proper.remove('Uncle Joe')
                return 'uncle_joe'
            elif 'grannylelu' in choice.lower().strip().replace(' ', ''):
                relatives_proper.remove('Granny Lelu')
                return 'granny_lelu'
            elif 'grandpappyaaron' in choice.lower().strip().replace(' ', '') or \
                    'grandpapyaaron' in choice.lower().strip().replace(' ', ''):
                relatives_proper.remove('Grandpappy Aaron')
                return 'grandpappy_aaron'
            else:
                print("Invalid entry... make sure you spelled it right!")
        except ValueError:
            print(f"\n{choice.title()} has already walked away, choose someone else.\n")


def get_answer_responses(relative, answer):
    time.sleep(1)

    relative_response = responses[relative]
    print(relative_response[answer])

    time.sleep(2)

    # outros based on a,b,c or d response.
    print(relative_response[f'outro_{answer}'])

    return get_time(answer, relative)


def get_time(answer, relative):
    relative_time = time_factor[relative]
    return relative_time[answer]


def get_user_answer():
    while True:
        answer = input("\nEnter your answer - a, b, c, or d: ")
        if answer.lower().strip()[0] in ['a', 'b', 'c', 'd']:
            return answer
        else:
            print("Please answer with a, b, c, or d.")


def pizza_main():
    global time_left
    while time_left > 0:

        # Clean the choice string from the player and add the underscore for key search

        current_relative = get_relative(relatives_proper)

        # Display the corresponding relative "intro"

        relative_intro(current_relative)

        # Display the corresponding relative "question"

        print(get_question(current_relative))

        # Gets relative response and outro based on question, and increments time based on response.

        user_answer = get_user_answer()

        get_answer_responses(current_relative, user_answer)

        time_left -= get_time(user_answer, current_relative)

        if time_left <= 0:
            # TODO: win game
            break
        elif len(relatives_proper):
            # TODO: lose game
            pass


if __name__ == '__main__':
    pizza_main()
