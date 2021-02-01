import time
from sensehatb import Board
 

def main():
    hat = Board()
    temperature, unit = hat.temperature()
    print(temperature, unit)



if __name__ == "__main__":
    main()