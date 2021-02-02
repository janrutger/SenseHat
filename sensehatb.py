import time

import board
#import digitalio
import busio

import adafruit_shtc3
from gpiozero import CPUTemperature


class  Board:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)

        self.cpu = CPUTemperature()
        #self.sht = adafruit_shtc3.SHTC3(self.i2c)

    def config(self):
        return(["temperature", "temperatureCPU"])

    def read(self, parameter):
        if parameter == "temperatureCPU":
            value = (self.cpu.temperature,)
            unit = "C"
            return(value, unit)
        elif parameter == "temperature":
            value = (37.4, 8, 45)
            #value_ = self.sht.temperature
            unit = "C"
            return(value, unit)