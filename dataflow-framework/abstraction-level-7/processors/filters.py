class LineProcessor:
    def __init__(self):
        pass

    def contains_error(self, line):
        """Check if the line contains the word 'error'."""
        return "error" in line.lower()

    def process(self, line):
        """Process a single line and filter based on error presence."""
        if self.contains_error(line):
            print(f"Filtered line: {line}")
            return [("formatters", line)]
        else:
            print(f"Ignored line: {line}")
            return []