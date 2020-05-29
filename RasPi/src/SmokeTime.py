import board
import digitalio
import time
import busio
import adafruit_max31856
import logging
import json
import pathlib
import json_log_formatter

def thermocoupleSetup(CSPin):
    SPI = busio.SPI(board.SCK,board.MOSI,board.MISO)
    CS = digitalio.DigitalInOut(CSPin)
    CS.direction = digitalio.Direction.OUTPUT
    thermocouple = adafruit_max31856.MAX31856(SPI,CS)
    return thermocouple

class CustomMessage:
    def __init__(self,**kwargs):
        self.kwargs = kwargs

    def __str__(self):
        return '%s' % (json.dumps(self.kwargs))


if __name__ == "__main__":
    thermocouple = thermocoupleSetup(board.D5)
    relay = digitalio.DigitalInOut(board.D17)
    relay.direction = digitalio.Direction.OUTPUT

    settings_file = "settings.conf"
    sf = open("settings.conf","r")



    target_tmp = 0
    with open("settings.conf", "r") as sf:
        data = json.load(sf)
        target_tmp = int(data["target_tmp"])

#    print(target_tmp)

    # target_tmp = int(input("Target Temperature: "))

    path = pathlib.Path('/var/tmp/SmokerPi/RasPi/temp.log')
#    print(path.exists())
    if not path.exists():
        with open('/var/tmp/SmokerPi/RasPi/temp.log','w') as f:
            headers = "Time, Temp, Message\n"
            f.write(headers)

    logging.basicConfig(format="%(message)s", filename='/var/tmp/SmokerPi/RasPi/temp.log', level=logging.INFO)

    while True:
        cur_temp = thermocouple.temperature

        if cur_temp >= target_tmp:
            relay.value = False
            m = CustomMessage(temp=cur_temp, time = time.asctime(), fan = "off"
            logging.info(str(m))
        else:
            relay.value = True
            m = CustomMessage(temp=cur_temp, time = time.asctime(), fan = "on"
            logging.info(str(m))

        time.sleep(2)
