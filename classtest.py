#A class is the blueprint of an object. For example, a recipe for a cake, a blueprint for a car
#Object is an instantiation of a class
#Classes have attributes and methods
#A method is a function that is part of a class
#Attributes are variables that are accessible through the instances

class Cake:
    def __init__(self, name, flavour, shape):
        """Initiate the name, flavour and shape attributes"""
        self.name = name
        self.flavour = flavour
        self.shape = shape
        
    def melt(self):
        print(f"Uh oh! The {self.flavour} cake has melted")
        
    def spoil(self):
        print(f"Oh no! The {self.shape} cake has gone bad")
        
"""Creating an instance of a class"""
christmas_cake = Cake('Christmas', 'vanilla', 'round')
print(f"The cake I had this christmas was {christmas_cake.flavour} flavoured and it was {christmas_cake.shape}")