#from datetime import datetime
import time
import datastore as ds
import datasender as dsend
from sensehatb import Board

import pandas as pd
#import matplotlib.pyplot as plt 
 

#sample = (sample_id, station_id, parameter, time_at, time_for, value, value1, value2, units)

def main():
    hat = Board()
    parameters = hat.config("parameters")
    #parameters =  "temperatureCPU",
    station_id = hat.config("name")

    samplesDB = ds.Datastore("mem")
    sender = dsend.Datasender()

    sampleFreq = 6 # in seconden (1 minuut)
    collect = True
    lastSendTime = time.time()
    lastCleanTime = time.time()
    sendFreq = 30 # in seconden (5 minuten)
    cleanFreq = 90 # in seconds (15 minuten)

    threshold = 0.05 # in dagen 

    while collect:
        starttime = time.time()

        #clean cache database
        if time.time() - lastCleanTime >= cleanFreq:
            samplesDB.clean_samples_table(threshold)
            lastCleanTime = time.time()
        #send unsend samples
        if time.time() - lastSendTime >= sendFreq:
            newSamples = samplesDB.read_new_samples()  
            result = sender.send_samples(newSamples)
            if result != "error":
                samplesDB.update_sample_status(newSamples, "send")
                lastSendTime = time.time()
        else:
            print(time.time() - lastSendTime)
        #get new samples per parameter
        for parameter in parameters:
            value, units = hat.read(parameter)
            samplesDB.store_sample(station_id, parameter, value, units)
        
        #Show current samples in cache 
        samples = samplesDB.read_all_samples()
        df = pd.DataFrame(samples, columns =['sample_id', 'status', 'station_id', 'parameter', 'time_at', 'time_for', 'values', 'units']) 
        df = df.set_index('status')
        print(df)

        #sleep sampleFreq
        if (sampleFreq- (time.time()-starttime)) > 0:
            time.sleep(sampleFreq- (time.time()-starttime))
            


if __name__ == "__main__":
    main()