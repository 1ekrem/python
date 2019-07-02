import sqlite3

sqlite_file = "test_db.sqlite"

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
#Open connections
c = conn.cursor()

# Creating a new SQLite table with 1 column
c.execute('INSERT INTO {tn}({nf}) VALUES({vl})'
          .format(tn="MyNumbers", nf="Value", vl=1.2))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()