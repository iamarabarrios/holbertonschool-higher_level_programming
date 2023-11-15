#!/usr/bin/python3
"""Takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    if len(argv) != 5:
        print(
            "Usage: {} username password database state_name"
            .format(argv[0])
        )
        exit(1)

    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_name_searched = argv[4]

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
        "WHERE BINARY name = '{}' "
        "ORDER BY id ASC".format(state_name_searched)
    )

    for row in cursor:
        print(row)

    cursor.close()
    database.close()
