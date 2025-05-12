import importlib

class StateBasedRouter:
    def __init__(self, config):
        self.config = config
        self.processors = {}
        self._load_processors()

    def _load_processors(self):
        for node in self.config['nodes']:
            module_class_path = node['type']
            try:
                module_path, class_name = module_class_path.rsplit('.', 1)
                module = importlib.import_module(module_path)
                cls = getattr(module, class_name)
                self.processors[node['tag']] = cls()
            except (ImportError, AttributeError) as e:
                print(f"Error importing {module_class_path}: {e}")

    def run(self, start_tag, lines):
        queue = [(start_tag, line) for line in lines]
        while queue:
            tag, line = queue.pop(0)
            processor = self.processors.get(tag)
            if not processor:
                print(f"No processor found for tag '{tag}'")
                continue
            try:
                output = processor.process(line)
                for next_tag, new_line in output:
                    queue.append((next_tag, new_line))
            except Exception as e:
                print(f"Error processing line '{line}' at tag '{tag}': {e}")
