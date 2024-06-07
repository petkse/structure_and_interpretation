class Pump:
    def activate(self):
        pass

class GeneralPump(Pump):
    def __init__(self, category):
        self.category = category

    def activate(self):
        print(f"{self.category} насос")

class PlungerPump(GeneralPump):
    def activate(self):
        print(f"{self.category} насос плунжерит")

class CentrifugalPump(GeneralPump):
    def activate(self):
        print(f"{self.category} насос центробежит")

def main():
    plunger = PlungerPump("плунжерный")
    centrifugal = CentrifugalPump("центробежный")

    pump_list = [plunger, centrifugal]

    for pump in pump_list:
        pump.activate()

if __name__ == "__main__":
    main()
