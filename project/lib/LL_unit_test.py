from led_light import Led_Light
from time import sleep, time

led = Led_Light(3, flashing=True, debug=True)

print("Testing on()")
led.on()
if led.value == 1:
    print(".off() method passed")

print("Testing off()")
led.on()
if led.value == 0:
    print(".off() method passed")

print("Testing Toggle")
led.toggle()
if led.value ==0:
    print("test passed Toggle: on")

    print("Testing Toggle")
led.toggle()
if led.value ==1:
    print("test passed Toggle: off")


