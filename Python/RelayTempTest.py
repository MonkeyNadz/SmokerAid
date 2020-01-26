import board
import digitalio
import time
import busio
import adafruit_max31856

def thermocoupleSetup(CSPin):
    SPI = busio.SPI(board.SCK,board.MOSI,board.MISO)
    CS = digitalio.DigitalInOut(CSPin)
    CS.direction = digitalio.Direction.Output
    thermocouple = adafruit_max31856.MAX31856(SPI,CS)
    return thermocouple


class RelayControl:
    controlPin = None

    def __init__(self,RelayPin):
        self.controlPin = RelayPin
        self.controlPin.direction = digitalio.Direction.Output

    def RelayOn:
        self.controlPin.value = True

    def RelayOff:
        self.controlPin.value = False

if __name__ == "__main__":
    thermocouple = thermocoupleSetup(board.D5)
    fan = RelayControl(board.D17)

    while True:
        cur_temp = thermocouple.temperature
        if cur_temp >= 24:
            fan.RelayOn()
        else:
            fan.RelayOff()


            
