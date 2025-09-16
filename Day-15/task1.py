class SmartDevice:
    def power_on(self):
        pass
class Smartphone(SmartDevice):
    def power_on(self):
        print("Smartphone: Booting mobile OS...")

class Smartwatch(SmartDevice):
    def power_on(self):
        print("Smartwatch: Starting wearable system..")

smart=[Smartphone(),Smartwatch()]
print("Turning on device...")
for s in smart:
    s.power_on()
