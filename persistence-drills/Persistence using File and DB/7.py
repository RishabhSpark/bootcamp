import json

class Node:
    def __init__(self, id, label, data=None):
        self.id = id
        self.label = label
        self.data = data or {}

    def to_dict(self):
        return {
            "id": self.id,
            "label": self.label,
            "data": self.data
        }

class Edge:
    def __init__(self, source, target, weight=1):
        self.source = source
        self.target = target
        self.weight = weight


    def to_dict(self):
        return {
            "source": self.source,
            "target": self.target,
            "weight": self.weight
        }

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node):
        self.nodes[node.id] = node

    def add_edge(self, edge):
        self.edges.append(edge)

    def to_dict(self):
        return {
            "nodes": [node.to_dict() for node in self.nodes.values()],
            "edges": [edge.to_dict() for edge in self.edges]
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)


g = Graph()

g.add_node(Node("A", "Start", {"x": 0, "y": 0}))
g.add_node(Node("B", "Middle", {"x": 1, "y": 1}))
g.add_node(Node("C", "End", {"x": 2, "y": 2}))

g.add_edge(Edge("A", "B", weight=5))
g.add_edge(Edge("B", "C", weight=3))

graph_json = g.to_json()

print("Serialized Graph:")
print(graph_json)