
import digitalio
import board
import time

relay = digitalio.DigitalInOut(board.D17)

relay.direction = digitalio.Direction.OUTPUT

relay.value = False

