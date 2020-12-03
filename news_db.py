
import psycopg2
import credentials


def insert(story,datepub):
    """ insert a new centre into the centre table """
    sql = """INSERT INTO news(story,datepub)
             VALUES(%s,%s);"""
    conn = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(host=credentials.host,dbname=credentials.dbname,
        user=credentials.user,password=credentials.password, port=credentials.port)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (story,datepub))
   
     
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
    sql = """SELECT * FROM news
    ORDER BY datepub DESC
    LIMIT 5;"""
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
