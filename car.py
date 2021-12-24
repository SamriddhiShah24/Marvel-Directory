class Car(object):
    def __init__(self, model, colour, company, speedLimit):
        self.model = model
        self.colour = colour
        self.company = company
        self.speedLimit = speedLimit

    def start(self):
        print("start!")
        
    def stop(self):
        print("stop!")
        
kia = Car("Kia", "black", "Kia", "240km/hr")
bmw = Car("BMW X5", "navy blue", "BMW", "280km/hr")
print(kia.model)
print(kia.colour)
print(kia.company)
print(kia.speedLimit)
print("*")
print(bmw.model)
print(bmw.colour)
print(bmw.company)
print(bmw.speedLimit)