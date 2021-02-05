import time

import board
#import digitalio
import busio

from gpiozero import CPUTemperature
import adafruit_shtc3
import adafruit_lps2x
import adafruit_tcs34725
import adafruit_icm20x
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn




class  Board:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.station_id = "station1"

        self.cpu = CPUTemperature()
        #self.sht = adafruit_shtc3.SHTC3(self.i2c)

    def config(self, part):
        if part == "parameters":
            return(["temperatureCPU", "temperature"])
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