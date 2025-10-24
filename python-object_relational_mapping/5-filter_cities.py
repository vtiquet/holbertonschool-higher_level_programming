#!/usr/bin/python3
"""
Lists all cities of a given state, safe from MySQL injection,
using the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        pass

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    query = """
        SELECT
            cities.name
        FROM
            cities
        JOIN
            states ON cities.state_id = states.id
        WHERE
            states.name = %s
        ORDER BY
            cities.id ASC
    """

    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    cursor.close()
    db.close()
