#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa."""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    with MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            database=argv[3]) as database:

        cursor = database.cursor()

        query = (
            "SELECT cities.id, cities.name, states.name "
            "FROM cities "
            "INNER JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id ASC;"
        )

        cursor.execute(query)

        elems = cursor.fetchall()

        for elem in elems:
            print(elem)

        cursor.close()
