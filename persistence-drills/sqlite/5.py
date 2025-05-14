import sqlite3

def update_price(product_id: int, new_price: float) -> None:
    """Updates the price of a product in the database.

    Args:
        product_id (int): The product ID to update.
        new_price (float): The updated price.
    """
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    
    update_sql = """
    UPDATE products
    SET price = ?
    WHERE id = ?;
    """
    
    cursor.execute(update_sql, (new_price, product_id))
    
    conn.commit()
    conn.close()
    

if __name__ == "__main__":
    update_price(1, 12.99)
