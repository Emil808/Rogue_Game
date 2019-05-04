
import random
from Source.Auxillary.undirected_graph import Graph
from Source.Auxillary.undirected_graph import Vertex
class room:
    def __init__(self):
        self.x = random.randint(10, 15)  # x dimension of the room
        self.y = random.randint(10, 15)  # y dimension of the room
        nodes = self.x * self.y # save total amount of nodes
        corners = [0, self.x, self.x * self.y - self.x, self.x * self.y - 1] # saves corners
        # make a node network to be used for path finding later
        self.map = Graph()  # undirected graph data type for the spaces in the room
        for i in range(nodes):  # initializes vertices on the room
            self.map.add_vertex(Vertex(i))

        # connects first and last row nodes
        a = 0
        while a < self.x - 1:
            self.map.add_edge(a, a + 1, 1)  # connects nodes within first row
            a += 1
        a = nodes - self.x
        while a < nodes - 1:
            self.map.add_edge(a, a + 1, 1)  # connects nodes within last row
            a += 1
        # todo: connect nodes inbetween

    # todo: return connection list for path finding functions in monster and player character
    # todo: return room edge check for movement, want to keep characters within bounds of room
    # todo: take in positions of characters and print them in their positions

    def print(self):
        print("")
        for j in range(self.y):
            for i in range(self.x):
                print('#', end='')
            print("")

