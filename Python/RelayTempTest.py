import board
import digitalio
import time
import busio
import adafruit_max31856

def thermocoupleSetup(CSPin):
    SPI = busio.SPI(board.SCK,board.MOSI,board.MISO)
    CS = digitalio.DigitalInOut(CSPin)
    CS.direction = digitalio.Direction.OUTPUT
    thermocouple = adafruit_max31856.MAX31856(SPI,CS)
    return thermocouple

def RelayOn(pin):
    pin.value = True

def RelayOff(pin):
    pin.value = False

def RelaySetup(pin):
    controlPin = pin
    controlPin.direction = digitalio.Direction.OUTPUT
    return controlPin

if __name__ == "__main__":
    thermocouple = thermocoupleSetup(board.D5)
    relay = RelaySetup(board.D17)

    while True:
        cur_temp = thermocouple.temperature
        print(cur_temp)
        if cur_temp >= 24:
            fan.RelayOn()
        else:
            fan.RelayOff()
