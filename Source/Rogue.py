
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
        for i in range(nodes):  # initipalizes vertices on the room
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
        # generates exit node
        self.exit_gen = [[random.randint(0, self.x-2), 0], [random.randint(0, self.x-2), self.y-1],
                    [0, random.randint(0, self.y-2)], [self.x-1, random.randint(0, self.y-2)]]
        self.exit = random.randint(0,3)  # chooses random exit node
        self.exit_node = self.exit_gen[self.exit]
    #  current row:  # - # - # - #
    #                |   |   |   |
    #  next row      #   #   #   #

    def get_room_nodes(self):    # return connection list for path finding functions in monster and player character
        return self.map

    def print(self, Hero, Monster):
        hero_position = Hero.get_position()
        monster_position = Monster.get_position()
        print("")
        for a in range(self.x+2):
            if self.exit is 0:
                if a is self.exit_node[0] + 1:
                    if Hero.at_exit is True:
                        print('H', end='')
                    else:
                        print(' ', end='')
                else:
                    print('#', end='')
            else:
                print('#', end='')
        print("")
        for j in range(self.y):
            if self.exit is 2:
                if j is self.exit_node[1]:
                    if Hero.at_exit is True:
                        print('H', end='')
                    else:
                        print(' ', end='')
                else:
                    print('#', end='')
            else:
                print('#', end='')

            for i in range(self.x):
                if [i, j] == monster_position:
                    print('M', end='')
                elif [i, j] == hero_position:
                    if Hero.at_exit is True:
                        print(' ', end='')
                    else:
                        print('H', end='')
                else:
                    print(' ', end='')

            if self.exit is 3:
                if j is self.exit_node[1]:
                    print(' ', end='')
                else:
                    print('#', end='')
            else:
                print('#', end='')
            print("")
        for a in range(self.x+2):
            if self.exit is 1:
                if a is self.exit_node[0] + 1:
                    if Hero.at_exit is True:
                        print('H', end='')
                    else:
                        print(' ', end='')
                else:
                    print('#', end='')
            else:
                print('#', end='')
        print("")

class character:

    def __init__(self, room):

        # generate random position within room limits
        self.position = [random.randint(0, room.x - 1), random.randint(0, room.y - 1)]   # [x,y]
        self.node = room.x * self.position[1] + self.position[0]
        self.x = room.x
        self.y = room.y

    def get_position(self):     # returns position
        return self.position


class Hero(character):
    # child of character class
    def __init__(self, room):
        character.__init__(self, room)
        self.last_position = self.position
        self.exit = room.exit
        self.exit_node = room.exit_node
        self.at_exit = False
    def move(self):
        # movement for hero character, need to call room.print to see changes
        while 1:
            if keyboard.is_pressed('w'):    # move up
                while keyboard.is_pressed('w'):
                    n = 1
                if self.position[1] == 0:
                    if self.exit == 0 and self.position == self.exit_node:
                        self.at_exit = True
                    break
                else:
                    self.last_position = self.position
                    self.position[1] -= 1
                    break
            if keyboard.is_pressed('s'):    # move down
                while keyboard.is_pressed('s'):
                    n = 1
                if self.position[1] == self.y - 1:
                    if self.exit == 1 and self.position == self.exit_node:
                        self.at_exit = True
                    break
                else:
                    self.last_position = self.position
                    self.position[1] += 1
                    break
            if keyboard.is_pressed('a'):    # move left
                while keyboard.is_pressed('a'):
                    n = 1
                if self.position[0] == 0:
                    if self.exit == 2 and self.position == self.exit_node:
                        self.at_exit = True
                    break
                else:
                    self.last_position = self.position
                    self.position[0] -= 1
                    break
            if keyboard.is_pressed('d'):    # move right
                while keyboard.is_pressed('d'):
                    n = 1
                if self.position[0] == self.x - 1:
                    if self.exit == 3 and self.position == self.exit_node:
                        self.at_exit = True
                    break
                else:
                    self.last_position = self.position
                    self.position[0] += 1
                    break
        self.node = self.x * self.position[1] + self.position[0]

    def die(self, monster): # die
        if self.get_position() == monster.get_position():  # if monster and hero on same position, hero dies
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
    def pursue_hero(self, hero, room_nodes):
        # with hero_position,
        # use Dijkstra,
        monster_node = self.node
        hero_node = hero.node
        queue = []
        touched = []
        distance = []
        edge_from = []

        for i in range(room_nodes.vertice_amount):  # initialize needed data
            touched.append(False)
            distance.append('I')
            edge_from.append(None)

        queue.append(monster_node)  # pushes monster's node onto queue
        distance[monster_node] = 0  # origin node distance is 0
        edge_from[monster_node] = monster_node
        # makes minimum spanning tree
        while queue:  # loop while there are still things in the queue
            current = queue.pop(0)
            touched[current] = True  # update current to be touched

            for i in room_nodes.vertices[current].neighbors:  # for nodes connected to current
                if touched[i] is False:  # if nodes were not touched before
                    if i not in queue:
                        queue.append(i)  # store in queue to be looked at later
                    new_distance = distance[current] + 1
                    if distance[i] is 'I' or distance[i] >= new_distance:
                        # if distance to I is infinity or if new distance is less than the present I distance
                        distance[i] = 1 + distance[current]  # distance to i node is current's distance + 1
                        edge_from[i] = current   # i came from edge connected to current

        current = hero_node
        next_node = edge_from[current]


        if next_node is monster_node:
            self.movement_queue.append(monster_node)

            current = self.movement_queue.pop()
            self.position[1] = current // self.x  # update position of monster
            self.position[0] = current % self.x
            self.node = current
            return

        elif edge_from[next_node] is monster_node:
            return
        else:
            movement = []

            while next_node is not monster_node:  # finds from hero to monster
                current = next_node
                movement.insert(0, current)
                next_node = edge_from[current]
            for i in range(len(movement)):
                if i < 1:
                    self.movement_queue.append(movement[i])
                else:
                    break
            # current is the next node that monster should move too
            current = self.movement_queue.pop()
            self.position[1] = current // self.x  # update position of monster
            self.position[0] = current % self.x
            self.node = current


