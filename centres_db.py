import sys, os
sys.path.append('/var/www/webApp/webApp')

import psycopg2
import credentials


def insert(province,district,constituency,ward,polling_district_name
    ,polling_station_name,phase):
    """ insert a new centre into the centre table """
    sql = """INSERT INTO centre(province,district,constituency,ward,polling_district_name,polling_station_name,phase)
             VALUES(%s,%s,%s,%s,%s,%s,%s);"""
    conn = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(host=credentials.host,dbname=credentials.dbname,
        user=credentials.user,password=credentials.password, port=credentials.port)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (province,district,constituency,ward,polling_district_name,polling_station_name,phase))
   
     
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def get_all():
    """ view all centre """
    sql = """SELECT * FROM centre;"""
    conn = None
    my_records=[]
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(host=credentials.host,dbname=credentials.dbname,
        user=credentials.user,password=credentials.password, port=credentials.port)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        my_records = cur.fetchall()

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

        return my_records

def get_all_constituencies():
    """ view all centre """
    sql = """SELECT DISTINCT constituency FROM centre;"""
    conn = None
    my_records=[]
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(host=credentials.host,dbname=credentials.dbname,
        user=credentials.user,password=credentials.password, port=credentials.port)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        my_records = cur.fetchall()

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

        return my_records


def search_constituency_and_ward(constituency,ward):
    """ view all centre """
    sql = """SELECT * FROM centre
    WHERE (lower(constituency)=lower('{}') AND lower(ward)=lower('{}'));""".format(constituency,ward)
    conn = None
    my_records=[]
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(host=credentials.host,dbname=credentials.dbname,
        user=credentials.user,password=credentials.password, port=credentials.port)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        my_records = cur.fetchall()

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

        return my_records


def search_district(district):
    """ view all centre """
    sql = """SELECT * FROM centre
    WHERE (lower(district)=lower('{}'));""".format(district)
    conn = None
    my_records=[]
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(host=credentials.host,dbname=credentials.dbname,
        user=credentials.user,password=credentials.password, port=credentials.port)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        my_records = cur.fetchall()

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

        return my_records

def search_constituency(constituency,phase):
    """ view all centre """
    sql = """SELECT * FROM centre
    WHERE (lower(constituency) LIKE lower('{}') AND phase LIKE '%{}%') 
    LIMIT 10;""".format(constituency,phase)
    conn = None
    my_records=[]
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(host=credentials.host,dbname=credentials.dbname,
        user=credentials.user,password=credentials.password, port=credentials.port)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        my_records = cur.fetchall()

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

        return my_records

def search_ward(ward):
    """ view all centre """
    sql = """SELECT * FROM centre
    WHERE (lower(ward)=lower('{}'));""".format(ward)
    conn = None
    my_records=[]
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(host=credentials.host,dbname=credentials.dbname,
        user=credentials.user,password=credentials.password, port=credentials.port)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        my_records = cur.fetchall()

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

        return my_records



if __name__ == '__main__':
   insert('lusaka','lusaka','chawama','ward 2','chawama basic school','chawama basic school',1)
   print(len(get_all()))
   #print(len(search_by_constituency_and_ward('chawama','ward 2')))
