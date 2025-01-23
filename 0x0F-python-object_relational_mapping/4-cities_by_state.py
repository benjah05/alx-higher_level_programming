#!/usr/bin/python3
"""Cities by states"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Get SQL credentials"""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            charset="utf8"
            )
    cur = db.cursor()
    filter_query = """SELECT cities.id, cities.name, states.name
    FROM cities, states WHERE cities.state_id = states.id ORDER BY cities.id ASC"""
    cur.execute(filter_query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
