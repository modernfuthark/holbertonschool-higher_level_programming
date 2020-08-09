#!/usr/bin/python3
""" Selects the cities and states from a database,
filtered with a user input
"""
from sys import argv
import MySQLdb


def main():
    """ Main function """
    sql_User = argv[1]
    sql_Password = argv[2]
    sql_dbName = argv[3]
    search = argv[4]

    sql_database = MySQLdb.connect(
        host="localhost",
        user=sql_User,
        passwd=sql_Password,
        db=sql_dbName,
        port=3306
    )

    cur = sql_database.cursor()

    cur.execute("SELECT cities.name FROM cities\
        JOIN states ON cities.state_id = states.id\
            WHERE states.name = %(search)s\
            ORDER BY cities.id ASC", {'search': search})

    # print(cur.fetchall())
    # for i in cur.fetchall():
    #   print(i[0], end=", ")
    print(", ".join(i[0] for i in cur.fetchall()))

if __name__ == "__main__":
    main()
