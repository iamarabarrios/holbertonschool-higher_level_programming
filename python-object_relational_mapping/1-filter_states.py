#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    database = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        password=mysql_password,
        database=database_name
    )

    cursor = database.cursor()

    cursor.execute(
        "SELECT * "
        "FROM states "
        "WHERE BINARY name LIKE 'N%' "
        "ORDER BY id ASC"
    )

    for row in cursor:
        print(row)

    cursor.close()
    database.close()
