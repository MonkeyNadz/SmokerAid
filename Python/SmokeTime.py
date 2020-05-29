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

if __name__ == "__main__":
    thermocouple = thermocoupleSetup(board.D5)
    relay = digitalio.DigitalInOut(board.D17)
    relay.direction = digitalio.Direction.OUTPUT
    target_tmp = input("Target Temperature: ")
    while True:
        cur_temp = thermocouple.temperature
#        print(cur_temp)
        if cur_temp >= target_tmp:
            print(str(cur_temp) + " too low setting fan off...")
            relay.value = False
        else:
            print(str(cur_temp) + " too high setting fan on...")
            relay.value = True

        time.sleep(0.5)
