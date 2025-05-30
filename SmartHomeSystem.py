from abc import ABC,abstractmethod




class SmartDevice(ABC):
    def __init__(self,name):
        self.__is_on = False
        self.name = name

    @abstractmethod
    def operate(self, param):
        pass

    def get_status(self):
        return self.__is_on

    def off_device(self):
        self.__is_on=False

    def on_device(self):
        self.__is_on= True

    def show_status(self):
        if self.__is_on:
            print('Device is On')
        else:
            print("Device is off")


class SmartLight(SmartDevice):
    def __init__(self,name):
        super().__init__(name)
        self.__brightness = 70

    def get_brigtness(self):
        return self.__brightness

    def operate(self,brightness_level):
        super().on_device()
        self.__brightness=brightness_level

    def show_status(self):
        status = super().get_status()
        if status:
            print(f"Light is Turned On & Brightness : {self.__brightness}")
        else:
            print("Light is turned Off")


class SmartFan(SmartDevice):
    def __init__(self,name):
        super().__init__(name)
        self.__speed = 'medium'

    def get_speed(self):
        return self.__speed

    def operate(self,speed):
        super().on_device()
        self.__speed=speed

    def show_status(self):
        status = super().get_status()
        if status:
            print(f"Fan is Turned On & Speed : {self.__speed}")
        else:
            print("Fan is turned Off")


class SmartAC(SmartDevice):
    def __init__(self,name):
        super().__init__(name)
        self.__temperature = 24

    def get_temperature(self):
        return self.__temperature

    def operate(self,temp):
        super().on_device()
        self.__temperature=temp

    def show_status(self):
        status = super().get_status()
        if status:
            print(f"AC is Turned On & Temperature : {self.__temperature}C")
        else:
            print("AC is turned Off")



hall_light = SmartLight("hall_light")
hall_light.show_status()
hall_light.operate(100)
hall_light.show_status()
hall_light.off_device()
hall_light.show_status()

#hall_light.__is_on = True






