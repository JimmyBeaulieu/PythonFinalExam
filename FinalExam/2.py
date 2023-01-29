# create a class called Auto.
# give the Auto class a constructor that defines properties for model and cylinder.
# create get methods for each of the properties. create methods that start the engine,
# accelerate the car and break the car. have the methods return a string that shows
# the method was called. create classes for 3 cars of your choice.
# Override the start, accelerate, and break methods.
# create an output that will show the car's name, model,
# and action called.

class Auto:
    def __init__(self, model, cylinder):
        self.model = model
        self.cylinder = cylinder

    def getModel(self):
        return self.model

    def getCylinder(self):
        return self.cylinder

    def toString(self):
        return self.model + " " + self.cylinder

    def StartEngine(self):
        print("Engine has started...")

    def Accelerate(self):
        print("The car is going a bit faster now...")

    def Break(self):
        print("Car was stopped...")


class BoringCar(Auto):
    def StartEngine(self):
        print("The boring car starts...")

    def Accelerate(self):
        print("The boring car accelerates...")

    def Break(self):
        print("The boring car stopped...")


class NormalCar(Auto):
    def StartEngine(self):
        print("The normal car starts...")

    def Accelerate(self):
        print("The normal car accelerates...")

    def Break(self):
        print("The normal car stopped...")


class CoolCar(Auto):
    def StartEngine(self):
        print("The cool car starts...")

    def Accelerate(self):
        print("The cool car accelerates...")

    def Break(self):
        print("The cool car stopped...")


boring = BoringCar("Boring model", "Not cool cylinder")
normal = NormalCar("Normal model", "Normal cylinder")
cool = CoolCar("Cool model", "Cool cylinder")

boring.StartEngine()
normal.Accelerate()
cool.Break()
print(boring.toString())
print(normal.toString())
print(cool.toString())