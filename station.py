
import datastore as ds
from sensehatb import Board

#from datetime import datetime
import pandas as pd
#import matplotlib.pyplot as plt 
 

#sample = (sample_id, station_id, parameter, time_at, time_for, value, value1, value2, units)

def main():
    hat = Board()
    parameters = hat.config("parameters")
    station_id = hat.config("name")

    samples = ds.Datastore("lite")
    

    for parameter in parameters:
        value, units = hat.read(parameter)
        samples.store_sample(station_id, parameter, value, units)
        
    samples = samples.read_all_samples()

    # for sample in samples:
    #     print(sample)

    df = pd.DataFrame(samples, columns =['sample_id', 'station_id', 'parameter', 'time_at', 'time_for', 'values', 'units']) 
    df = df.set_index('sample_id')
    print(df)



if __name__ == "__main__":
    main()