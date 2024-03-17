#!/usr/bin/python3
""" sys and MySQLdb module importation """
import MySQLdb
import sys


def main():
    """  script that lists all states with a name starting with N (upper N)
        from the database hbtn_0e_0_usa """

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE name = %s
            ORDER BY id""", (sys.argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
