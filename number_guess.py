#1. Number guessing game: Let the computer generate a random number and let us see how many guesses it takes for the user to arrive at that number
#Import the needed classes
from random import randint


def userInput():
    #Activate user input
    try:
        global user_number
        user_number = input("Please enter a number between 1 and 6: ")
        user_number = int(user_number)
        print(f"You chose {user_number}")
    except:
        print("You have not entered a number. You are one of the problems in this world. The game will end now")
        exit()  

def guessChecker():
    #Compare the user input to the computer's
    global user_number, random_number
    while user_number != random_number:
        print("Try again")
        if user_number < random_number:
            print("Hint: Go a bit higher")
            userInput()
        elif user_number > random_number:
            print("Hint: Go a a bit lower")
            userInput()        
        break
    print("Congratulations!")
    
#Let the computer generate the random number
random_number = randint(1, 6)

#Define the list of numbers to guess from. In this case 1 to 6
list_of_numbers = list(range(1, 7))

#Check if user input is valid
userInput()

if user_number in list_of_numbers:
    print(f"The number the computer chose is {random_number}")
    #Check if the user guessed correctly
    guessChecker()
    

# else:
#     print("The value you entered is invalid")
#     while user_number not in list_of_numbers:
#         userInput()
#         continue
#     print("Thank you!")
#     guessChecker()
#     print("Congratulations!")




#extra spices: guess limits

