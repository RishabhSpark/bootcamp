import sqlite3

class Product:
    def __init__(self, db_name="store.db"):
        self.db_name = db_name
    
    def insert_new_product(self, name: str, price: float) -> None:
        """
        Inserts a new product into the products table.
        
        name: The name of the product.
        price: The price of the product.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            insert_sql = """
            INSERT INTO products (name, price) VALUES (?, ?);
            """
            
            cursor.execute(insert_sql, (name, price))
            
            conn.commit()
            conn.close()
            
            print(f"\nInserted new product: {name} with price: {price}")
        except sqlite3.Error as e:
            print(f"An error occurred while inserting the product: {e}")
        finally:
            if conn:
                conn.close()
        
    def print_records(self) -> None:
        """
        Prints all records from the products table.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            select_sql = """
            SELECT * FROM products;
            """
            
            cursor.execute(select_sql)
            
            # fetch all rows from the query
            rows = cursor.fetchall()
            
            conn.close()
            
            print("All products in the database:")
            for row in rows:
                product_id, name, price = row
                print(f"ID: {product_id}, Name: {name}, Price: {price}")
            
            print("\nEnd of product list.")
        except sqlite3.Error as e:
            print(f"An error occurred while fetching records: {e}")
        finally:
            if conn:
                conn.close()
    
    
    def update_price(self, product_id: int, new_price: float) -> None:
        """Updates the price of a product in the database.

        Args:
            product_id (int): The product ID to update.
            new_price (float): The updated price.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            update_sql = """
            UPDATE products
            SET price = ?
            WHERE id = ?;
            """
            
            cursor.execute(update_sql, (new_price, product_id))
            
            conn.commit()
            conn.close()
            if cursor.rowcount == 0:
                print(f"\nNo product found with ID: {product_id}")
            else:
                print(f"\nUpdated product ID {product_id} to new price: {new_price}")
        
        except sqlite3.Error as e:
            print(f"An error occurred while updating the product price: {e}")
        
        finally:
            if conn:
                conn.close()
        
    def delete_product(self, product_id: int) -> None:
        """
        Deletes a product from the products table by its ID.
        
        product_id: The ID of the product to delete.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            delete_sql = """
            DELETE FROM products WHERE id = ?;
            """
            
            cursor.execute(delete_sql, (product_id,))
            
            conn.commit()
            conn.close()
            
            print(f"\nDeleted product with ID: {product_id}")
        
        except sqlite3.Error as e:
            print(f"An error occurred while deleting the product: {e}")
        
        finally:
            if conn:
                conn.close()
        
if __name__ == "__main__":
    product_db = Product('store.db')
    
    product_db.insert_new_product("Keyboard_2", 29.99)
    product_db.insert_new_product("Keyboard_3", 19.99)
    
    product_db.print_records()
    
    product_db.update_price(4, 59.99)
    
    product_db.delete_product(6)

    # Print all products again to see changes
    product_db.print_records()