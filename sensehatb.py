import time

import board
#import digitalio
import busio

import adafruit_shtc3


class  Board:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)

        self.sht = adafruit_shtc3.SHTC3(self.i2c)


    def temperature(self):
        value = 37.4
        value_ = self.sht.temperature
        unit = "C"
        return(value, unit)

