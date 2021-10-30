listOfCars = ['Lexus', 'Honda', 'Toyota', 'Benz', 'Chrysler']
#This method is specifically for the example you gave. It will likely not work for other examples
listOfCars1 = sorted(listOfCars)
print(listOfCars1[1:4])

#This method involves removing the strings you do not want
del listOfCars[2:4]
print(listOfCars)