from controller import TrafficLightSubsystem, PedestrianSubsystem
from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep, time

led_ped_red = led_light(19, True, True)
led_ped_green = led_light(17, False, True)
led_car_red = led_light(3, False, True)
led_car_amber = led_light(5, False, True)
led_car_green = led_light(6, False, True)
ped_button = ped_button(22, True)
buzzer = Ausio Notification(27, True)


def Subsystem_driver():

Subsystem_driver()