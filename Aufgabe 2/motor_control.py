import mraa, time

pwm_ina = mraa.Pwm(0)
pwm_inb = mraa.Pwm(14)

pin_stby = mraa.Gpio(15) # 0 = motor off
pin_ina1 = mraa.Gpio(45) # 0/1 -> go forward/backward
pin_ina2 = mraa.Gpio(46)
pin_inb1 = mraa.Gpio(47) # 0/1 -> go left/right
pin_inb2 = mraa.Gpio(48)

if pwm_inb is None:
    print('pwm_inb could not be initialized')

if pwm_inb.enable(True) is not mraa.SUCCESS:
    print('error while enabling pwm_inb')

pwm_ina.enable(True)

pin_stby.dir(mraa.DIR_OUT)
pin_ina1.dir(mraa.DIR_OUT)
pin_ina2.dir(mraa.DIR_OUT)
pin_inb1.dir(mraa.DIR_OUT)
pin_inb1.dir(mraa.DIR_OUT)

pin_stby.write(0);
pin_ina1.write(1);
pin_ina2.write(0);
pin_inb1.write(1);
pin_inb2.write(0);

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