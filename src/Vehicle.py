class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.is_operational = False
        self.speed = 0

    def turn_on(self):
        if not self.is_operational:
            self.is_operational = True
            self.speed = 0
            print(f"The engine of {self.make} {self.model} has been turned on.")
        else:
            print(f"{self.make} {self.model} is already on.")

    def turn_off(self):
        if self.is_operational and self.speed == 0:
            self.is_operational = False
            print(f"{self.make} {self.model} has been turned off.")
        elif self.speed > 0:
            print(f"Reduce speed to 0 before turning off the engine.")
        else:
            print(f"{self.make} {self.model} is already off.")

    def accelerate(self, increment):
        if self.is_operational:
            self.speed += increment
            print(f"Accelerating. The speed of {self.make} {self.model} is now {self.speed} km/h.")
        else:
            print("Start the engine before accelerating.")

    def decelerate(self, decrement):
        if self.is_operational and self.speed >= decrement:
            self.speed -= decrement
            print(f"Decelerating. The speed of {self.make} {self.model} is now {self.speed} km/h.")
        else:
            print("Insufficient speed to decelerate or the engine is not on.")

    def show_status(self):
        if self.is_operational:
            print(f"{self.make} {self.model} is operational. Current speed: {self.speed} km/h.")
        else:
            print(f"{self.make} {self.model} is not operational.")
    def test(self):
        pass
