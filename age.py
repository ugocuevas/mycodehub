'''This code will calculate the age of the user provided the correct data is supplied.
To make this code a bit dynamic, the user has to supply the year in which they are using the code as well
'''
presentYear = input("What year is this? ")
yourName = input("What is your name? ")
yourYearOfBirth = input("In what year were you born? ")
yourAge = int(presentYear)-int(yourYearOfBirth)
print(f"\nDear \033[1m{yourName}\033[0m, you are \033[1m{yourAge}\033[0m years old")
