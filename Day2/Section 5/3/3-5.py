import calendar
from datetime import datetime

today = datetime.now()
weekday_name = calendar.day_name[today.weekday()]
print(f"Today is: {weekday_name}")
