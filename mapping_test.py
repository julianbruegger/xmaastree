
from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
import datetime 
import time

# Define board / Pins
board01 = LEDBoard(4, pwm=True)
board07 = LEDBoard(5, pwm=True)
board16 = LEDBoard(6, pwm=True)
board22 = LEDBoard(7, pwm=True)
board06 = LEDBoard(8, pwm=True)
board14 = LEDBoard(9, pwm=True)
board08 = LEDBoard(10, pwm=True)
board21 = LEDBoard(11, pwm=True)
board15 = LEDBoard(12, pwm=True)
board03 = LEDBoard(13, pwm=True)
board19 = LEDBoard(14, pwm=True)
board02 = LEDBoard(15, pwm=True)
board09 = LEDBoard(16, pwm=True)
board10 = LEDBoard(17, pwm=True)
board20 = LEDBoard(18, pwm=True)
board18 = LEDBoard(19, pwm=True)
board17 = LEDBoard(20, pwm=True)
board04 = LEDBoard(21, pwm=True)
board24 = LEDBoard(22, pwm=True)
board23 = LEDBoard(23, pwm=True)
board13 = LEDBoard(24, pwm=True)
board05 = LEDBoard(25, pwm=True)
board12 = LEDBoard(26, pwm=True)
board11 = LEDBoard(27, pwm=True)

speed   = 5.0

# Turn off
time.sleep(speed)
board24.on()
time.sleep(speed)
board24.off()
board23.on()
time.sleep(speed)
board23.off()
board22.on()
time.sleep(speed)
board22.off()
board21.on()
time.sleep(speed)
board21.off()
board20.on()
time.sleep(speed)
board20.off()
board19.on()
time.sleep(speed)
board19.off()
board18.on()
time.sleep(speed)
board18.off()
board17.on()
time.sleep(speed)
board17.off()
board16.on()
time.sleep(speed)
board16.off()
board15.on()
time.sleep(speed)
board15.off()
board14.on()
time.sleep(speed)
board14.off()
board13.on()
time.sleep(speed)
board13.off()
board12.on()
time.sleep(speed)
board12.off()
board11.on()
time.sleep(speed)
board11.off()
board10.on()
time.sleep(speed)
board10.off()
board09.on()
time.sleep(speed)
board09.off()
board08.on()
time.sleep(speed)
board08.off()
board07.on()
time.sleep(speed)
board07.off()
board06.on()
time.sleep(speed)
board06.off()
board05.on()
time.sleep(speed)
board05.off()
board04.on()
time.sleep(speed)
board04.off()
board03.on()
time.sleep(speed)
board03.off()
board02.on()
time.sleep(speed)
board02.off()
board01.on()   
time.sleep(speed)