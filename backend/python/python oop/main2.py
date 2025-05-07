# Inhertianse (meros olish)
class Vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
    def start(self):
        print(f"{self.brand} vehical started at speed {self.speed} km/h")
    def stop(self):
        print(f"{self.brand} vehica stopped")

class Car(Vehicle):
    def __init__(self,brand,speed,model):
        super().__init__(brand,speed)
        self.model = model

    def start(self):
        super().start()
        print(f"The car model {self.model} is now running")

class Boat(Vehicle):
    def __init__(self,brand,speed,capacity):
        super().__init__(brand,speed)
        self.capacity = capacity
    def start(self):
        super().start()
        print(f"The boat with capacity {self.capacity} people is now sailing")

car = Car("Tayota",400,"Supra")

car.start()

boat = Boat("Yamaha",30,10)
boat.start()

print(dir(Vehicle))


