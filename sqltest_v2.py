import sqlite3
import pandas as pd
import csv
from datetime import datetime, timedelta


def connect_to_db():
    """Connect to SQLite database or create it if it doesn't exist."""
    return sqlite3.connect("new_table1.db")


def create_table(conn):
    """Create the users table if it doesn't exist."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            created_at DATETIME
        );
    """)
    conn.commit()


def insert_data(conn):
    """Insert sample data into the users table."""
    conn.execute("INSERT OR IGNORE INTO users (id, name, email, created_at) VALUES (1, 'Chris', 'Christopher.roberts11220@gmail.com', '2024-01-25')")
    conn.execute("INSERT OR IGNORE INTO users (id, name, email, created_at) VALUES (2, 'Mike', 'Mike@gmail.com', '2023-01-25')")
    conn.execute("INSERT OR IGNORE INTO users (id, name, email, created_at) VALUES (3, 'Finn', 'Finn@gmail.com', '2021-11-20')")
    conn.execute("INSERT OR IGNORE INTO users (id, name, email, created_at) VALUES (4, 'Micky', 'Micky@gmail.com', '2021-03-15')")
    conn.execute("INSERT OR IGNORE INTO users (id, name, email, created_at) VALUES (5, 'Sasha', 'Sasha@gmail.com', '2024-01-23')")
    conn.commit()


def query_users(conn):
    """Query users created after 2023-01-01 and export results to CSV."""
    query = """
        SELECT *
        FROM users
        WHERE created_at >= '2023-01-01'
    """
    df = pd.read_sql_query(query, conn)
    print("Query Results:")
    print(df)
    
    # Export filtered results to a CSV file
    df.to_csv("filtered_users.csv", index=False)
    print("Filtered results have been exported to 'filtered_users.csv'")

def main():
    """Main function to run the script."""
    conn = connect_to_db()
    create_table(conn)
    insert_data(conn)
    query_users(conn)
    conn.close()
    print("Database connection closed.")


if __name__ == "__main__":
    main()
