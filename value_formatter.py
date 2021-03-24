


#"temperatureCPU", "temperature", "Humidity",
# "temperature2", "pressure",
# "lux", "color-temperature", "color-rgb",
# "acceleration", "gyro", "magnetic",
# "external1", "external2", "external3", "external4"

class Formatter:
    def __init__(self):
        self.temperatures = ["temperatureCPU", "temperature", "temperature2"]
        self.humidities   = ["Humidity"]
        self.pressures    = ["pressure"]
        self.lux          = ["lux"]
        self.colortemp    = ["color-temperature"]
        self.rgb          = ["color-rgb"]
        self.xyz          = ["acceleration", "gyro", "magnetic"]
        self.external     = ["external1", "external2", "external3", "external4"]



    def format(self, paraameter, value, value1, value2):
        if paraameter in self.temperatures:
            symbol = "T"
            value  = {symbol : value}
            return(value)
        if paraameter in self.humidities:
            symbol = "H"
            value  = {symbol : value}
            return(value)
        if paraameter in self.pressures:
            symbol = "P"
            value  = {symbol : value}
            return(value)
        if paraameter in self.lux:
            symbol = "L"
            value  = {symbol : value}
            return(value)
        if paraameter in self.colortemp:
            symbol = "T"
            value  = {symbol : value}
            return(value)
        if paraameter in self.rgb:
            symbol = "red"
            symbol1 = "green"
            symbol2 = "blue"
            value  = {symbol : value, symbol1 : value1, symbol2 : value2}
            return(value)
        if paraameter in self.xyz:
            symbol = "X-ax"
            symbol1 = "Y-ax"
            symbol2 = "Z-ax"
            value  = {symbol : value, symbol1 : value1, symbol2 : value2}
            return(value)
        if paraameter in self.external:
            symbol = "ex"
            value  = {symbol : value}
            return(value)