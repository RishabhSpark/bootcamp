import psutil

def print_resource_usage():
    memory = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=1)
    print(f"Memory Usage: {memory.percent}%")
    print(f"CPU Usage: {cpu}%")

print_resource_usage()
