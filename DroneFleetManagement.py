class Device:
    def __init__(self,name,model):
        self.__name = name
        self.__model = model

    def get_name(self):
        return self.__name

    def get_model(self):
        return self.__model

class Flyer:
    def fly(self):
        print("Device is Flying")


class Drone(Device,Flyer):
    def __init__(self,name,model):
        super().__init__(name,model)

    def fly(self):
        print("Drone is Flying")

    def capture_image(self):
        print("Capturing the image")



drone = Drone("my_drone","model_25")
drone.fly()
drone.capture_image()
print(drone.get_name())
print(drone.get_model())