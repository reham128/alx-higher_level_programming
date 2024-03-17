#!/usr/bin/python3
''' script that lists all states from the database hbtn_0e_0_usa'''


import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    if (len(sys.argv) >= 4):
        mydb = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=password, db=database)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")
    states = mycursor.fetchall()
    for result in states:
        print(result)
    mycursor.close()
    mydb.close()
