def validate_data(data):
    if not data:
        raise ValueError("Data is required")

def validate_item(item):
    if not item['valid']:
        raise ValueError(f"Item {item['name']} is not valid")

def process_and_validate_data(data):
    validate_data(data)
    for item in data:
        validate_item(item)
    return data
