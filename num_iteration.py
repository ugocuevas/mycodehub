#This code iterates through every number in a list to separate out even and odd numbers

my_list = [1, 2, 3, 4, 5, 6, 7, 21, 33, 32, 2, 4]

#Create a list to place the even numbers
even_numbers = []

#Create a list to place the odd numbers
odd_numbers = []

#Iterate through the list to select the separate the even and odd numbers
for number in my_list:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
        
#Print out the populated lists        
print(odd_numbers)
print(even_numbers)
    
