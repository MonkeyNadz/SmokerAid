import board
import busio
import digitalio
import adafruit_max31856

#SPI Bus object (busio based) - just defines the grouping of pins for SPI
# - adafruit_bus_device/spi_device.py
SPI = busio.SPI(board.SCK, board.MOSI, board.MISO)

#Chip Select - if we want multiple SPI slave devices - can set multiple CS for
#    multiple slave SPI chips.
CS = digitalio.DigitalInOut(board.D5)

#Output as its chip selection - and default high - sets to low to select that
#  slave chip and then send data out of MOSI
CS.direction = digitalio.Direction.OUTPUT

#Finally set up thermocouple object - defaults to K Type
thermocouple = adafruit_max31856.MAX31856(SPI,CS)

# The .temperature reads the register - sets CS to low - and reads
print(thermocouple.temperature)
