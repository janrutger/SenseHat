#import sqlite3
from hashlib import sha256
from datetime import datetime

import SQLcmds as database


class Datastore:
    def __init__(self, type):
        self.dbtype = type
        self.SQL = database.SQL(self.dbtype)
        self.SQL.SQLcreate_samples_table()
        

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
            if row[7] == "":
                value_ = (row[5])
            else:
                value_ = (row[5], row[6], row[7])

            time_at_  = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
            time_for_ = datetime.strptime(row[4], "%Y-%m-%d %H:%M")

            row_ = (row[0], row[1], row[2], time_at_, time_for_, value_, row[8])
            result.append(row_)
        return(result)
           

    