#!/usr/bin/python3
""" This script lists all states with a name starting with N """

if __name__ == '__main__':
    
    from sys import argv
    import MySQLdb

    db_user = argv[1]
    db_password = argv[2]
    db_name = argv[3]

    database = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=db_user,
                               password=db_password,
                               db=db_name)

    cursor = database.cursor()

    cursor.execute('SELECT id, name FROM states\
                   ORDER BY states.id ASC')
    
    for row in cursor.fetchall():
        if row[1][0] == 'N':
            print(row)

