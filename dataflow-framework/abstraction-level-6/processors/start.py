class StartProcessor:
    def __init__(self):
        pass

    def process(self, line: str):
        print(f"Starting processing: {line}")
        return [("filters", line)]
