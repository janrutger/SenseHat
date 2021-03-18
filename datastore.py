#import sqlite3
from hashlib import sha256
from datetime import datetime

import DBcommands as dbc
import value_formatter as F


class Datastore:
    def __init__(self, type):
        self.dbtype = type
        self.SQL = dbc.SQL(self.dbtype)
        self.SQL.SQLcreate_samples_table()
        
        self.valueformat = F.Formatter()

    def store_sample(self, station_id, parameter, _value, units):
        station_id  = station_id
        parameter   = parameter
        time_at     = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        time_for    = datetime.now().strftime("%Y-%m-%d %H:%M")
        hashstring = station_id + parameter + time_at
        hash       = sha256(hashstring.encode("utf-8")).hexdigest
        sample_id   = hash()
        units       = units

        if len(_value) == 1:
            value  = _value[0]
            value1 = ""
            value2 = ""
        elif len(_value) == 3:
            value  = _value[0]
            value1 = _value[1]
            value2 = _value[2]
        else:
            print("ERRROR, a invalid number of value fields")

        sample = (sample_id, station_id, parameter, time_at, time_for, value, value1, value2, units)
        self.SQL.SQLstore_sample(sample)

    def read_all_samples(self):
        sql_result = self.SQL.SQLread_all_samples()
        result = []
        for row in sql_result:
            # if row[8] == "":
            #     value_ = (row[6],)
            # else:
            #     value_ = (row[6], row[7], row[8])

            value_ = self.valueformat.format(row[3], row[6], row[7], row[8])

            time_at_  = datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S")
            time_for_ = datetime.strptime(row[5], "%Y-%m-%d %H:%M")

            row_ = (row[0], row[1], row[2], row[3], time_at_, time_for_, value_, row[9])
            result.append(row_)
        return(result)


    def read_new_samples(self):
        sql_result = self.SQL.SQLread_new_samples()
        result = []
        for row in sql_result:
            # if row[8] == "":
            #     value_ = (row[6],)
            # else:
            #     value_ = (row[6], row[7], row[8])

            value_ = self.valueformat.format(row[3], row[6], row[7], row[8])

            time_at_  = datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S")
            time_for_ = datetime.strptime(row[5], "%Y-%m-%d %H:%M")

            row_ = (row[0], row[2], row[3], time_at_, time_for_, value_, row[9])
            result.append(row_)
        return(result)

    def update_sample_status(self, samples, newStatus):
        for sample in samples:
            self.SQL.SQLupdate_sample_status(sample[0], newStatus)

    
    def clean_samples_table(self, threshold):
        self.SQL.SQLdelete_samples(threshold)
