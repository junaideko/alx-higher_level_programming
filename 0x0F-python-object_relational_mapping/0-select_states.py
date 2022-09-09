#!/usr/bin/python3
"""List all states from a given db sorted in ascending orderby id
Username, password, and database names are given as user args
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    rows = cur.fetchall()
    [print(row) for row in rows]

cur.close()
db.close()
