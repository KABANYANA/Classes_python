# fruit.py

class Fruit:
    category = "vegies"
    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste
    
    def wash(self):
        print(f"{self.name} is being washed.")
        
    def peel(self):
        print(f"{self.name} with {self.color} color is being peeled.")
    
    def eat(self):
        print(f"{self.name} I am eating is{self.taste}.")



fruit1 = Fruit("Apple", "Red", "Sweet")
fruit2 = Fruit("Orange", "Orange", "Sour")


fruit1.wash()
fruit2.peel()
fruit2.eat()