#1. Number guessing game: Let the computer generate a random number and let us see how many guesses it takes for the user to arrive at that number
#Import the needed classes
from random import randint

#Activate user input
user_number = input("Please enter a number between 1 and 6: ")
user_number = int(user_number)
random_number = randint(1, 6)

list_of_numbers = list(range(1, 7))
#Check if user input is valid
if user_number in list_of_numbers:
    print("Thank you!")
    print(f"The number the computer chose is {random_number}")
    #Check if the user guessed correctly
    while user_number != random_number:
        print("Try again")
        user_number = input("Please enter a number between 1 and 6: ")
        user_number = int(user_number)
        continue
    print("Congratulations!")
    
    
    
 
 
 
 
 
 
 
 
 
    
    # if user_number == random_number:
    #     print("Congratulations")
    # else:
    #     print("Try again, sorry")
    #     exit()    
    
    
    
# elif user_number not in list_of_numbers:
#     print()
# else:
#     print("Enter a valid integer between 1 and 6")
#     user_number = input("Please enter a number between 1 and 6: ")
#     user_number = int(user_number)    



#extra spices: guess limits

