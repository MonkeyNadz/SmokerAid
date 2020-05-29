import digitalio
import board
import time

relay = digitalio.DigitalInOut(board.D17)

relay.direction = digitalio.Direction.OUTPUT

while True:
	relay.value = True
	time.sleep(1)
	relay.value = False
	time.sleep(1)
