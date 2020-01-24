import board
import busio
import digitalio
import Adafruit_CircuitPython_MAX31856

#SPI Busio Object
SPI = busio.SPI(board.SCK, board.MOSI, board.MISO)

cs = digitalio.DigitalInOut(board.D5)
cd.direction = digitalio.Direction.Output

thermocouple = adafruit_max31856.MAX31856(spi,cs)

print(thermocouple.temperature)
