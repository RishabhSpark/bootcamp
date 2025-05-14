import sqlite3

def setup_tables(db_name="store.db"):
    """Initializes the orders and order_details tables."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            status TEXT NOT NULL
        );
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_details (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY(order_id) REFERENCES orders(id)
        );
    """)
    
    conn.commit()
    conn.close()

def seed_data(db_name="store.db"):
    """Inserts one sample order and details for testing."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO orders (customer_name, status) VALUES (?, ?);", ("Rishabh", "Pending"))
    order_id = cursor.lastrowid
    
    order_details = [
        (order_id, "Laptop", 1),
        (order_id, "Mouse", 2),
    ]
    cursor.executemany("INSERT INTO order_details (order_id, product_name, quantity) VALUES (?, ?, ?);", order_details)
    
    conn.commit()
    conn.close()

def update_order_and_details(order_id: int, new_status: str, updates: list, db_name="store.db"):
    """
    Updates order status and details in a single transaction.

    Args:
        order_id (int): ID of the order to update.
        new_status (str): New status to update in orders table.
        updates (list of tuples): Each tuple (detail_id, new_quantity) for order_details.
    """
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        conn.execute("BEGIN")

        # Update order status
        cursor.execute("UPDATE orders SET status = ? WHERE id = ?;", (new_status, order_id))

        # Update order_details quantities
        for detail_id, new_qty in updates:
            cursor.execute("UPDATE order_details SET quantity = ? WHERE id = ?;", (new_qty, detail_id))

        conn.commit()
        print("\nTransaction successful: Order and details updated.")

    except sqlite3.Error as e:
        conn.rollback()
        print(f"\nTransaction failed and rolled back: {e}")

    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    setup_tables()
    seed_data()

    update_order_and_details(
        order_id=1,
        new_status="Shipped",
        updates=[(1, 2), (2, 3)]
    )