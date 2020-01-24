import board
import busio
import digitalio
import adafruit_max31856

#SPI Busio Object
SPI = busio.SPI(board.SCK, board.MOSI, board.MISO)

CS = digitalio.DigitalInOut(board.D5)
CS.direction = digitalio.Direction.OUTPUT

thermocouple = adafruit_max31856.MAX31856(SPI,CS)

print(thermocouple.temperature)
