#!/usr/bin/python3
""" sys and MySQLdb module importation """
import MySQLdb
import sys


def main():
    """ script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument SAFERMODE """

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE name = %s
            ORDER BY id""", ((sys.argv[4],)))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
