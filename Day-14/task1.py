class Vehicle:
    def start(self):
        print("vehicle starting....")
class Car(Vehicle):
    def start(self):
        print("Car: Vroom Vroom!")
class Bike(Vehicle):
    def start(self):
        print("Bike: Brumm Brumm!")

for i in [Vehicle(),Car(),Bike()]:
    i.start()
