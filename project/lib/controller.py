from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from project.lib.audio_notification import Audio_Notification
from time import sleep, time

class TrafficLightSubsystem:
    def __init__(self, red, amber, green, debug=False):
        self.__red = red
        self.__amber = amber
        self.__green = green
        self.__debug = debug

    def show_red(self):
        if self.__debug:
            print ("traffic: Red ON")
        self.__red.on()
        self.__amber.off()
        self.__green.off()

    def show_amber(self):
        if self.__debug:
            print ("traffic: Amber ON")
        self.__red.off()
        self.__amber.on()
        self.__green.off()

    def show_green(self):
        if self.__debug:
            print ("traffic: Green ON")
        self.__red.off()
        self.__amber.off()
        self.__green.on()

class PedestrianSubsystem:
    def __init__(self, red, green, button, buzzer, debug=False):
        self.__red =red
        self.__green = green
        self.__button = button
        self.__buzzer = buzzer
        self.__debug = debug

    def show_stop(self):
        if self.__debug:
            print("Pedestrian: Red ON")
        self.__red.on()
        self.__green.off()
        self.__buzzer.warning_off()

    def show_walk(self):
        if self.__debug:
            print("Pedestrian: Green ON")
        self.__red.off()
        self.__green.on()
        self.__buzzer.warning_off()

    def show_warning(self):
        if self.__debug:
            print("Pedestrian: Red FLASHING")
        self.__red.flashing()
        self.__green.off()
        self.__buzzer.warning_on()

    def button_pressed(self):
        return self.__button.button_state()

    def reset_button(self):
        return self.__button.button_state(False)
    

class Controller:
    def __init__(self, ped_red, ped_green, car_amber, car_red, car_green, button, buzzer, debug):
        self.__traffic_lights = TrafficLightSubsystem(car_red, car_amber, car_green, debug)
        self.__pedestrian_lights = PedestrianSubsystem(ped_red, ped_green, button, buzzer, debug)
        self.__debug = debug
        self.state = "IDLE"
        self.last_state_change = time()

    def set_idle_state(self):
        if self.__debug:
            print("System: IDLE state")
        self.__pedestrian_lights.show_stop()
        self.__traffic_lights.show_green()

    def set_change_state(self):
        if self.__debug:
            print("System: CHANGE state")
        self.__pedestrian_lights.show_stop()
        self.__traffic_lights.show_amber()
    
    def set_walk_state(self):
        if self.__debug:
            print("System: WALK state")
        self.__pedestrian_lights.show_walk()
        self.__traffic_lights.show_red()
    
    def set_warning_state(self):
        if self.__debug:
            print("System: WARNING state")
        self.__pedestrian_lights.show_warning()
        self.__traffic_lights.show_red()
    
    def error_state(self):
        if self.__debug:
            print("System: ERROR state")
        self.__pedestrian_lights.show_warning()
        self.__traffic_lights.show_error()  #needs amber flashing