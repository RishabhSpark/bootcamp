import threading

# Shared variable
counter = 0

# Lock to protect shared resource
lock = threading.Lock()

# Function to increment the counter
def increment():
    global counter
    with lock:
        counter += 1
        print(f"Counter value: {counter}")

# Start multiple threads
threads = [threading.Thread(target=increment) for _ in range(5)]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
