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

duty_cycle = 0.1
period = 1
pin_stby.write(1)
value = 0.1

i = 0

while (i < 500):
    i += 1
    pin_ina1.write(0)
    pin_ina2.write(1)
    pwm_ina.period(period)
    pwm_ina.write(value)

    pin_inb1.write(1)
    pin_inb2.write(0)
    pwm_inb.period(period)
    pwm_inb.write(0.3)
    time.sleep(0.01)

pin_stby.write(0)