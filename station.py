import time
from sensehatb import Board
 

def main():
    hat = Board()

    temperature, unit = hat.read("temperature")
    print(temperature, unit)

    temperatureCPU, unit = hat.read("temperatureCPU")
    print(temperatureCPU, unit)



if __name__ == "__main__":
    main()