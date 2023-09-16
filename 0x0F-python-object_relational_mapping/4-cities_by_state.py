#!/usr/bin/python3
""" This script list all arguments from the database hbtn_0e_4_usa """

from sys import argv
import MySQLdb

if __name__ == '__main__':

    db_user = argv[1]
    db_password = argv[2]
    db_name = argv[3]

    database = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=db_user,
                               password=db_password,
                               db=db_name)

    cursor = database.cursor()

    cursor.execute('SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC')

    for row in cursor.fetchall():
        print(row)
