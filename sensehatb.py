import time

import board
#import digitalio
import busio

import adafruit_shtc3
from gpiozero import CPUTemperature



class  Board:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.station_id = "station1"

        self.cpu = CPUTemperature()
        #self.sht = adafruit_shtc3.SHTC3(self.i2c)

    def config(self, part):
        if part == "parameters":
            return(["temperature", "temperatureCPU"])
        if part == "name":
            return(self.station_id)

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