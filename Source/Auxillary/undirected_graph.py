# Emil's undirected graph
class Vertex:
    def __init__(self, vertex):
        self.name = vertex      # vertex id
        self.neighbors = {}     # neighbors dictionary. Key is name of neighbor vertex, value is weight

    def add_neighbor(self, neighbor, weight = 0):       # adds one vertex's name to neighbor
        self.neighbors[neighbor] = weight          # appends neighbor to vertex neighbor list

    def add_neighbors(self, neighbors):     # adds from array of vertex object
        for x in neighbors:                 # assumes neighbors is another vertex object's neighbors array
            return 1

    def get_connections(self):  # returns neighbors of self vertexx
        return self.neighbors

    def get_id(self):           # return name of self vertex
        return self.name

    def get_weight(self, neighbor):
        return self.neighbors.get(neighbor)  # return value(weight) of key(neighbor)

    def __repr__(self):
        return str(self.name) + str(self.neighbors)   # returns neighbors array as a string


class Graph:
    def __init__(self):
        self.vertices = {}      # dictionary of vertices
        self.vertice_amount = 0

    def add_vertex(self, vertex):
        self.vertices[vertex.name] = vertex   # adds vertex to dictionary, key is name, value is vertex object
        self.vertice_amount += 1
        return 1

    def get_vertex(self, n):            # n is vertex name
        return self.vertices.get(n)    # returns vertex object in key

    def get_vertices(self):
        return self.vertices.keys()

    def add_edge(self, frm, to, weight = 0):
        self.vertices[frm].add_neighbor(to, weight)     # gets frm vertex, add neighbor to vertex object
        self.vertices[to].add_neighbor(frm, weight)     # gets to vertex, add neighber to vertec object

    def remove_edge(self, frm, to):
        del self.vertices[frm].neighbors[to]
        del self.vertices[to].neighbors[frm]

    def add_edges(self, edges):
        # todo: waht should edges object be?
        return 1

    #def adjacencyList(self):    # to represent the graph as adjacent list
     #   adjacencylist = []
      #  for x in self.vertices:
       #     adjacencylist.append(x)
        #    for y in self.vertices[x].neighbors:
         #       adjacencylist[x]
        # return adjacencylist

def graph(g):
    """ Function to print a graph as adjacency list and adjacency matrix. """
    return str(g.adjacencyList()) + '\n'