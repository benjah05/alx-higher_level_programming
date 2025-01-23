#!/usr/bin/python3
"""Filter states by user input"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Get SQL credentials"""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    searched_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            charset="utf8"
            )
    cur = db.cursor()
    filter_query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(searched_name)
    cur.execute(filter_query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
