#This code prints all the numbers between 10 and 20 except prime number
#For background, a prime number is a number that can only divide one and itself without a remainder. For example, 2, 3, 7 etc.
#This demonstrates the three method: Courtesy Viennivre

#Create the list of numbers
list_of_numbers = list(range(10, 21)) 
print(list_of_numbers)

#Create a list to append the non-prime number
non_prime_numbers = set()

#Iterate through the list and select the non-prime numbers
for number in list_of_numbers: 
    for i in range(2, number): 
        if (number % i) == 0:
            non_prime_numbers.add(number)
            
print(non_prime_numbers)