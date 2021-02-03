import sqlite3
from hashlib import sha256
from datetime import datetime




class Datastore:
    def __init__(self, type):
        self.dbtype = type
        if self.dbtype == "lite":
            self.connection = sqlite3.connect("samples.db")
            self.SQLcreate_samples_table()

        elif self.dbtype == "mem":
            self.connection = sqlite3.connect(":memory:")
            self.SQLcreate_samples_table()
        

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
        self.SQLstore_sample(sample)

    def read_all_samples(self):
        sql_result = self.SQLread_all_samples()
        result = []
        for row in sql_result:
            if row[7] == "":
                value_ = (row[5],)
            else:
                value_ = (row[5], row[6], row[7])
            row_ = (row[1], row[2], row[3], row[4], value_, row[8])
            result.append(row_)
        return(result)
           

    def SQLread_all_samples(self):
        if self.dbtype == "lite" or self.dbtype == "mem":
            sql = """SELECT sample_id, station_id, parameter, time_at, time_for, value, value1, value2, units FROM samplestable"""
            result = self.connection.execute(sql)
            result = result.fetchall()
            return(result)


    def SQLstore_sample(self, sample):
        if self.dbtype == "lite" or self.dbtype == "mem":
            sql = """INSERT INTO samplestable (sample_id, station_id, parameter, time_at, time_for, value, value1, value2, units) VALUES (?,?,?,?,?,?,?,?,?)"""
            self.connection.execute(sql, sample)
            self.connection.commit()



    def SQLcreate_samples_table(self):
        if self.dbtype == "lite" or self.dbtype == "mem":
            self.connection.execute(
                """create table if not exists samplestable (
                        sample_id  text PRIMARY KEY, 
                        station_id text NOT NULL,
                        parameter  text NOT NULL,
                        time_at  text NOT NULL,
                        time_for text NOT NULL,
                        value  real NOT NULL,
                        value1 real DEFAULT NULL,
                        value2 real DEFAULT NULL,
                        units  text NOT NULL 
                        ) 
                    """)

    

