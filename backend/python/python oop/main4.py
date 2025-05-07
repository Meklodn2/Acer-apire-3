# Polimorfizm (Polymorphism)
class Car():
    def startEngine(self):
        return "Car engine started"
class bike():
    def startEngine(self):
        return "Bike engine started"
    
# polimorfizm nmaoyish qiluvchi funksiya 
def SatartVehicalEngine(vehical):
    print(vehical.startEngine())

car = Car()
bike = bike()
SatartVehicalEngine(car)
SatartVehicalEngine(bike)