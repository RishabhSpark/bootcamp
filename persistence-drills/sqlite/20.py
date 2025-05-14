import sqlite3
from datetime import datetime

def setup_inventory_schema(db_name="inventory.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create products table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL CHECK (quantity >= 0)
    );
    """)

    # Create inventory_log table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory_log (
        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER NOT NULL,
        change INTEGER NOT NULL,
        reason TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    );
    """)

    # Insert initial product
    cursor.execute("INSERT OR IGNORE INTO products (product_id, name, quantity) VALUES (1, 'Mouse', 20);")
    cursor.execute("INSERT OR IGNORE INTO products (product_id, name, quantity) VALUES (2, 'Coffee', 100);")
    conn.commit()
    conn.close()


def update_inventory(db_name: str, product_id: int, change: int, reason: str) -> None:
    """
    Updates product inventory and logs the change in a single transaction.
    Rolls back if either step fails.
    """
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        conn.execute("BEGIN")

        # Get current quantity
        cursor.execute("SELECT quantity FROM products WHERE product_id = ?;", (product_id,))
        result = cursor.fetchone()
        if not result:
            raise ValueError("Product not found.")

        current_qty = result[0]
        new_qty = current_qty + change

        if new_qty < 0:
            raise ValueError("Insufficient stock for this operation.")

        # Update inventory
        cursor.execute("UPDATE products SET quantity = ? WHERE product_id = ?;", (new_qty, product_id))

        cursor.execute("""
            INSERT INTO inventory_log (product_id, change, reason, timestamp)
            VALUES (?, ?, ?, ?);
        """, (product_id, change, reason, datetime.utcnow().isoformat()))

        conn.commit()
        print(f"Inventory updated. New quantity for product {product_id}: {new_qty}")

    except (sqlite3.Error, ValueError) as e:
        conn.rollback()
        print(f"Transaction failed and rolled back. Reason: {e}")

    finally:
        conn.close()


if __name__ == "__main__":
    setup_inventory_schema()

    # Successful update
    update_inventory("inventory.db", product_id=1, change=-10, reason="Customer order")

    # Fails due to negative stock
    update_inventory("inventory.db", product_id=1, change=-1000, reason="Huge order")