
from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
import datetime 
import time

speed = 0.3

while True:
    
    now = datetime.datetime.now()
    day = now.strftime('%d')
    month = now.strftime('%m')
    anzahl = int(day)
    boards = []
  
    if month != '12':
        print 'Es ist NICHT Dezember.'
        break

    for i in range(anzahl):
        led = i + 4
        board = LEDBoard(led, pwm=False)
        boards.append(board)

    for board in boards:
        board.off()
        time.sleep(speed)
        board.on()
        time.sleep(speed)