import time
import datastore as ds
from sensehatb import Board

 

def main():
    hat = Board()
    parameters = hat.config("parameters")
    station_id = hat.config("name")

    samples = ds.Datastore("lite")
    

    for parameter in parameters:
        value, units = hat.read(parameter)
        samples.store_sample(station_id, parameter, value, units)
        
    samples = samples.read_all_samples()
    for sample in samples:
        print(sample)




if __name__ == "__main__":
    main()