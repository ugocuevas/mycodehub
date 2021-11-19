#In this program, we roll a die and the results of the die determines the next step to take
from random import randint

username = input("To test your luck, please enter your name or type exit to leave the game: ")
username = username.capitalize()
if username == "Exit":
    print("Goodbye and see you later")
    exit()
else:
    print(f"Welcome {username}, your die will now be rolled")

#Roll the die    
die_roll = randint(1,6)

#Determine the outcome of the die throw
if die_roll == 1:
    print(f"You rolled {die_roll}. Please drop the die. Better luck next time {username}. Thank you")
    exit()
elif die_roll == 6:
    print(f"You rolled {die_roll}. Move to the next step")
    secondDieRoll = randint(1, 6)
    if secondDieRoll == 6:
        print(f"Second die roll.\n Amazing {username}, you rolled {secondDieRoll}. You are the Champion! ") 
    else: 
        print(f"You rolled {secondDieRoll}.\n Not bad {username}, goodbye!")   
else: 
    print(f"You rolled {die_roll}. Please roll again")
    secondDieRoll = randint(1, 6)
    if secondDieRoll != 6:
        print(f"You rolled {secondDieRoll}.\n Too bad, {username}, better luck next time. Goodbye!")
    else:
        print(f"Nice throw {username}! You rolled {secondDieRoll}. You are luckier than most players. Goodbye")    