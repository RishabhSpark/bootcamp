import sqlite3

def delete_product(product_id: int) -> None:
    """
    Deletes a product from the products table by its ID.
    
    product_id: The ID of the product to delete.
    """
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    delete_sql = """
    DELETE FROM products WHERE id = ?;
    """
    
    cursor.execute(delete_sql, (product_id,))
    
    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    delete_product(2)