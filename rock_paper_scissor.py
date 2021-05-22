print("""
HELLO,
and welcome to rock paper scissor game,
MADE BY DEVARYA MISHRA
""")
import random

rock = """
ROCK
"""
paper = """
PAPER
"""
scissor = """
SCISSOR
"""
ans = input("What do you want to choose, scissor- s, rock- r, paper = p: ")
if ans == "s" or ans == "r" or ans == "p":
    comp = random.randint(1, 3)
    if comp == 1:
        comp = "r"
    elif comp == 2:
        comp = "p"
    else:
        comp = 's'
    if ans == 's' and comp == 'r':
        print("You chose scissor, computer chose rock. rock beats scissor, YOU LOSE!!!")
    elif ans == 'p' and comp == 's':
        print("You chose paper, computer chose scissor. scissor beats paper, YOU LOSE!!!")
    elif ans == 'r' and comp == 'p':
        print("You chose rock, computer chose rock. scissor beats paper, YOU LOSE!!!")
    elif ans == comp:
        print("You both have chosen same, TIED!!!")
    else:
        print(f"you have chose {ans} ,  computer has chosen {comp} .  {ans} beats {comp}, YOU WON!!!"
              "\np- paper, s- scissor, r- rock")
else:
    print("ERROR, WRONG INPUT ENTERED\t"
          "PLEASE CHECK THE INPUT AND RERUN THE PROGRAM!!!")
