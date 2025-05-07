from datetime import datetime, timedelta

current_date = datetime.now()
new_date = current_date + timedelta(days=7)
print(f"New date (7 days later): {new_date}")
