import mraa, time


class EdisonCar():
    def __init__(self):
        self.pwm_ina = mraa.Pwm(0)
        self.pwm_inb = mraa.Pwm(14)
        self.pin_stby = mraa.Gpio(15) # 0 = motor off
        self.pin_ina1 = mraa.Gpio(45) # 0/1 -> go forward/backward
        self.pin_ina2 = mraa.Gpio(46)
        self.pin_inb1 = mraa.Gpio(47) # 0/1 -> go left/right
        self.pin_inb2 = mraa.Gpio(48)
        self.period = 1

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
        self.pwm_ina.write(duty_cycle)

    def brake(self):
        i = 0
        while (i < 1000):
            self.pin_inb1.write(1)
            self.pin_inb2.write(0)
            self.pwm_inb.period(self.period)
            self.pwm_inb.write(1.0)
            self.pin_inb1.write(0)
            self.pin_inb2.write(1)
            self.pwm_inb.period(self.period)
            self.pwm_inb.write(1.0)
            i += 1

    def steer(self, dir):
        '''
        :param dir: string "left" or "write"
        :return:
        '''
        if (dir == "left"):
            self.pin_inb1.write(1)
            self.pin_inb2.write(0)
        elif (dir == "right"):
            self.pin_inb1.write(0)
            self.pin_inb2.write(1)

    def steeringAngle(self, duty_cycle):
        self.pwm_inb.period(self.period)
        self.pwm_inb.write(duty_cycle)

    def setForward(self):
        self.pin_ina1.write(1)
        self.pin_ina2.write(0)

    def setbBackward(self):
        self.pin_ina1.write(0)
        self.pin_ina2.write(1)