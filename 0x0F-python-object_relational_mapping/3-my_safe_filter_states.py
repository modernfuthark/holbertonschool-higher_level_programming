#!/usr/bin/python3
""" Selects the states from an SQL database that match a user input
    Protects against SQL injection
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

    cur.execute("SELECT id, name FROM states \
        WHERE states.name = %(search)s \
        ORDER BY states.id ASC", {'search': search})

    # self note: could also be written as:
    #  cur.execute("SELECT id, name FROM states \
    # WHERE states.name = %s ORDER BY states.id ASC",
    # (search, ))

    # print(cur.fetchall())
    for i in cur.fetchall():
        if i[1] == search:
            print(i)

if __name__ == "__main__":
    main()
