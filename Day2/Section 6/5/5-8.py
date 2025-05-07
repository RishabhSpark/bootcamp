# Only process valid items to avoid errors
for item in items:
    if item['valid']:
        process(item)
