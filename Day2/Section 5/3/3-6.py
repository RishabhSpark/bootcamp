from datetime import datetime

date1 = datetime(2024, 1, 1)
date2 = datetime(2025, 1, 1)

if date1 < date2:
    print(f"{date1} is earlier than {date2}")
elif date1 > date2:
    print(f"{date1} is later than {date2}")
else:
    print(f"{date1} and {date2} are the same.")
