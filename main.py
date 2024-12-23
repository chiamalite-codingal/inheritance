class vehicle:
    def __init__(self,name,maxspeed,mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage
class new(vehicle):
    pass
#obj
v1 = new("bus",120,55)
print("The vehicle's name is:",v1.name)
print("The vehicle's speed is:",v1.maxspeed)
print("The vehicle's mileage is:",v1.mileage)