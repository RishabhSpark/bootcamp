import time

def retry(max_retries=3, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {retries + 1} failed: {e}")
                    retries += 1
                    if retries < max_retries:
                        print(f"Retrying in {delay} seconds...")
                        time.sleep(delay)
                    else:
                        print("Max retries reached. Function failed.")
                        raise e
        return wrapper
    return decorator

@retry(max_retries=3, delay=1)
def risky_operation():
    if time.time() % 2 < 1:
        raise ValueError("Simulated failure!")
    return "Success!"

# Test
print(risky_operation())
