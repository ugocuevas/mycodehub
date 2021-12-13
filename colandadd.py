#I've only been asked to collect the numbers that you give me and add them up
firstNumber = input("Please enter the first number: ")
secondNumber = input("Please enter the second number: ")
def sumOfNumbers(a, b):
    a = int(a)
    b = int(b)
    c = a - b
    return c
print(f"The sum of {firstNumber} and {secondNumber} is {sumOfNumbers(secondNumber, firstNumber)}")


# Variables
#Global: When a variable is declared outside........it can be used anywhere within the script
#Local: When a variable is declared inside a function, the variable is local and cannot be used outside the variable

