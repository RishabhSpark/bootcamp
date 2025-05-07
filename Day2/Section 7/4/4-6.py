import time

metrics = {
    "requests_processed": 0,
    "errors_occurred": 0,
    "total_execution_time": 0
}

def process_data(data):
    start_time = time.time()
    # Simulate processing
    time.sleep(1)
    metrics["requests_processed"] += 1
    end_time = time.time()
    metrics["total_execution_time"] += (end_time - start_time)

print(metrics)
