class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.is_running = False
        self.speed = 0

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.speed = 0
            print(f"The {self.make} {self.model} has started.")
        else:
            print(f"The {self.make} {self.model} is already running.")

    def stop(self):
        if self.is_running and self.speed == 0:
            self.is_running = False
            print(f"The {self.make} {self.model} has stopped.")
        elif self.speed > 0:
            print(f"Reduce speed to 0 before stopping the car.")
        else:
            print(f"The {self.make} {self.model} is already stopped.")

    def accelerate(self, increment):
        if self.is_running:
            self.speed += increment
            print(f"Accelerating. The speed of the {self.make} {self.model} is now {self.speed} km/h.")
        else:
            print("Start the car before accelerating.")

    def decelerate(self, decrement):
        if self.is_running and self.speed >= decrement:
            self.speed -= decrement
            print(f"Decelerating. The speed of the {self.make} {self.model} is now {self.speed} km/h.")
        else:
            print("Insufficient speed to decelerate by that amount or the car is not running.")

    def display_status(self):
        if self.is_running:
            print(f"The {self.make} {self.model} is running. Current speed: {self.speed} km/h.")
        else:
            print(f"The {self.make} {self.model} is not running.")

# Example usage:
my_car = Car("Toyota", "Corolla")
my_car.start()
my_car.accelerate(30)
my_car.display_status()
my_car.decelerate(20)
my_car.stop()
