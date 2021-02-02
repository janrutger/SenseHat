import time
from sensehatb import Board
 

def main():
    hat = Board()

    parameters = hat.config()

    for parameter in parameters:
        value, unit = hat.read(parameter)
        if len(value) == 1:
            print(parameter, value[0], unit)
        else:
            print(parameter, value[0], value[1], value[2], unit)



if __name__ == "__main__":
    main()