#This code shows that it is possible to cast from integer to boolean.
#We will start with zero
a = 0
check = bool(a)
print(type(check))
print(check)

#Let us try one
a = 1
check = bool(a)
print(type(check))
print(check)

#Let us try four
a = 4
check = bool(a)
print(type(check))
print(check)

#Let us try minus five
a = -5
check = bool(a)
print(type(check))
print(check)

print(f'\nFrom the results obtained after running the code, we can conclude that integers can be cast to boolean.\nHowever, zero will ''return False while any other number will return True')
