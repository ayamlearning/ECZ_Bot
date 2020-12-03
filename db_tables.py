import sys, os
sys.path.append('/var/www/webApp/ecz_bot')

import psycopg2
import credentials

conn = psycopg2.connect(host=credentials.host,dbname=credentials.dbname,
user=credentials.user,password=credentials.password, port=credentials.port)

print ( conn.get_dsn_parameters(),"\n")

def reset():
    """
    Drop all tables of database you given.
    """
    try:
        #Setting auto commit false
        conn.autocommit = True

        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        #cursor.execute("DROP TABLE if exists  centre cascade")
        cursor.execute("DROP TABLE if exists  news cascade")

        print("Tables dropped... ")

        #Commit your changes in the database
        conn.commit()

        #Closing the connection
        conn.close()
    except:
        print ("Error: ", sys.exc_info()[1])

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS centre(
            id SERIAL PRIMARY KEY,
            province VARCHAR(255) NOT NULL,
            district VARCHAR(255) NOT NULL,
            constituency VARCHAR(255) NOT NULL,
            ward VARCHAR(255) NOT NULL,
            polling_district_name VARCHAR(255) NOT NULL,
            polling_station_name VARCHAR(255) NOT NULL,
            phase VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE  IF NOT EXISTS news (
                id SERIAL PRIMARY KEY,
                story VARCHAR NOT NULL,
                datepub date NOT NULL
                )
        """)
        
    try:
        # connect to the PostgreSQL server
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    #reset()
    create_tables()