from typing import Callable, Dict, List, Tuple

class DAG:
    def __init__(self):
        self.nodes: Dict[str, Callable] = {}
        self.edges: Dict[str, List[Tuple[str, str]]] = {}
        self.start_node = None

    def add_node(self, name: str, processor: Callable, start: bool = False):
        self.nodes[name] = processor
        self.edges[name] = []
        if start or self.start_node is None:
            self.start_node = name

    def add_edge(self, source: str, target: str, tag: str = None):
        self.edges[source].append((target, tag))

    def process(self, line: str):
        self._walk(self.start_node, line)

    def _walk(self, node: str, line: str, results: List[str] = None):
        if results is None:
            results = []
        
        if node not in self.nodes:
            return

        output = list(self.nodes[node](line))
        print(output)
            
        # Process the current line using the node's processor
        for tag, result in output:
            next_nodes = self.edges.get(node, [])
            if not next_nodes:
                results.append(result)
            # Check if there are edges from this node
            for target, edge_tag in self.edges.get(node, []):
                # Only proceed with the target node if the tag matches
                if edge_tag is None or edge_tag == tag:
                    self._walk(target, result)