from Vehicle import Vehicle
class MotorCar(Vehicle):
    def activate_air_conditioning(self):
        if self.is_operational:
            print("Air conditioning activated.")
        else:
            print("Start the car to activate air conditioning.")

