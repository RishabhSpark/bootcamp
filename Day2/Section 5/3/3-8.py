from datetime import datetime

# Round current time to the nearest hour
current_time = datetime.now()
rounded_time = current_time.replace(minute=0, second=0, microsecond=0)

# If minutes are greater than or equal to 30, round up
if current_time.minute >= 30:
    rounded_time = rounded_time.replace(hour=current_time.hour + 1)

print(f"Rounded time: {rounded_time}")
