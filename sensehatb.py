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
        # self.sht = adafruit_shtc3.SHTC3(self.i2c)
        # self.lps = adafruit_lps2x.LPS22(self.i2c, 0x5c)

        # self.tcs = adafruit_tcs34725.TCS34725(self.i2c)
        # self.tcs.integration_time = 200

        # self.icm = adafruit_icm20x.ICM20948(self.i2c, 0x68)
        # self.ads = ADS.ADS1015(self.i2c)

    def config(self, part):
        if part == "parameters":
            return(["temperatureCPU", "temperature", "Humidity",
            "temperature2", "pressure",
            "lux", "color-temperature", "color-rgb",
            "acceleration", "gyro", "magnetic",
            "external1", "external2", "external3", "external4"])
        if part == "name":
            return(self.station_id)

    def read(self, parameter):
        if parameter == "temperatureCPU":
            value = (self.cpu.temperature,)
            unit = "C"
            return(value, unit)
        elif parameter == "temperature":
            value = (self.sht.temperature,)
            unit = "C"
            return(value, unit)
        elif parameter == "Humidity":
            value = (self.sht.relative_humidity,)
            unit = "%"
            return(value, unit)
        elif parameter == "temperature2":
            value = (self.lps.temperature,)
            unit = "C"
            return(value, unit)
        elif parameter == "pressure":
            value = (self.lps.pressure,)
            unit = "hPa"
            return(value, unit)
        elif parameter == "lux":
            value = (self.tcs.lux,)
            unit = "lux"
            return(value, unit)
        elif parameter == "color-temperature":
            value = (self.tcs.color_temperature,)
            unit = "K"
            return(value, unit)
        elif parameter == "color-rgb":
            value = (self.tcs.color_rgb_bytes)
            unit = "RGB"
            return(value, unit)
        elif parameter == "acceleration":
            value = (self.icm.acceleration)
            unit = "m/s²"
            return(value, unit)
        elif parameter == "gyro":
            value = (self.icm.gyro)
            unit = "Rads/s"
            return(value, unit)
        elif parameter == "magnetic":
            value = (self.icm.magnetic)
            unit = "uT"
            return(value, unit)
        elif parameter == "external1":
            chan = AnalogIn(self.ads, ADS.P0)
            value = (chan.voltage,)
            unit = "mV"
            return(value, unit)
        elif parameter == "external2":
            chan = AnalogIn(self.ads, ADS.P1)
            value = (chan.voltage,)
            unit = "mV"
            return(value, unit)
        elif parameter == "external3":
            chan = AnalogIn(self.ads, ADS.P2)
            value = (chan.voltage,)
            unit = "mV"
            return(value, unit)
        elif parameter == "external4":
            chan = AnalogIn(self.ads, ADS.P3)
            value = (chan.voltage,)
            unit = "mV"
            return(value, unit)