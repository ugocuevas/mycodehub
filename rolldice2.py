#In this program, we roll two fair dice and the results will determine the next step to take
from random import randint
from time import sleep

#In this first section, all the needed functions will be declared
#Play option: This function determines whether the user wants to play or not
def playOption():
    playOrNot = input("Do you want to roll the dice or exit the game? \n Type Y/N to indicate your choice: ")
    playOrNot = playOrNot.capitalize()
    if playOrNot == "N":
        print("Goodbye. See you later")
        exit()
    elif playOrNot == "Y":
        print(f"Welcome {username}, your dice will now be rolled")   
    else:  
        print(f"{username}, The game will now exit because you put in an invalid command.\nGoodbye!")
        exit()  

#Roll dice: This function rolls the dice on behalf of the user
def rollDice():
    print("Rolling die...")
    sleep(1)
    die_roll_one = randint(1,6)
    die_roll_two = randint(1,6)
    print(f"You need double sixes to start the game")
    if die_roll_one == die_roll_two == 6:
        print(f"Amazing {username}, you rolled double sixes. \nYou can start the game! ")
        exit()
    else:
        print(f"You rolled {die_roll_one} and {die_roll_two}.\nPlease try again")

#---------------Running the code-----------------------------------------------------
username = input("Please enter your name: ")
username = username.capitalize()

playOption()

#Determine the outcome of the die throw
count = 10
while count > 0:
#Roll the die    
    rollDice()
    count = count -1
print(f"Uh oh! {username}, you have exhausted the number of times you can throw.\nYou will now exit the game! ") 



