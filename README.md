# xmaastree
Pi-Hut Xmaas Tree

Auf Wunsch von Horst habe ich mich mit diesem Projekt auseinander gesetzt. 

## Was ist die Idee?

- Gemäs Datum leuchten dementsprechend viele Lampen
(am ersten eine, am 2. zwei, usw.)

- Die Lampen sind auf dem Baum Nummeriert, am 1. brennt die erste, am 2. die 1. & die 2...

## Die Umsetzung
Ich bin mit Urs zusammengesessen und habe mit siener Unterstützung zwei versionen deses Scriptes geschrieben. 

__Version 1:__ Diese Version haben wir so geschrieben wie ich es gelöst hätte.

__Version 2:__ Diese Version hat Urs so gelöst wie er es lösen würde. 
[Link](https://github.com/julianbruegger/xmaastree/tree/generisch "Anderer Branch")


Als erstes Importiere ich allen benötigten Module:

```Python
from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
import datetime 
import time
```

Danach definiere ich die bestimmten lampen, und die Sleep dauer.
In diesem falle korespondiert die 11. Lampe auf den Pin Nr. 27 
Mit ```pmw:True``` wird der Pin als besetzt angegeben. 

```python
board11 = LEDBoard(27, pwm=True)

speed = 0.9
```

Nun starten wir eine ```while True`` schleife. Dies ist in einer Art eine unendliche Schleife.

Als erstes fragen wir in dieser Schleife der aktuelle Monat und der aktuelle Tag ab. 

Auch definieren wir die Variable ``anzahl``. Mit dem ``int(day)``wird die Ausgabe von ``day`` in eine Zahl umgewandelt. 


```python
while True:
    
    now = datetime.datetime.now()
    day = now.strftime('%d')
    month = now.strftime('%m')
    anzahl = int(day)
```

Dann begint der einfache teil des Ganzen.

Wir Prüfen nun welches der aktuelle Monat ist, fals dies nicht der Dezember ist, wird eine Errormeldung ausgegeben und das Programm abgebrochen. 

```python
if month != '12':
        print 'Es ist NICHT Dezember. Julians Weihnachtsbaum leuchtet nur im Dezember'
        break
```

Ansonnsten wird das aktuelle Datum abgefragt, je nach Tag gibt es dann ein ``elif`` wleches auf den Tag zutrifft. 

Dort werden dann als erstes alle LED's ausgeschaltet mit ``boardxx.off()``. Danach wird eine Pause gemacht, welche am Anfang definiert worden ist. Zum schluss werden dann die Entsprechenden LED's Angeschaltet mit ``boardxx.on()``
```python
elif (anzahl == 1):
    board01.off()
    time.sleep(speed)
    board01.on()
    time.sleep(speed)
```


