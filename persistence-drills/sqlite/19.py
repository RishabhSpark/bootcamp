import sqlite3

def setup_accounts_table(db_name="bank.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        account_id INTEGER PRIMARY KEY,
        balance REAL NOT NULL CHECK (balance >= 0)
    );
    """)
    
    # Insert some initial data
    cursor.execute("INSERT OR IGNORE INTO accounts (account_id, balance) VALUES (1, 1000.0);")
    cursor.execute("INSERT OR IGNORE INTO accounts (account_id, balance) VALUES (2, 500.0);")
    cursor.execute("INSERT OR IGNORE INTO accounts (account_id, balance) VALUES (3, 1000.0);")

    conn.commit()
    conn.close()

def transfer_funds(
    db_name: str, from_account: int, to_account: int, amount: float
) -> None:
    """
    Transfers funds from one account to another using a single transaction.

    Rolls back if any part of the transaction fails.
    """
    if amount <= 0:
        print("Transfer amount must be positive.")
        return

    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        conn.execute("BEGIN")  # Start transaction

        cursor.execute("SELECT balance FROM accounts WHERE account_id = ?;", (from_account,))
        from_result = cursor.fetchone()
        if not from_result:
            raise ValueError("Sender account does not exist.")

        if from_result[0] < amount:
            raise ValueError("Insufficient funds in sender's account.")

        # Debit sender
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?;", (amount, from_account))

        # Credit receiver
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?;", (amount, to_account))
        if cursor.rowcount == 0:
            raise ValueError("Receiver account does not exist.")

        conn.commit()
        print(f"Transferred ${amount:.2f} from account {from_account} to {to_account}.")

    except (sqlite3.Error, ValueError) as e:
        conn.rollback()
        print(f"Transaction failed and rolled back. Reason: {e}")

    finally:
        conn.close()
        
def show_balances(db_name="bank.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT account_id, balance FROM accounts;")
    rows = cursor.fetchall()
    conn.close()

    print("\nAccount Balances:")
    for acc_id, balance in rows:
        print(f"Account {acc_id}: ${balance:.2f}")
        
if __name__ == "__main__":
    setup_accounts_table()

    transfer_funds("bank.db", from_account=1, to_account=2, amount=150.0)
    transfer_funds("bank.db", from_account=1, to_account=3, amount=50.0)
    transfer_funds("bank.db", from_account=3, to_account=2, amount=250.0)
    
    show_balances()