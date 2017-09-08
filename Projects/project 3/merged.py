# -*- coding: utf-8 -*-
"""
Created on Sat May  6 15:31:29 2017

@author: Rush
"""

import pandas as pd
import sqlite3

connection = sqlite3.connect("project3.db")
cursor = connection.cursor()

impl_str = """INSERT INTO sensorA VALUES (SELECT * from sensorB);"""
cursor.execute(impl_str)
print(cursor.execute("select count(*) from sensorA") )
cursor.commit