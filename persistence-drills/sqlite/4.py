import sqlite3

def print_records() -> None:
    """
    Prints all records from the products table.
    """
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    
    select_sql = """
    SELECT * FROM products;
    """
    
    cursor.execute(select_sql)
    
    # fetch all rows from the query
    rows = cursor.fetchall()
    
    conn.close()
    
    for row in rows:
        product_id, name, price = row
        print(f"ID: {product_id}, Name: {name}, Price: {price}")
        

if __name__ == "__main__":
    print_records()