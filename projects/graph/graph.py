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
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        try:
            if v2 not in self.vertices:
                raise Exception

            self.vertices[v1].add(v2)
        except KeyError:
            print("There is no vertex {}".format(v1))
        except Exception:
            print("You can't add an non existant vertex {} to {}".format(v2, v1))

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        queue.enqueue(starting_vertex)

        visited = set()

        while queue.size() > 0:
            temp_vertex = queue.dequeue()

            if temp_vertex not in visited:
                visited.add(temp_vertex)
                print(temp_vertex)
                for neighbor in self.get_neighbors(temp_vertex):
                    queue.enqueue(neighbor)
                    
            

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)

        visited = set()

        while stack.size() > 0:
            temp_vertex = stack.pop()

            if temp_vertex not in visited:
                visited.add(temp_vertex)
                print(temp_vertex)
                for neighbor in self.get_neighbors(temp_vertex):
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #Check if node has been visited
        #If not
            #Mark it as visited
            #Call dft_recursive on each neighbor
            #Figure out to carry out visited, nested function, default arg
        def dft_helper(vertex, visited):
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
            
                for neighbor in self.get_neighbors(vertex):
                    dft_helper(neighbor, visited)
        
        visited = set()

        dft_helper(starting_vertex, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #Create a queue
        #Enqueue a path to the starting vertex
        #Create a set to store visited vertices
        #While the queue is not empty
            #Dequeue the first path
            #Grab the vertex from the end of the path
            #Check if it has been visited
            #Check if its the target if so return the path
            #if it hasnt been visited
                #mark it as visited
                #enqueue a path to all its neighbors
                    #make a copy of the path
                    #enqueue the copy

        queue = Queue()
        visited = set()
        path = [starting_vertex]
        queue.enqueue(path)

        while queue.size() > 0:
            path = queue.dequeue()
            vertex = path[-1]

            if vertex == destination_vertex:
                return path

            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    new_path = path[:]
                    new_path.append(neighbor)
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = set()
        path = [starting_vertex]
        stack.push(path)

        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]

            if vertex == destination_vertex:
                return path

            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    new_path = path[:]
                    new_path.append(neighbor)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        def dft_helper(vertex, visited):
                      
            if vertex == destination_vertex:
                return [vertex]

            if vertex not in visited:
                    visited.add(vertex)

                    if self.get_neighbors(vertex) is None:
                        return None

                    for neighbor in self.get_neighbors(vertex):
                        path = dft_helper(neighbor, visited)
                        if path:
                            return [vertex, *path]
                
        visited = set()
        path = dft_helper(starting_vertex, visited)

        return path


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
