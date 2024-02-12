import sqlite3

# Create a connection to the database
conn = sqlite3.connect('bank.db')

# Create a cursor
cur = conn.cursor()



some_dudes = [
    ('John', 'Smith'),
    ('Jane', 'Johnson'),
    ('Sam', 'Williams'),
    ('Sara', 'Brown'),
]


# Create a "people" table#
# cur.execute(f'''CREATE TABLE IF NOT EXISTS people
#                 (first_name TEXT, last_name TEXT, age INTEGER)''')
cur


# End of the program
cur.close()
conn.close()
