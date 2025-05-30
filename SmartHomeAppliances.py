class Appliance:
    def status(self):
        print("Appliance is turned Off")


class Fan(Appliance):
    def status(self):
        print("Fan is Turned On")


class Light(Appliance):
    def status(self):
        print("Light is Turned On")


class AC(Appliance):
    def status(self):
        print("AC is Turned On")


devices = [Fan(),Light(),AC()]
for device in devices:
    device.status()