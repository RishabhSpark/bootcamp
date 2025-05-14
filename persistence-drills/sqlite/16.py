import sqlite3

def insert_customers(customers, db_name="store.db"):
    """
    Inserts multiple customer records into the customers table using a transaction.
    
    Args:
        customers (list of tuples): Each tuple should be (name, email).
        db_name (str): SQLite database name.
    """
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            );
        """)

        conn.execute("BEGIN")  # Start transaction

        insert_sql = "INSERT INTO customers (name, email) VALUES (?, ?);"
        cursor.executemany(insert_sql, customers)

        conn.commit()
        print(f"\nInserted {len(customers)} customers successfully.")

    except sqlite3.Error as e:
        conn.rollback()
        print(f"\nTransaction failed. Rolled back. Error: {e}")

    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    customer_data = [
        ("Alice Johnson", "alice@example.com"),
        ("Bob Smith", "bob@example.com"),
        ("Charlie Brown", "charlie@example.com")
    ]

    insert_customers(customer_data)