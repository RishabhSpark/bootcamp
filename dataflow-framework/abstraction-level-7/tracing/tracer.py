from collections import deque
import threading

class Tracer:
    def __init__(self, max_traces=1000):
        self.lock = threading.Lock()
        self.traces = deque(maxlen=max_traces)

    def add_trace(self, tag, line):
        with self.lock:
            self.traces.append({'tag': tag, 'line': line})

    def get_traces(self):
        with self.lock:
            return list(self.traces)

tracing = Tracer()