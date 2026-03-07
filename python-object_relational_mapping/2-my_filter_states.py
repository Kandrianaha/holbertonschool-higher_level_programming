#!/usr/bin/python3
"""Lists all states matching the name given as argument"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC",
        (state_name_searched,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
