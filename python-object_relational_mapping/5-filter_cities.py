""" lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    cur.execute(query, (state,))

    rows = cur.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    cur.close()
    db.close()
    