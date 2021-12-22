# def function_name(parameter1, parameter2):
#     do something

#function_name(argument1, argument2)

#Positional parameters
def describe_human(gender, human_name):
    print(f"This is a {gender} whose name is {human_name}")
     
describe_human('male', 'Tolu')

#Keyword parameters 
def describe_cars(brand, model):
    print(f"This is a {brand} and its model is {model}")
    
describe_cars(model = 'Camry 2015', brand = 'Toyota')

#Default values
def what_to_eat(food = 'rice', meat = 'beef', drink = 'bobo'):
    print(f"My husband will eat {food},{meat} and {drink} this evening")
    
what_to_eat(drink='water')
