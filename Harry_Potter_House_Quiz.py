import os
import time
from time import sleep
from colorama import Fore, Style
from termcolor import colored
import sys


class color:
    BOLD = '\033[1m'
    END = '\033[0m'


Gryffindor = 0
Slytherin = 0
Hufflepuff = 0
Ravenclaw = 0


def screen_cls():
    pass

os.system('cls')

for x in colored(
        "Imagine you get selected in Hogwarts house of magic. So what house you will get there?🤔 \n\n\nThis quiz will tell you a little probability of the house that you can get in Hogwarts.",
        "red"):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.05)

os.system('cls')

my_str = f"WELCOME TO THE HARRY POTTER HOGWARTS HOUSE QUIZ.\n\n\nEvery house of Hogwarts has it's own speciality and the sorting hat try to put students accordingly to the house that's best for them, {Fore.RED}Gryffindor?{Style.RESET_ALL}, {Fore.GREEN}Slytherin?{Style.RESET_ALL}, {Fore.YELLOW}Hufflepuff?{Style.RESET_ALL}, OR {Fore.BLUE} Ravenclaw?{Style.RESET_ALL}."

print(my_str)

time.sleep(8)

os.system('cls')

for x in colored(
        "So, without wasting much time, let's get started, for this exciting journey......",
        "green"):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.05)

os.system('cls')


def first_part():
    global Gryffindor
    global Slytherin
    global Hufflepuff
    global Ravenclaw

    Ques_1 = f"{Fore.CYAN}Q1. Which of the following traits describes you the most?{Style.RESET_ALL}\n\n\n1. Ambitious, cunning, self-confident, goal-oriented and leadership\n\n2. Loyal, humble, honest, justice, true, fair and kind \n\n3. Brave, courageous, daring, athletic and adventurous \n\n4. Wise, Wisdom, wit, Intelligent, curious and creative"

    print(Ques_1)

    print(colored("\n\nChoose one option", "magenta"))

    choice1 = input()
    print()

    if choice1 == "1":
        Slytherin += 3
        os.system('cls')
        second_part()

    elif choice1 == "2":
        Hufflepuff += 3
        os.system('cls')
        second_part()

    elif choice1 == "3":
        Gryffindor += 3
        os.system('cls')
        second_part()

    elif choice1 == "4":
        Ravenclaw += 3
        os.system('cls')
        second_part()

    else:
        wrong1 = f"{Fore.RED}Oops! Wrong option, try again{Style.RESET_ALL}"
        print(wrong1)
        time.sleep(1)
        os.system('cls')
        first_part()


def second_part():
    global Gryffindor
    global Slytherin
    global Hufflepuff
    global Ravenclaw

    Ques_2 = f"{Fore.CYAN}Q2. If you could have any power, which would you choose?{Style.RESET_ALL} \n\n\n1. The power to read minds \n\n2. The power of invisibility \n\n3. The power of superhuman strength \n\n4. The power to change the past"

    print(Ques_2)

    print(colored("\n\nChoose one option", "magenta"))

    choice2 = input()
    print()

    if choice2 == "1":
        Ravenclaw += 2
        os.system('cls')
        third_part()

    elif choice2 == "2":
        Gryffindor += 2
        os.system('cls')
        third_part()

    elif choice2 == "3":
        Hufflepuff += 2
        os.system('cls')
        third_part()

    elif choice2 == "4":
        Slytherin += 2
        os.system('cls')
        third_part()

    else:
        wrong2 = f"{Fore.RED}Oops! Wrong option, try again{Style.RESET_ALL}"
        print(wrong2)
        time.sleep(1)
        os.system('cls')
        second_part()


def third_part():
    global Gryffindor
    global Slytherin
    global Hufflepuff
    global Ravenclaw

    Ques_3 = f"{Fore.CYAN}Q3. Which of the weakness describes you the worst?{Style.RESET_ALL}\n\n\n1. You are Naivety i.e. You believe on others very easily.Which means you can easily be tricked and taken advantage of. \n\n2. You are Short Tempered i.e. you get angry on small things \n\n3. You tend to live inside their own heads and stay disconnect with the outside world. Which is inappropriate in certain situations. \n\n4. You are a power Hunger and want to achieve your goal. In this tend you often try to do things without caring the principles of right and wrong behavior."

    print(Ques_3)

    print(colored("\n\nChoose one option", "magenta"))

    choice3 = input()
    print()

    if choice3 == "1":
        Hufflepuff += 2
        os.system('cls')
        fourth_part()

    elif choice3 == "2":
        Gryffindor += 2
        os.system('cls')
        fourth_part()

    elif choice3 == "3":
        Ravenclaw += 2
        os.system('cls')
        fourth_part()

    elif choice3 == "4":
        Slytherin += 2
        os.system('cls')
        fourth_part()

    else:
        wrong3 = f"{Fore.RED}Oops! Wrong option, try again{Style.RESET_ALL}"
        print(wrong3)
        time.sleep(1)
        os.system('cls')
        third_part()


def fourth_part():
    global Gryffindor
    global Slytherin
    global Hufflepuff
    global Ravenclaw

    Ques_4 = f"{Fore.CYAN}Q4. Your vacation from Hogwarts are going and it's your free time. What you would like to do in this free time?{Style.RESET_ALL}\n\n\n1. Sports or any physical activity to stay fit \n\n2. Time is precious and you intend to get the best use out of it \n\n3. Reading anything from heart, whether it's a fantasy novel, a magzine or any other type of book or even learning something new \n\n4. Watching TV on the couch or playing video games with friends"

    print(Ques_4)

    print(colored("\n\nChoose one option", "magenta"))

    choice4 = input()
    print()

    if choice4 == "1":
        Gryffindor += 2
        os.system('cls')
        fifth_part()

    elif choice4 == "2":
        Slytherin += 2
        os.system('cls')
        fifth_part()

    elif choice4 == "3":
        Ravenclaw += 2
        os.system('cls')
        fifth_part()

    elif choice4 == "4":
        Hufflepuff += 2
        os.system('cls')
        fifth_part()

    else:
        wrong4 = f"{Fore.RED}Oops! Wrong option, try again{Style.RESET_ALL}"
        print(wrong4)
        time.sleep(1)
        os.system('cls')
        fourth_part()


def fifth_part():
    global Gryffindor
    global Slytherin
    global Hufflepuff
    global Ravenclaw

    Ques5 = f"{Fore.CYAN}Q5. Again it's your free time and you are at Hogwarts. You want to go outside to spend some time, So where would you go? {Style.RESET_ALL}\n\n\n1. Kitchen \n\n2. Room of requirements \n\n3. Forbidden forest \n\n4. Library"

    print(Ques5)

    print(colored("\n\nChoose one option", "magenta"))

    choice5 = input()
    print()

    if choice5 == "1":
        Hufflepuff += 2
        os.system('cls')
        sixth_part()

    elif choice5 == "2":
        Gryffindor += 2
        os.system('cls')
        sixth_part()

    elif choice5 == "3":
        Slytherin += 2
        os.system('cls')
        sixth_part()

    elif choice5 == "4":
        Ravenclaw += 2
        os.system('cls')
        sixth_part()

    else:
        wrong5 = f"{Fore.RED}Oops! Wrong option, try again{Style.RESET_ALL}"
        print(wrong5)
        time.sleep(1)
        os.system('cls')
        fifth_part()


def sixth_part():
    global Gryffindor
    global Slytherin
    global Hufflepuff
    global Ravenclaw

    Ques6 = f"{Fore.CYAN}Q6. Which nightmare would frighten you most? {Style.RESET_ALL}\n\n\n1. Waking up to find that neither your friends nor your family have any idea who you are \n\n2. An eye at the keyhole of a dark windowless room in which you are locked \n\n3. Standing on top of something very high and realizing suddenly that there are no hand-or-footholds, nor any barrier to stop you falling \n\n4. Being forced to speak in such silly voice that hardy anyone can understand you, and everyone laughs at you"

    print(Ques6)

    print(colored("\n\nChoose one option", "magenta"))

    choice6 = input()
    print()

    if choice6 == "1":
        Hufflepuff += 2
        os.system('cls')
        seventh_part()

    elif choice6 == "2":
        Gryffindor += 2
        os.system('cls')
        seventh_part()

    elif choice6 == "3":
        Ravenclaw += 2
        os.system('cls')
        seventh_part()

    elif choice6 == "4":
        Slytherin += 2
        os.system('cls')
        seventh_part

    else:
        wrong6 = f"{Fore.RED}Oops! Wrong option, try again{Style.RESET_ALL}"
        print(wrong6)
        time.sleep(1)
        os.system('cls')
        sixth_part()


def seventh_part():
    global Gryffindor
    global Slytherin
    global Hufflepuff
    global Ravenclaw

    Ques_7 = f"{Fore.CYAN}Q7. Given the choice, would you rather invent a portion that will guarantee you? {Style.RESET_ALL}\n\n\n1. Glory \n\n2. Love \n\n3. Power \n\n4. Wisdom"

    print(Ques_7)

    print(colored("\n\nChoose one option", "magenta"))

    choice7 = input()
    print()

    if choice7 == "1":
        Gryffindor += 2
        os.system('cls')
        eight_part()

    elif choice7 == "2":
        Hufflepuff += 2
        os.system('cls')
        eight_part()

    elif choice7 == "3":
        Slytherin += 2
        os.system('cls')
        eight_part

    elif choice7 == "4":
        Ravenclaw += 2
        os.system('cls')
        eight_part()

    else:
        wrong7 = f"{Fore.RED}Oops! Wrong option, try again{Style.RESET_ALL}"
        print(wrong7)
        time.sleep(1)
        os.system('cls')
        seventh_part()


def eight_part():
    global Gryffindor
    global Slytherin
    global Hufflepuff
    global Ravenclaw

    Ques_8 = f"{Fore.CYAN}Q8. What path you're intended to follow after leaving Hogwarts School? {Style.RESET_ALL}\n\n\n1. I will work hard and try to achieve as much success as possible \n\n2. I will settle down and live a simple life \n\n3. I will go on adventures, going to explore the world and travel new places \n\n4. I will try to make a difference in the world"

    print(Ques_8)

    print(colored("\n\nChoose one option", "magenta"))

    choice8 = input()
    print()

    if choice8 == "1":
        Slytherin += 2
        os.system('cls')
        ninth_part()

    elif choice8 == "2":
        Hufflepuff += 2
        os.system('cls')
        ninth_part()

    elif choice8 == "3":
        Gryffindor += 2
        os.system('cls')
        ninth_part()

    elif choice8 == "4":
        Ravenclaw += 2
        os.system('cls')
        ninth_part()

    else:
        wrong8 = f"{Fore.RED}Oops! Wrong option, try again{Style.RESET_ALL}"
        print(wrong8)
        time.sleep(1)
        os.system('cls')
        eight_part()


def ninth_part():
    global Gryffindor
    global Slytherin
    global Hufflepuff
    global Ravenclaw

    Ques_9 = f"{Fore.CYAN}Q9. Which of these Classical elements describes you you the most? {Style.RESET_ALL}\n\n\n1. Earth \n\n2. Water \n\n3. Air \n\n4. Fire"

    print(Ques_9)

    print(colored("\n\nChoose one option", "magenta"))

    choice9 = input()
    print()

    if choice9 == "1":
        Hufflepuff += 2
        os.system('cls')
        tenth_part()

    elif choice9 == "2":
        Slytherin += 2
        os.system('cls')
        tenth_part()
        
    elif choice9 == "3":
        Ravenclaw += 2
        os.system('cls')
        tenth_part()

    elif choice9 == "4":
        Gryffindor += 2
        os.system('cls')
        tenth_part()

    else:
        wrong9 = f"{Fore.RED}Oops! Wrong option, try again{Style.RESET_ALL}"
        print(wrong9)
        time.sleep(1)
        os.system('cls')
        ninth_part()


def tenth_part():
    global Gryffindor
    global Slytherin
    global Hufflepuff
    global Ravenclaw

    Ques_10 = f"{Fore.CYAN}Q10. Finally, In which house you want to go in?{Style.RESET_ALL} \n\n\n1. Gryffindor (red and gold)\n\n2. Slytherin (green and silver) \n\n3. Hufflepuff (yellow and black) \n\n4. Ravenclaw (blue and bronze)"

    print(Ques_10)

    print(colored("\n\nChoose one option", "magenta"))

    choice10 = input()
    print()

    if choice10 == "1":
        Gryffindor += 4
        os.system('cls')
        final_result()

    elif choice10 == "2":
        Slytherin += 4
        os.system('cls')
        final_result()

    elif choice10 == "3":
        Hufflepuff += 4
        os.system('cls')
        final_result()

    elif choice10 == "4":
        Ravenclaw += 4
        os.system('cls')
        final_result()

    else:
        wrong10 = f"{Fore.RED}Oops! Wrong option, try again{Style.RESET_ALL}"
        print(wrong10)
        time.sleep(1)
        os.system('cls')
        tenth_part()


def final_result():
    global Gryffindor
    global Slytherin
    global Hufflepuff
    global Ravenclaw

    print("The Sorting Hat gives you....\n")
    time.sleep(4)

    Houses_Score = [Gryffindor, Slytherin, Hufflepuff, Ravenclaw]

    High_Score = max(Houses_Score)

    if High_Score == Gryffindor:

        Griff = f"{Fore.RED}Gryffindor\n\n{Style.RESET_ALL}"

        print(color.BOLD + Griff + color.END)
        time.sleep(1.5)

        for x in colored("You get the house of the daring and the brave.",
                         "red"):

            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(0.05)

        time.sleep(1)

        print(
            "\n\nYou have a heart of a lion. You never give up, never back down and give everything 100%. Good things happen to you because you fight for them. You stand up for yourself and for your friends because you believe in what is right. Your energy is magnetic and makes you a natural leader.\n\n\n\n\n"
        )

        exit()

    elif High_Score == Slytherin:

        Slyt = f"{Fore.GREEN}Slytherin\n\n{Style.RESET_ALL}"

        print(color.BOLD + Slyt + color.END)
        time.sleep(1.5)

        for x in colored("You get the house of the daring and the brave.",
                         "green"):

            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(0.05)

        time.sleep(1)

        print(
            "\n\nYou're always ahead of the pack. You know what is cooler before anyone else knows and you are happy to be the trendsetter. You're smart and ambitious and not afraid to put your all in. You love to stay away from the croud and so you will be. You're destined for greatness and you deserve it because you're one of a kind.\n\n\n\n\n"
        )

        exit()

    elif High_Score == Hufflepuff:

        Huff = f"{Fore.YELLOW}Hufflepuff\n\n{Style.RESET_ALL}"

        print(color.BOLD + Huff + color.END)
        time.sleep(1.5)

        for x in colored("You get the house of the loyal and the fair.",
                         "yellow"):

            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(0.05)

        time.sleep(1)

        print(
            "\n\nPeople flock to you because you're a great friend. You value loyalty and always think of others first. People are lucky to have you in their lives and they know it. You are the most favorite type of person. Why isn't it exciting to told you're a kind person? You have bold at argument and a big thinker.\n\n\n\n\n"
        )

        exit()

    elif High_Score == Ravenclaw:

        Raven = f"{Fore.BLUE}Ravenclaw\n\n{Style.RESET_ALL}"

        print(color.BOLD + Raven + color.END)
        time.sleep(1.5)

        for x in colored("You get the house of the clever and wise.", 
                         "blue"):

            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(0.05)

        time.sleep(1)

        print(
            "\n\nYou are intelligent, creative and wise. Your friends often come to you to get advice because you always know what to say. Your creativity allows you to look at things in an out-of-the-box way. And your wit makes you a pleasure to be around. Knowledge in everything for you\n\n\n\n\n"
        )

        exit()


first_part()
final_result()
screen_cls()
