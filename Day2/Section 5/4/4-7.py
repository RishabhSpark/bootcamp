import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # Return ISO format string for datetime objects
        return super().default(obj)

now = datetime.now()
json_string = json.dumps({"time": now}, cls=DateTimeEncoder)
print(f"Serialized datetime: {json_string}")