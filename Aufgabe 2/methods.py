

def drive(duty_cycle):
    pin_stby.write(1)
    pwm_ina.write(duty_cycle)

def steer(dir):
    '''
    :param dir: string "left" or "write"
    :return: 
    '''
    if(dir =="left"):
        pin_inb1.write(1)
        pin_inb2.write(0)
    elif(dir == "right"):
        pin_inb1.write(0)
        pin_inb2.write(1)

def steeringAngle(duty_cycle):
    pwm_inb.period(period)
    pwm_inb.write(duty_cycle)

def setForward():
    pin_ina1.write(1)
    pin_ina2.write(0)

def setbBackward():
    pin_ina1.write(0)
    pin_ina2.write(1)

def brake():
    i = 0
    while(i < 1000):
        pin_inb1.write(1)
        pin_inb2.write(0)
        pwm_inb.period(period)
        pwm_inb.write(1.0)
        pin_inb1.write(0)
        pin_inb2.write(1)
        pwm_inb.period(period)
        pwm_inb.write(1.0)
        i += 1