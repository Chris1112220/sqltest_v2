import sqlite3
import pandas as pd

from datetime import datetime, timedelta

conn = sqlite3.connect("new_table.db")
cursor = conn.cursor()

pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.expand_frame_repr', False)  # Avoid line wrapping
pd.set_option('display.max_colwidth', None) 



#Calculating 1 year ago for the query below
one_year_ago = datetime.now() - timedelta(days=365)
formatted_date = one_year_ago.strftime("%Y-%m-%d")
print(formatted_date)




#Created
cursor.execute("""
               CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY,
               name TEXT,
               email TEXT,
               created_at DATETIME
               );
               """)

#Inserting

cursor.execute("INSERT OR IGNORE INTO users (id, name, email, created_at ) VALUES('1', 'Chris', 'Christopher.roberts11220@gmail.com', '2024-01-25' )")
cursor.execute("INSERT OR IGNORE INTO users (id, name, email, created_at ) VALUES('2', 'Mike', 'Mike@gmail.com', '2023-01-25' )")
cursor.execute("INSERT OR IGNORE INTO users (id, name, email, created_at ) VALUES('3', 'Finn', 'Finn@gmail.com', '2021-11-20' )")
cursor.execute("INSERT OR IGNORE INTO users (id, name, email, created_at ) VALUES('4', 'Micky', 'Micky@gmail.com', '2021-03-15' )")
cursor.execute("INSERT OR IGNORE INTO users (id, name, email, created_at ) VALUES('5', 'Sasha', 'Sasha@gmail.com', '2024-01-23' )")


# Query to get employees in department 1
cursor.execute("""
    SELECT *
    FROM users
    WHERE created_at >= '2023-01-01'
    
""")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

panda_setup = pd.read_sql_query("""
    SELECT *
    FROM users
    
""", conn)

print(panda_setup)
df_filtered = pd.DataFrame(rows, columns=["id", "name", "email", "created_at"])

# Export the DataFrame to a CSV file
df_filtered.to_csv("filtered_users.csv", index=False)

print("Filtered results have been exported to 'filtered_users.csv'")

conn.close()    