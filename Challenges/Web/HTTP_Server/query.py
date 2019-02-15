import sys
import sqlite3
from sqlite3 import Error

def main():
  try:
    db = "database.db"
    conn = sqlite3.connect(db)
    conn.text_factory = str
    
    cur = conn.cursor()
    
    user = raw_input("Input username: ")
    pw = raw_input("Input password: ")
    q = "SELECT * FROM users WHERE name='"+user+"' AND password='"+pw+"'"
    cur.execute(q)
    #print "Executing query: %s" % q
    rows = cur.fetchall()
    print "Found %s results" % len(rows)
    #print "Showing results..."
    for row in rows:
        print(row)
      
  except Error as e:
    print(e)

if __name__ == '__main__':
    main()
