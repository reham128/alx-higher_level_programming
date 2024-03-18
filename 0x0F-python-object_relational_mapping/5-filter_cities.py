#!/usr/bin/python3
''' script that lists all states from the database hbtn_0e_0_usa'''


import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_n = sys.argv[4]

    if (len(sys.argv) >= 5):
        mydb = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=password, db=database)
    mycursor = mydb.cursor()
    sql = """
    SELECT cities.name FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %s ORDER BY cities.id
    """
    mycursor.execute(sql, (state_n,))
    c = mycursor.fetchall()
    c_names = [city[0] for city in c]
    print(', '.join(c_names))
    mycursor.close()
    mydb.close()
