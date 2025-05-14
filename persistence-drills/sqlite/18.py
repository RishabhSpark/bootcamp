import sqlite3
import csv
from typing import List, Tuple

class Product:
    def __init__(self, db_name="store.db"):
        self.db_name = db_name
        
    def insert_new_product(self, name: str, price: float) -> None:
        """
        Inserts a new product into the products table.
        
        name: The name of the product.
        price: The price of the product.
        """
        if not isinstance(name, str) or not name.strip():
            print("\nProduct name must be a non-emptystring.")
            return
        
        if not isinstance(price, (int, float)) or price <= 0:
            print("\nProduct price must be a positive number.")
            return
            
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            conn.execute("BEGIN")  # Start transaction

            insert_sql = """
            INSERT INTO products (name, price) VALUES (?, ?);
            """
            
            cursor.execute(insert_sql, (name, price))
            
            conn.commit()
            conn.close()
            
            print(f"\nInserted new product: {name} with price: {price}")
            
        except sqlite3.Error as e:
            conn.rollback()
            print(f"\nAn error occurred while inserting the product: {e}")
        
        finally:
            if conn:
                conn.close()
    
    def insert_multiple_products(self, products: List[tuple[str, float]]) -> None:
        """
        Inserts multiple products into the products table in one transaction.

        Args:
            products (list of tuples): A list where each tuple contains (name, price) of a product.
        """
        if not products or not all(isinstance(p, tuple) and len(p) == 2 for p in products):
            print("\nInvalid input: provide a list of (name, price) tuples.")
            return

        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            conn.execute("BEGIN")
            
            insert_sql = "INSERT INTO products (name, price) VALUES (?, ?);"
            
            for name, price in products:
                if not isinstance(name, str) or not name.strip():
                    raise ValueError(f"Invalid product name: {name}")
                if not isinstance(price, (int, float)) or price <= 0:
                    raise ValueError(f"Invalid price for product '{name}': {price}")
                cursor.execute(insert_sql, (name.strip(), price))

            
            conn.commit()
            conn.close()
            
            print(f"\nInserted {len(products)} new products.")
        
        except sqlite3.Error as e:
            conn.rollback()
            print(f"\nAn error occurred while inserting multiple products: {e}")
        
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
            print(f"\nAn error occurred while fetching records: {e}")
        finally:
            if conn:
                conn.close()
    
    def update_price(self, product_id: int, new_price: float) -> None:
        """Updates the price of a product in the database.

        Args:
            product_id (int): The product ID to update.
            new_price (float): The updated price.
        """
        
        if not isinstance(new_price, (int, float)) or new_price <= 0:
            print("\nProduct price must be a positive number.")
            return
        
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            conn.execute("BEGIN")  # Start transaction
            
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
            conn.rollback()
            print(f"\nAn error occurred while updating the product price: {e}")
        
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
            conn.execute("BEGIN")  # Start transaction

            delete_sql = """
            DELETE FROM products WHERE id = ?;
            """
            
            cursor.execute(delete_sql, (product_id,))
            
            conn.commit()
            conn.close()
            
            print(f"\nDeleted product with ID: {product_id}")
        
        except sqlite3.Error as e:
            conn.rollback()
            print(f"\nAn error occurred while deleting the product: {e}")
        
        finally:
            if conn:
                conn.close()
    
    def search_product_by_name(self, name: str) -> None:
        """
        Searches for a product by its name in the products table.
        
        name: The name of the product to search for.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            search_sql = """
            SELECT * FROM products WHERE name LIKE ?;
            """
            
            cursor.execute(search_sql, (f"%{name}%",))
            
            results = cursor.fetchall()
            
            conn.close()
            
            print(f"Search results for '{name}':")
            for row in results:
                product_id, name, price = row
                print(f"ID: {product_id}, Name: {name}, Price: {price}")
            
            print("\nEnd of search results.")
            
        except sqlite3.Error as e:
            print(f"\nAn error occurred while searching for the product: {e}")
            
        finally:
            if conn:
                conn.close()
    
    def fetch_products_with_cateogry(self) -> None:
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            join_sql = """
            SELECT p.id, p.name, p.price, c.category_name
            FROM products p
            LEFT JOIN categories c ON p.name = c.product_name;
            """
            
            cursor.execute(join_sql)
            
            results = cursor.fetchall()
            conn.close()
            
            print(f"\nProducts with Categories:")
            for row in results:
                product_id, name, price, category_name = row
                print(f"ID: {product_id}, Name: {name}, Price: {price}, Category: {category_name or 'Uncategorized'}")            
        
        except sqlite3.Error as e:
            print(f"An error occurred while fetching products with categories: {e}")
        
        finally:
            if conn:
                conn.close()
                
    def calculate_total_values(self) -> None:
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            total_sql = """
            SELECT SUM(price) FROM products;
            """
            
            cursor.execute(total_sql)
            
            result = cursor.fetchone()[0]
            conn.close()
            
            if result is not None:
                print(f"\nTotal value of all products in stock: {result:.2f}")
            else:
                print("\nNo products found in the database.")
        
        except sqlite3.Error as e:
            print(f"An error occurred while calculating total values: {e}")
        
        finally:
            if conn:
                conn.close()
                
    def export_to_csv(self, filename: str) -> None:
        """
        Exports the products table to a CSV file.
        
        filename: The name of the CSV file to export to.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            select_sql = "SELECT * FROM products;"
            
            cursor.execute(select_sql)
            rows = cursor.fetchall()

            column_names = [description[0] for description in cursor.description]

            with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(column_names)
                writer.writerows(rows)

            print(f"\nExported {len(rows)} products to {filename}")
        
        except sqlite3.Error as e:
            print(f"\nAn error occurred while exporting to CSV: {e}")
        
        finally:
            if conn:
                conn.close()

        
if __name__ == "__main__":
    product = Product()
    
    product_list = [
        ("Notebook2", 4.99),
        ("Pen2", 1.49),
        ("Backpack", 39.99)
    ]
    
    product.insert_multiple_products(product_list)
    product.print_records()