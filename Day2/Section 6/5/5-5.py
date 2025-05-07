def process_data(data):
    if data:
        valid_items = get_valid_items(data)
        print_valid_items(valid_items)

def get_valid_items(data):
    return [item for item in data if item['is_valid']]

def print_valid_items(items):
    for item in items:
        print(item['name'])
