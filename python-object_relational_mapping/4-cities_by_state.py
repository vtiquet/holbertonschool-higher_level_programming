#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa, showing the state name.
Requires only one execute() call.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        pass

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
    )

    cursor = db.cursor()

    query = """
        SELECT
            cities.id, cities.name, states.name
        FROM
            cities
        JOIN
            states ON cities.state_id = states.id
        ORDER BY
            cities.id ASC
    """

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
