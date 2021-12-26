# def function_name(parameter1, parameter2):
#     do something

#function_name(argument1, argument2)

#Function without parameters
def sit_down():
    print("I am sitting down")
    
sit_down()

# #Functions with parameters
# #Positional parameters
def describe_human(gender, human_name):
    print(f"This is a {gender} whose name is {human_name}")
     
describe_human('male', 'Tolu')

#Keyword parameters 
def describe_cars(brand, model):
    print(f"This is a {brand} and its model is {model}")
    
describe_cars(model = 'Camry 2015', brand = 'Toyota')

# #Default values
def what_to_eat(food = 'rice', meat = 'beef', drink = 'bobo'):
    print(f"My husband will eat {food},{meat} and {drink} this evening")
    
what_to_eat(food = 'omelette', meat = 'chicken')

# Passing lists into functions
def order_meal(menu):
    """This code prints out the menu in the restaurant"""
    for food in menu:
        order = f"{food}"
        print(order)
menu_list = ['rice', 'beans', 'spaghetti', 'plantain']
order_meal(menu_list)

#Arbitrary number of arguments
def order_meal(meal_class, *menu):
    print(menu)
    
order_meal('regular', 'rice', 'beans', 'egg', 'spaghetti', 'potatoes', 'yam', 'plantain')

def build_student(first_name, course, **other_info):
    other_info['first_name'] = first_name
    other_info['course'] = course
    return other_info

new_student = build_student('Nwachi', 'Psychology', state = 'Florida', marital_status = 'married', gender = 'male')
print(new_student)
