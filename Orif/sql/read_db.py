import sqlite3

sqlite_file = "test_db.sqlite"

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating a new SQLite table with 1 column
result = c.execute('SELECT * FROM {tn}'
                   .format(tn="MyNumbers"))

rows = c.fetchall()
#number_rows = len(rows)
for row in rows:
    print(row)

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()