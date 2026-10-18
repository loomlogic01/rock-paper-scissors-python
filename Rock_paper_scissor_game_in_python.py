"""
Workflow of project

1.input from user(rock, paper, and scissor)
2.computer choice (computer choose randomly not conditionally)
3.result print

"""
"""
cases:
A-Rock
rock-rock= tie 
rock-paper = paper win
rock-scissor = rock win

B-Paper
paper-paper = tie
paper-scissor = scissor win
paper-rock = paper win

C-Scissor 
scissor-Scissor = tie
scissor-Rock = Rock win
scissor-paper = scissor win 

"""

import random
item_list=["Rock", "paper", "scissor"]
user_choice=input("enter your move \"Rock\", \"paper\", \"scissor\" :")
comp_choice= random.choice(item_list)
print(f"user_choice={user_choice},computer choice ={comp_choice}")

if user_choice == comp_choice :
    print("both chooses same : Match tie")

elif user_choice == "Rock" :
    if comp_choice == "paper":
        print("paper cover Rock = computer win")
    else :
        print("Rock smashes Scissor = You win")

elif user_choice == "paper":
    if comp_choice == "scissor":
        print("scissor cut the paper = computer win")
    else:
        print("paper cover Rock = you win")
elif user_choice == "scissor":
    if comp_choice == "Rock":
        print("Rock smashes the scissor = computer win")
    else:
        print("scissor cut the paper = you win")     



