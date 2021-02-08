
import datastore as ds
import datasender as sender
from sensehatb import Board

import pandas as pd
#import matplotlib.pyplot as plt 
 

#sample = (sample_id, station_id, parameter, time_at, time_for, value, value1, value2, units)

def main():
    hat = Board()
    parameters = hat.config("parameters")
    station_id = hat.config("name")

    samplesDB = ds.Datastore("mem")
    

    for parameter in parameters:
        value, units = hat.read(parameter)
        samplesDB.store_sample(station_id, parameter, value, units)
        
    samples = samplesDB.read_all_samples()

    sender.send_samples(samples)
    

    df = pd.DataFrame(samples, columns =['sample_id', 'station_id', 'parameter', 'time_at', 'time_for', 'values', 'units']) 
    df = df.set_index('sample_id')
    print(df)



if __name__ == "__main__":
    main()