#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        pass

    try:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]

        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
            charset="utf8"
        )

        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name = '{}' " \
                "ORDER BY id ASC".format(state_name)

        cursor.execute(query)

        for row in cursor.fetchall():
            print(row)

        cursor.close()
        db.close()

    except Exception as e:
        pass
