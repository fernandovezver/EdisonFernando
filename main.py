import random

import pyupm_grove as grove
import pyupm_buzzer as upmBuzzer
import pyupm_i2clcd as lcd
import time

button = grove.GroveButton(4)
count = 0;




while 1:
  check = True
    if button.value() AND check:
      print("Prueba")
      count+=1
      print(count)
      check=False
      time.sleep(.1)
    elif not(button.value) and not(check):
      check=True

del button