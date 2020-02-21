#!/usr/bin/python3

from flask import Flask
import valuemod

app = Flask(__name__)

@app.route('/api/valcheck')
def valcheck():
    valteststr="{}".format(valuemod.valtestfunc()) # coerce int to str conversion from module function to enable decorator return str
    return valteststr

@app.route('/api/valinc')
def valincrement():
    # get prior value before increment
    valteststr="{}".format(valuemod.valtestfunc()) # coerce int to str conversion from module function to enable decorator return str

    # increment value, as per challenege spec
    valuemod.valincfunc() 

    return valteststr

if __name__ == "__main__":
    app.run()
