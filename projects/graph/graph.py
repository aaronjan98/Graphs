"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
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

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
		# Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)

		# Create a Set to store visited vertices
        visited = set()

		# While the queue is not empty...
        while q.size() > 0:
			# Dequeue the first vertex 
            v = q.dequeue()

			# If that vertex has not been visited...
            if v not in visited:
				# Visit it
                print(v)

				# Mark it as visited...
                visited.add(v)

				# Then add all of its neighbors to the back of the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)
        
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and add the starting_vertex to the stack
        s = Stack()
        s.push(starting_vertex)

        # Create a Set to store visited vertices
        visited = set()

        # While the stack is not empty
        while s.size() > 0:
            # Pop last item from stack
            v = s.pop()

            # If that vertex has been visited...
            if v not in visited:
                print(v)
                # Mark it as visited
                visited.add(v)

                # Then push all of its neighbors onto the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # If that vertex has been visited...
        if starting_vertex not in visited:
            print(starting_vertex)
            # Mark it as visited
            visited.add(starting_vertex)

            # Then push all of its neighbors onto the stack
            for neighbor in self.get_neighbors(starting_vertex):
                # s.push(neighbor)
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # keep track of explored nodes
        explored = []
        # keep track of all the paths to be checked
        queue = [[starting_vertex]]
    
        # return path if starting_vertex is destination_vertex
        if starting_vertex == destination_vertex:
            return "That was easy! The starting vertex is the destination vertex."
    
        # keeps looping until all possible paths have been checked
        while queue:
            # pop the first path from the queue
            path = queue.pop(0)
            # get the last node from the path
            node = path[-1]
            if node not in explored:
                neighbours = self.vertices[node]
                # go through all neighbour nodes, construct a new path and
                # push it into the queue
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    # return path if neighbour is destination_vertex
                    if neighbour == destination_vertex:
                        return new_path
    
                # mark node as explored
                explored.append(node)
    
        # in case there's no path between the 2 nodes
        return "So sorry, but a connecting path doesn't exist :("

		# Create an empty queue and enqueue A PATH TO the starting vertex ID
		# Create a Set to store visited vertices
		# While the queue is not empty...
			# Dequeue the first PATH
			# Grab the last vertex from the PATHa
			# If that vertex has not been visited...
				# CHECK IF IT'S THE TARGET
				  # IF SO, RETURN PATH
				# Mark it as visited...
				# Then add A PATH TO its neighbors to the back of the queue
				  # COPY THE PATH
				  # APPEND THE NEIGHOR TO THE BACK
        pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
