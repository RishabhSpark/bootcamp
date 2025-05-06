class DBConnection:
    def __enter__(self):
        print("Opening DB connection...")
        # Simulate DB connection
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing DB connection...")
        # Simulate cleanup
        if exc_type:
            print(f"Exception: {exc_val}")
        return True  # Suppress exception

with DBConnection() as db:
    print("Using DB connection...")
    # Simulate an error
    raise ValueError("Simulated error!")
