
speed = 1.5

import time
from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause

east1  = LEDBoard(16,13,20,pwm=True)
east2  = LEDBoard(19,26,21,pwm=True)
south1 = LEDBoard(25,24,23,pwm=True)
south2 = LEDBoard(9,22,10,pwm=True)
west1  = LEDBoard(17, 4,14,pwm=True)
west2  = LEDBoard(27,18,15,pwm=True)
north1 = LEDBoard(11, 5,12,pwm=True)
north2 = LEDBoard(8, 6, 7,pwm=True)


while True:
  south1.off()
  north1.on()
  time.sleep(speed)

  west1.off() 
  east1.on()
  time.sleep(speed)

  north1.off()
  south1.on()
  time.sleep(speed)

  east1.off()
  west1.on()
  time.sleep(speed)