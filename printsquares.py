#This code creates and prints out a list that contains the squares of each number from 1 to 20
list_of_squares = []

def x_squared(first_num, second_num):
    for number in range(first_num, second_num):
        square = number ** 2
        list_of_squares.append(square)
    return(list_of_squares)    

print(x_squared(1, 6))