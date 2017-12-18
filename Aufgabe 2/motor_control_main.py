import EdisonCar

if __name__ == '__main__':
    granTurino = EdisonCar()
    granTurino.enable_pins()
    granTurino.enable_motors()
    granTurino.setForward()
    granTurino.drive(0.5)
    granTurino.brake()
    granTurino.disable_motors()