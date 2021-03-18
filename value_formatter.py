


#"temperatureCPU", "temperature", "Humidity",
# "temperature2", "pressure",
# "lux", "color-temperature", "color-rgb",
# "acceleration", "gyro", "magnetic",
# "external1", "external2", "external3", "external4"

class Formatter:
    def __init__(self):
        self.temperature = ["temperatureCPU", "temperature", "temperature2"]


    def format(self, paraameter, value, value1, value2):
        if paraameter in self.temperature:
            symbol = "T"
            value  = {symbol : value}
            return(value)