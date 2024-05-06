
class Vehicle:
    def __init__(self, speed):
        self.speed = speed


class Landvehicle(Vehicle):
    def __init__(self, speed, w_count):
        super().__init__(speed)
        self.w_count = w_count


class Car(Landvehicle):
    pass


vehicle = Vehicle(60)
landvehicle = Landvehicle(60, 4)
car = Car(50, 4)

print(isinstance())
print(isinstance(landvehicle, Landvehicle))
print(isinstance(landvehicle, Car))