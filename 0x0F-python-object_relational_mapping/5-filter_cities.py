#!/usr/bin/python3
""" sys and MySQLdb module importation """
import MySQLdb
import sys


def main():
    """  script that takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa """

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT cities.name FROM cities
            INNER JOIN states ON states.id = cities.state_id
            WHERE states.name = %s
            ORDER BY cities.id""", (sys.argv[4],))
    query_rows = cur.fetchall()
    city_names = set(row[0] for row in query_rows)
    print(*city_names, sep=", ")
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
