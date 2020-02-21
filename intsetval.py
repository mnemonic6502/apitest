#!/usr/bin/python3

# test at simply reading a value from postgres db using psycopg2 python module

import psycopg2

conn=psycopg2.connect(database="valuestore", user="valuestore", password="valuestore", host="localhost", port="5432")

cursor = conn.cursor()

cursor.execute("INSERT into valuetable (id, value) VALUES ('1','0')")
conn.commit()

conn.close()
