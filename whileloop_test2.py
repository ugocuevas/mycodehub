# List of numbers
listOfStuff = [21, 33, 77, 2, 4, 10, 3, 17]

#This while loop starts listing the odd and even from index 0 which is number from 21
length_of_list = len(listOfStuff)
count = 0
print('while loop')
while count < length_of_list:
    if listOfStuff[count] % 2 == 0:
        print(f"even - {listOfStuff[count]}")
    else:
        print(f"odd - {listOfStuff[count]}")
    count = count + 1
    
print('-----------------------------------------------------------------')

# this for loop starts listing the odd and even number from index 0 which is 21
print('for loop')
listOfStuff = [21, 33, 77, 2, 4, 10, 3, 17]
for x in listOfStuff:
    if x % 2 == 0:
        print(f"even - {x}")
    else:
        print(f"odd - {x}")


# Task:
# Rewrite the while loop so that it would start listing the odd and even numbers from
# index 0
