from led_light import Led_Light
from project.lib.controller import TrafficLightSubsystem, PedestrianSubsystem
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep, time

led_ped_red = Led_Light(19, True, True)
led_ped_green = Led_Light(17, False, True)
led_car_red = Led_Light(3, False, True)
led_car_amber = Led_Light(5, False, True)
led_car_green = Led_Light(6, False, True)
pedestrain_button = Pedestrian_Button(22, True)
buzzer = Audio_Notification(27, True)

red = Led_Light(3, False, True)
amber = Led_Light(6, False, True)
green = Led_Light(9, False, True)

light = TrafficLightSubsystem(red, amber, green, False)

def Traffic_Subsystem_driver():
    #Test Red Light
    print("Testing Traffic Light In 5 Seconds")
    sleep(5)
    light.show_red()
    print("Pass if: Red ON, Amber OFF & Green OFF")
    sleep(10)
    
    #Test Green Light
    print("Testing Traffic Light In 5 Seconds")
    sleep(5)
    light.show_green()
    print("Pass if: Red OFF & Amber OFF, Green ON")
    sleep(10)
    
    #Test Amber Light
    print("Testing Traffic Light In 5 Seconds")
    sleep(5)
    light.show_amber()
    print("Pass if: Red OFF, Amber ON, Green OFF")
    sleep(10)


Traffic_Subsystem_driver()