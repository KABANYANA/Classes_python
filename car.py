
class Car:
    make = "BMW"
    def __init__(self, model, color, mileage):
        self.model = model
        self.color = color
        self.mileage = mileage
    
    def start(self):
        print(f"{self.model} has started going")
        
    def drive(self):
        print(f"The car is being driven at {self.mileage} km/hr")
    
    def stop(self):
        print(f"{self.model} with {self.color} color has stopped.")

car1 = Car("BMWX7", "Red", 30000)
car2 = Car("BMWi4", "Blue", 20000)

car1.start()
car1.stop()
car2.drive()