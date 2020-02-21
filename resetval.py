#!/usr/bin/python3

# test at simply reading a value from postgres db using psycopg2 python module

import psycopg2

conn=psycopg2.connect(database="valuestore", user="valuestore", password="valuestore", host="localhost", port="5432")

cursor = conn.cursor()

cursor.execute("UPDATE valuetable SET value = 0 where id = 1")
conn.commit()

conn.close()
