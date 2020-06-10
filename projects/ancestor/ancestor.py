# import sys
# sys.path.append("../graph")
# from util import Queue

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()  # set of edges from this vert

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)  # add v2 as a neighbor to v1
        else:
            raise IndexError("Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

'''
ancestors is a list of (parent, child) pairs
starting_node is an ID, an integer
'''

def earliest_ancestor(ancestors, starting_node):
    # create graph
    graph = Graph()

    for ancestor in ancestors:
        parent = ancestor[0]
        child = ancestor[1]

        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)

    # Create an empty queue and enqueue the starting vertex ID
    q = Queue()
    q.enqueue([starting_node])

    # Create a Set to store visited vertices
    visited = set()

    earliest_anc = -1

    max_len = 1

    # While the queue is not empty...
    while q.size() > 0:
        # pop the first path from the queue
        path = q.dequeue()
        # get the last node from the path
        node = path[-1]

        # If that vertex has not been visited...
        if node not in visited:
            # Visit it
            print('current:', node)

            # Mark it as visited...
            visited.add(node)

            # Then add all of its neighbors to the back of the queue
            for neighbor in graph.get_neighbors(node):
                print('neighbor', neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                max_len = len(new_path)
                q.enqueue(new_path)
            # if no neighbors
            if graph.get_neighbors(node) == set():
                print('path:', path)
                # if node < earliest_anc:
                earliest_anc = path[-1]
    print('max length:', max_len)
    return earliest_anc
