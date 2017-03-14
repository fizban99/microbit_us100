from us100 import US100
from microbit import sleep


sonar = US100()
while True:
    print('Distance: %.1f' % (sonar.distance_mm()/10))
    print('Temperature: %i' % (sonar.temperature()))
    sleep(1000)
