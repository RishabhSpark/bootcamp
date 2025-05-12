from collections import defaultdict

class Metrics:
    def __init__(self):
        self.line_received = defaultdict(int)
        self.line_emitted = defaultdict(int)
        self.processing_time = defaultdict(float)
        self.errors = defaultdict(int)
    
    def increment_received(self, processor_name):
        self.line_received[processor_name] += 1

    def increment_emitted(self, processor_name):
        self.line_emitted[processor_name] += 1

    def add_processing_time(self, processor_name, time_taken):
        self.processing_time[processor_name] += time_taken

    def increment_errors(self, processor_name):
        self.errors[processor_name] += 1
    
    def get_metrics(self):
        return {
            "received": dict(self.line_received),
            "emitted": dict(self.line_emitted),
            "time": {key: round(value, 4) for key, value in self.processing_time.items()},
            "errors": dict(self.errors)
        }