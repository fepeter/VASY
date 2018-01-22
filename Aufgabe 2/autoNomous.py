#!/usr/bin/env python
import mraa, time, sys, serial, io
from evdev import InputDevice, categorize, ecodes
from thread import start_new_thread
from mouseReader import mouseReader
from EdisonCar import EdisonCar



class controller():


    def __init__(self):
        self.moveValX = 6000
        self.moveValY = 6000
        self.granTurino = EdisonCar()
        self.granTurino.enable_pins()
        self.granTurino.enable_motors()
        self.granTurino.setupSerial()
        #self.granTurino.listenToTheAir()
        mouse = mouseReader(self.callback, '/dev/input/event2')
        self.old = True
        self.stop = False
        self.totalcountY = 0
        self.totalcountX = 0
        self.gogogo()



    def callback(self, dir, value):
        #print("asdf", dir, abs(value))
        if(dir == "x"):
            self.moveValX -= abs(value)
            self.totalcountX += abs(value)
            if(self.moveValX < 0):
                self.moveValX = 0
                self.stop = True
                print("STOP X")
        else:
            self.moveValY -= abs(value)
            self.totalcountY += abs(value)
            if (self.moveValY < 0):
                self.moveValY = 0
                self.stop = True
                print("STOP Y")

    def gogogo(self):
        self.totalcountY = 0
        self.totalcountX = 0
        while(not self.stop):
            print("moving",self.moveValX, self.moveValY, self.totalcountX, self.totalcountY)

            if(not self.old):
                self.granTurino.setForward()
                self.granTurino.drive(0.8)
                self.old = False

        self.granTurino.brake()


def main(args):

    cont = controller()




    #granTurino = EdisonCar()
    #granTurino.enable_pins()
    #granTurino.enable_motors()
    #granTurino.setupSerial()
    #granTurino.listenToTheAir()
#
    #granTurino.disable_motors()

if __name__ == '__main__':
    main(sys.argv)