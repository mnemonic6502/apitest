def valtestfunc():
    # test at simply reading a value from postgres db using psycopg2 python module

    import psycopg2

    connect = psycopg2.connect(database="valuestore", user="valuestore", password="valuestore", host="localhost", port="5432")
    connect.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE)
    cursor = connect.cursor()

    cursor.execute("SELECT value FROM valuetable")
    valreturned = cursor.fetchone()
    connect.close()

    return(valreturned[0])

def valincfunc():
    # increments value in psql valuetable

    # But first pull back the prior value

    valreturned=valtestfunc()

    valadded = valreturned + 1

    #now update the db with the new val

    import psycopg2

    connect = psycopg2.connect(database="valuestore", user="valuestore", password="valuestore", host="localhost", port="5432")
    connect.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE)
    cursor = connect.cursor()

    cursor.execute('UPDATE valuetable SET value = %s where id = 1', [valadded])
    connect.commit()

    connect.close()
