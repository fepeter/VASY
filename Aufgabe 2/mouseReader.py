
from evdev import InputDevice, categorize, ecodes
from thread import start_new_thread
import sys

class mouseReader():
    def __init__(self, callback_Method, Mousedevice):
        self.callback = callback_Method
        self.device = InputDevice(Mousedevice)
        print("Using:")
        print(self.device)
        start_new_thread(self.readMouse, (99,))

    def readMouse(self, a):

        for event in self.device.read_loop():
            # code 00 --> x - achse
            # code 01 --> y - achse
            # type 02 --> move value
            # value --> ticks in + / -
            if (int(event.type) == 2):
                print(event.code)
                if (int(event.code) == 0):
                    # move on X-axis
                    #print("move X with", event.value)
                    self.callback("x", int(event.value))
                elif (int(event.code) == 1):
                    # move on Y-axis
                    #print("move Y with", int(event.value))
                    self.callback("y", int(event.value))