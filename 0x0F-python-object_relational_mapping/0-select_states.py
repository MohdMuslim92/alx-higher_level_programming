#!/usr/bin/python3
import MySQLdb
from sys import argv


def main():
    if len(argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(argv[0]))
        return
    user = argv[1]
    password = argv[2]
    db_name = argv[3]
    con = None
    cursor = None
    try:
        con = MySQLdb.connect(
                host="localhost",
                port=3306, user=user, password=password, db=db_name)
        cursor = con.cursor()
        query = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print("Error connecting to the MySQL server: ", e)
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()


if __name__ == "__main__":
    main()
