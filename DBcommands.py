import sqlite3


class SQL:
    def __init__(self, type):
        self.dbtype = type
        if self.dbtype == "lite":
            self.connection = sqlite3.connect("samples.db")

        elif self.dbtype == "mem":
            self.connection = sqlite3.connect(":memory:")



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