#!/usr/bin/python3
"""
   Takes in the name of a state as an argument
   and lists all cities of that state,
   using the database hbtn_0e_4_usa
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
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s"
    )

    cursor.execute(query, (argv[4],))

    elems = cursor.fetchall()

    printArr = [elem[0] for elem in elems]
    print(*printArr, sep=', ')

    cursor.close()
    database.close()
