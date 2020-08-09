#!/usr/bin/python3
""" Selects the cities and states from a database """
from sys import argv
import MySQLdb


def main():
    """ Main function """
    sql_User = argv[1]
    sql_Password = argv[2]
    sql_dbName = argv[3]

    sql_database = MySQLdb.connect(
        host="localhost",
        user=sql_User,
        passwd=sql_Password,
        db=sql_dbName,
        port=3306
    )

    cur = sql_database.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
        JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC")

    # print(cur.fetchall())
    for i in cur.fetchall():
        print(i)

if __name__ == "__main__":
    main()
