#!/usr/bin/python3
"""All cities by state"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Get SQL credentials"""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            charset="utf8"
            )
    cur = db.cursor()
    filter_query = """SELECT cities.name FROM cities
        WHERE cities.state_id LIKE BINARY ( SELECT states.id
        FROM states WHERE states.name LIKE BINARY %s)
        ORDER BY cities.id ASC"""
    cur.execute(filter_query, (state_name,))
    rows = cur.fetchall()
    result = []
    for row in rows:
        result += row
    print(', '.join(result))
    cur.close()
    db.close()
