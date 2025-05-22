from machine import Pin
from time import sleep

sleep(0.1)

led_pin = 25

led = Pin(led_pin, Pin.out)

while true:
    led.value(True)
    sleep(1)
    led.value(False)

    
    sleep(1)
