import mraa, time, sys


class EdisonCar():
    def __init__(self):
        self.pwm_ina = mraa.Pwm(0)
        self.pwm_inb = mraa.Pwm(14)
        self.pin_stby = mraa.Gpio(15)  # 0 = motor off
        self.pin_ina1 = mraa.Gpio(45)  # 0/1 -> go forward/backward
        self.pin_ina2 = mraa.Gpio(46)
        self.pin_inb1 = mraa.Gpio(47)  # 0/1 -> go left/right
        self.pin_inb2 = mraa.Gpio(48)
        self.period = 1
        self.drivingDir = None

    def enable_pins(self):
        if self.pwm_ina is None:
            raise RuntimeError('pwm_ina could not be initialized')

        if self.pwm_ina.enable(True) is not mraa.SUCCESS:
            raise RuntimeError('error while enabling pwm_ina')

        if self.pwm_inb is None:
            raise RuntimeError('pwm_inb could not be initialized')

        if self.pwm_inb.enable(True) is not mraa.SUCCESS:
            raise RuntimeError('error while enabling pwm_inb')

        if self.pin_stby.dir(mraa.DIR_OUT) is not mraa.SUCCESS:
            raise RuntimeError("Can't set digital pin stdby as output, exiting")

        if self.pin_ina1.dir(mraa.DIR_OUT) is not mraa.SUCCESS:
            raise RuntimeError("Can't set digital pin a1 as output, exiting")

        if self.pin_ina2.dir(mraa.DIR_OUT) is not mraa.SUCCESS:
            raise RuntimeError("Can't set digital pin a2 as output, exiting")

        if self.pin_inb1.dir(mraa.DIR_OUT) is not mraa.SUCCESS:
            raise RuntimeError("Can't set digital pin b1 as output, exiting")

        if self.pin_inb2.dir(mraa.DIR_OUT) is not mraa.SUCCESS:
            raise RuntimeError("Can't set digital pin b2 as output, exiting")

    def enable_motors(self):
        self.pin_stby.write(1)

    def disable_motors(self):
        self.pin_stby.write(0)

    def drive(self, duty_cycle):
        print("driving", duty_cycle)
        self.__accelerate(duty_cycle)
        #self.pwm_ina.write(duty_cycle)

    def brakeold(self, time=1, intensity = 0.7):
        print("breaking!!!")
        i = 0
        self.pwm_ina.period_us(1000)
        self.pwm_ina.write(1.0)
        self.pin_ina1.write(0)
        self.pin_ina2.write(1)


        while(i < 1000):
            self.pin_ina1.write(1)
            self.pin_ina2.write(0)
            self.pin_ina1.write(0)
            self.pin_ina2.write(1)
            i+=1

        self.pin_ina1.write(0)
        self.pin_ina2.write(0)
        self.pwm_ina.write(1.0)

    def brake(self, time1=1, intensity=1.0):
        self.pwm_ina.period_us(1000)
        self.pwm_ina.write(intensity)

        if(self.drivingDir == "forward"):
            for i in [x * 0.1 for x in range(0, int(10 * time1))]:
                self.pin_ina1.write(0)
                self.pin_ina2.write(1)
                time.sleep(0.05)
                self.pin_ina1.write(1)
                self.pin_ina2.write(0)
                time.sleep(0.01)

        elif(self.drivingDir == "backward"):
            for i in [x * 0.1 for x in range(0, int(10 * time1))]:
                self.pin_ina1.write(1)
                self.pin_ina2.write(0)
                time.sleep(0.05)
                self.pin_ina1.write(0)
                self.pin_ina2.write(1)
                time.sleep(0.01)

        self.pin_ina1.write(0)
        self.pin_ina2.write(1)
        self.pwm_ina.period_us(1000)
        self.pwm_ina.write(0)
        time.sleep(time1)
        self.drivingDir = None

    def steer(self, dir):
        '''
        :param dir: string "left" or "write"
        :return:
        '''
        if (dir == "right"):
            self.pin_inb1.write(1)
            self.pin_inb2.write(0)
        elif (dir == "left"):
            self.pin_inb1.write(0)
            self.pin_inb2.write(1)

    def steeringAngle(self, duty_cycle):
        self.pwm_inb.period(self.period)
        self.pwm_inb.write(duty_cycle)

    def setForward(self):
        self.drivingDir = "forward"
        self.pin_ina1.write(1)
        self.pin_ina2.write(0)

    def setbBackward(self):
        self.drivingDir = "backward"
        self.pin_ina1.write(0)
        self.pin_ina2.write(1)

    def __accelerate(self, max_speed=1, intervall=0.1):
        for i in [x * 0.1 for x in range(0, int(10 * max_speed))]:
            self.pwm_ina.write(i)
            time.sleep(intervall)

def main(args):
    if (len(args) > 1):
        granTurino = EdisonCar()
        granTurino.enable_pins()
        granTurino.enable_motors()

        if(args[1] == "f"):
            granTurino.setForward()
        elif(args[1] == "b"):
            granTurino.setbBackward()

        if(args[2] != None):
            drivingtime = float(args[2])
            print("Drivingtime = ", drivingtime)

        granTurino.steer("right")
        granTurino.steeringAngle(1)
        granTurino.drive(1)

        print("sleep 1")
        time.sleep(drivingtime)
        granTurino.steeringAngle(1)

        granTurino.brake()
        time.sleep(5)

        granTurino.disable_motors()
    else:
        print("No driving arguments set")

if __name__ == '__main__':
    main(sys.argv)
