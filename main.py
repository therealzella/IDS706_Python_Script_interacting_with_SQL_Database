import sqlite3
import os

def connect_to_db(db_name="test.db"):
    conn = sqlite3.connect(db_name)
    print(f"Connected to database: {db_name}")
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                         id INTEGER PRIMARY KEY,
                         name TEXT NOT NULL,
                         age INTEGER)''')
    conn.commit()
    print("Table 'users' created successfully.")

def insert_user(conn, name, age):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print(f"Inserted user: {name}, {age}")

def read_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def update_user(conn, user_id, new_name):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ? WHERE id = ?", (new_name, user_id))
    conn.commit()

def delete_user(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

if __name__ == "__main__":
    print(f"Current working directory: {os.getcwd()}")

    conn = connect_to_db("test.db")  # This will create 'test.db' on disk
    create_table(conn)

    insert_user(conn, "John Doe", 30)

    conn.close()
    print("Database connection closed.")


