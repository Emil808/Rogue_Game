
import random
import keyboard
from Source.Auxillary.undirected_graph import Graph
from Source.Auxillary.undirected_graph import Vertex

class room:
    def __init__(self):
        self.x = random.randint(10, 11)  # x dimension of the room
        self.y = random.randint(5, 7)  # y dimension of the room
        self.map = Graph()  # undirected graph data type for the spaces in the room
        nodes = self.x * self.y  # save total amount of nodes
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

    # todo: edge case if monster is generated in same position as hero
    def print(self, Hero, Monster):
        hero_position = Hero.get_position()
        monster_position = Monster.get_position()
        print("")
        for a in range(self.x+2):
            print('#', end='')
        print("")
        for j in range(self.y):
            print('#', end='')
            for i in range(self.x):
                if [i, j] == hero_position:
                    print('H', end='')
                elif [i, j] == monster_position:
                    print('M', end='')
                else:
                    print(' ', end='')
            print('#', end='')
            print("")
        for a in range(self.x+2):
            print('#', end='')
        print("")


class character:

    def __init__(self, room):

        # generate random position within room limits
        self.position = [random.randint(0, room.x - 1), random.randint(0, room.y - 1)]   # [x,y]
        self.x = room.x
        self.y = room.y

    def get_position(self):  # returns position
        return self.position





class Hero(character):
    # child of character class
    def __init__(self, room):
        character.__init__(self, room)
        self.last_position = self.position

    def move(self):
        # movement for hero character, need to call room.print to see changes
        while 1:
            if keyboard.is_pressed('w'):    # move up
                while keyboard.is_pressed('w'):
                    n = 1
                if self.position[1] == 0:
                    break
                else:
                    self.last_position = self.position
                    self.position[1] -= 1
                    break
            if keyboard.is_pressed('s'):    # move down
                while keyboard.is_pressed('s'):
                    n = 1
                if self.position[1] == self.y - 1:
                    break
                else:
                    self.last_position = self.position
                    self.position[1] += 1
                    break
            if keyboard.is_pressed('a'):    # move left
                while keyboard.is_pressed('a'):
                    n = 1
                if self.position[0] == 0:
                    break
                else:
                    self.last_position = self.position
                    self.position[0] -= 1
                    break
            if keyboard.is_pressed('d'):    # move right
                while keyboard.is_pressed('d'):
                    n = 1
                if self.position[0] == self.x - 1:
                    break
                else:
                    self.last_position = self.position
                    self.position[0] += 1
                    break
    # todo: die,

    def die(self, monster):
        if self.get_position() == monster.get_position():
            return True
        else:
            return False

    def get_last_position(self):    # return last position, used for monster update path
        return self.last_position



class Monster(character):
    # make child of character class
    def __init__(self, room):
        character.__init__(self, room)
        self.movement_queue = []

    # todo: move, take command from movement queue made from path finding
    # todo: update path, gets last position of hero, from tha position, updates movement queue

    def pursue_hero(self):
        return 1;
#todo: pursue Hero, initial path finding, use Dijstras