import sqlite3

def insert_new_product(name: str, price: float) -> None:
    """
    Inserts a new product into the products table.
    
    name: The name of the product.
    price: The price of the product.
    """
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    insert_sql = """
    INSERT INTO products (name, price) VALUES (?, ?);
    """
    
    cursor.execute(insert_sql, (name, price))
    
    conn.commit()
    conn.close()
    

if __name__ == "__main__":
    insert_new_product("Book", 10.00)
    insert_new_product("Mouse", 19.99)
    insert_new_product("Headphones", 109.99)
