
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        # adjacency list
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # TODO
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2
        """
        # TODO
        # check if they exist
        if v1 in self.vertices and v2 in self.vertices:
            # add the edge
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None
            # might want to raise an exception here instead

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue and enqueue starting vertex
        que = Queue()
        que.enqueue([starting_vertex])
        # create a set of traversed vertices
        visited = set()
        ancestor_path = [starting_vertex]
        # while queue is not empty
        while que.size() > 0:
            # dequeue/pop the first vertex
            path = que.dequeue()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!
                print(path[-1])
                if len(path) > len(ancestor_path):
                    ancestor_path = path
                elif len(path) == len(ancestor_path):
                    if path[-1] < ancestor_path[-1]:
                        ancestor_path = path
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    que.enqueue(new_path)
        if len(ancestor_path) == 1:
            return -1
        else:
            return ancestor_path[-1]


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


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


'''
UNDERSTAND
Inputs: Dataset(ancestors), ID(starting_node)
given the inputs find the earliest known ancestor
The one at the farthest distance from starting_node
If there are two nodes tied for earliest ancestor, return the smaller one
If the starting node has no parents, return -1
Clarifications:
    - The input will not be empty.
    - There are no cycles in the input.
    - There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
    - IDs will always be positive integers.
    - A parent may have any number of children.
After looking at the README it seems like a Depth first search would be the best way to go about this
inputs are pairs (creating an edge) so for (1,3) 1 would be the parent and 3 would be the child
PLAN 
initialize a graph
initialize a stack
create a path variable
build edges in reverse so we can go from child to parent instead of parent to child
keep track of longest path 
'''

#                      Dataset,      ID
# def earliest_ancestor(ancestors, starting_node):
#     # initialize the graph
#     graph = Graph()
#     # DFS so add a stack
#     stack = Stack()
#     #add the starting node to the stack
#     stack.push([starting_node])
#     # keep track of the longest path
#     longest_path = [starting_node]
#     # initialize earliest ancestor as -1 since that will be the default if the vertex has no ancestor
#     earliest_ancestor = -1
#     # add all the pairs as vertices
#     for pair in ancestors:
#         graph.add_vertex(pair[0])
#         graph.add_vertex(pair[1])

#         #add edges in reverse
#         #add child first then parent
#         graph.add_edge(pair[1], pair[0])
'''
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    '''
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


def ancestor_graph(ancestors):
    graph = Graph()

    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        # add checks to see if they're already in vertices and only add if they're not, so we don't overwrite
        # think about moving it to graph class
        # if parent not in graph.vertices:
        graph.add_vertex(parent)
        # if child not in graph.vertices:
        graph.add_vertex(child)

        graph.add_edge(child, parent)
    return graph


def earliest_ancestor(ancestors, starting_node):
    # Initialize a graph
    graph = Graph()

    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        # add checks to see if they're already in vertices and only add if they're not, so we don't overwrite
        # think about moving it to graph class
        # if parent not in graph.vertices:
        graph.add_vertex(parent)
        # if child not in graph.vertices:
        graph.add_vertex(child)

        graph.add_edge(child, parent)

    return graph.bft(starting_node)
