#!/usr/bin/python3
"""Lists all states matching the name 
protecting from MySQL injections"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    query = (
        "SELECT * FROM states"
        " WHERE BINARY name = %s"
        " ORDER BY id ASC"
    )

    cursor.execute(query, (sys.argv[4],))
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
