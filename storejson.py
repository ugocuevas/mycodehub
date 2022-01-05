#JSON: JavaScript Object Notation
#Dumping and loading
import json

def get_username():
    firstname = input("Please enter your first name: ")
    lastname = input("Please enter your last name: ")
    username = f"Hi {firstname} {lastname}, python will remember you when you return"
    return username

user_one = get_username()
filename = 'names.json'
with open(filename, 'w') as f:
    json.dump(user_one, f)
    
print(user_one)
