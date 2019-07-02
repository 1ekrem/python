import sqlite3

sqlite_file = "test_db.sqlite"

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating a new SQLite table with 1 column
c.execute("CREATE TABLE {tn} ({nf} {ft})"
          .format(tn="MyNumbers", nf="Value", ft='INTEGER'))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()

