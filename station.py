import time
from sensehatb import Board as hat
 

def main():
    temperature, unit = hat.temperature()
    print(temperature, unit)



if __name__ == "__main__":
    main()