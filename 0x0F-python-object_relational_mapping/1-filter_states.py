#!/usr/bin/python3
""" Selects the states from an SQL database that start with N """
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

    cur.execute("SELECT id, name FROM states ORDER BY states.id ASC")

    # print(cur.fetchall())
    for i in cur.fetchall():
        if i[1][0] is 'N':
            print(i)

if __name__ == "__main__":
    main()
