#!/usr/bin/python3
"""
Takes in arguments and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument. But this time,
write one that is safe from MySQL injections!
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        database=argv[3]
    )

    cursor = database.cursor()
    query = (
        "SELECT name "
        "FROM cities "
        "WHERE cities.state_id = ("
            "SELECT id "
            "FROM states "
            "WHERE states.name = %s);"
    )

    cursor.execute(query, (argv[4],))
    elems = cursor.fetchall()

    for elem in elems:
        print(elem)

    cursor.close()
    database.close()
