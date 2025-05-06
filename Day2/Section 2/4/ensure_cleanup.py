class CleanupManager:
    def __enter__(self):
        print("Entering the context...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context...")
        if exc_type:
            print(f"Exception: {exc_val}")
        return True  # Suppress exception

with CleanupManager():
    print("Doing some work...")
    # Simulate an error
    raise RuntimeError("Something went wrong!")