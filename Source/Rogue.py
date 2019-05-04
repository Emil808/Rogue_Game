
import random
from Source.Auxillary.undirected_graph import Graph
from Source.Auxillary.undirected_graph import Vertex

class room:
    def __init__(self):
        self.x = random.randint(10, 20)  # x dimension of the room
        self.y = random.randint(5, 10)  # y dimension of the room
        self.map = Graph()  # undirected graph data type for the spaces in the room
        nodes = self.x * self.y # save total amount of nodes
        for i in range(nodes):  # initializes vertices on the room
            self.map.add_vertex(Vertex(i))

        # connects first and last row nodes
        # make a node network to be used for path finding later
        a = nodes - self.x
        while a < nodes - 1:
            self.map.add_edge(a, a + 1, 1)  # connects nodes within row y
            a += 1
        a = 0
        while a < self.x:
            if a < self.x - 1:
                self.map.add_edge(a, a + 1, 1)  # connects nodes within row 0
            self.map.add_edge(a, a + self.x, 1) # connects this row to the nodes of the next row
            a += 1
        for j in range(1, self.y - 1): # starting from row 1
            row = j * self.x
            for a in range(0, self.x): # connects the nodes within the row, and nodes with the next row
                if a < self.x - 1:
                    self.map.add_edge(a + row, a + row + 1, 1)
                self.map.add_edge(a + row, a + row + self.x, 1)

    #  current row:  # - # - # - #
    #                |   |   |   |
    #  next row      #   #   #   #

    def get_room_nodes(self):    # return connection list for path finding functions in monster and player character
        return self.map

    # todo: take in positions of characters and print them in their positions
    def print(self):
        print("")
        for j in range(self.y):
            for i in range(self.x):
                print('#', end='')
            print("")

