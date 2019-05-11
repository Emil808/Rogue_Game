
from Source.Rogue import room
from Source.Rogue import Hero
from Source.Rogue import Monster
import time
class Test_room(object):
    def setup_class(self):
        print("Starting Test for Room")

    def test_room_generation(self):
        t1 = time.time()
        room0 = room()
        t0 = time.time()
        exec_time = t0 - t1
        print("Nodes: ", room0.x * room0.y)
        print("Edges: ", room0.edges)
        print("Room Generation Time: ", exec_time)

    def test_room_generation1(self):
        t1 = time.time()
        room0 = room()
        t0 = time.time()
        exec_time = t0 - t1
        print("Nodes: ", room0.x * room0.y)
        print("Edges: ", room0.edges)
        print("Room Generation Time: ", exec_time)

    def test_room_generation2(self):
        t1 = time.time()
        room0 = room(10, 10)
        t0 = time.time()
        exec_time = t0 - t1
        print("Nodes: ", room0.x * room0.y)
        print("Edges: ", room0.edges)
        print("Room Generation Time: ", exec_time)

    def test_room_generation3(self):
        t1 = time.time()
        room0 = room(50, 50)
        t0 = time.time()
        exec_time = t0 - t1
        print("Nodes: ", room0.x * room0.y)
        print("Edges: ", room0.edges)
        print("Room Generation Time: ", exec_time)

    def test_room_generation4(self):
        t1 = time.time()
        room0 = room(70, 70)
        t0 = time.time()
        exec_time = t0 - t1
        print("Nodes: ", room0.x * room0.y)
        print("Edges: ", room0.edges)
        print("Room Generation Time: ", exec_time)

    def test_room_generation5(self):
        t1 = time.time()
        room0 = room(100, 100)
        t0 = time.time()
        exec_time = t0 - t1
        print("Nodes: ", room0.x * room0.y)
        print("Edges: ", room0.edges)
        print("Room Generation Time: ", exec_time)

    def test_room_generation6(self):
        t1 = time.time()
        room0 = room(150, 150)
        t0 = time.time()
        exec_time = t0 - t1
        print("Nodes: ", room0.x * room0.y)
        print("Edges: ", room0.edges)
        print("Room Generation Time: ", exec_time)

    def test_room_generation7(self):
        t1 = time.time()
        room0 = room(200, 200)
        t0 = time.time()
        exec_time = t0 - t1
        print("Nodes: ", room0.x * room0.y)
        print("Edges: ", room0.edges)
        print("Room Generation Time: ", exec_time)

    def test_room_generation_1(self):
        room0 = room()
        print(room0.get_room_nodes())

    def test_room_connection(self):
        room0 = room()

        connections = room0.get_room_nodes()
        print("Room Connections")
        print(connections.vertices)

    def test_hero_generation(self):
        room0 = room()
        hero = Hero(room0)
        monster = Monster(room0)
        room0.print(hero, monster)

    # todo: times for running: room generation, bed on nodes in the room
    def test_monster_generation(self):
        room0 = room()
        hero = Hero(room0)
        monster = Monster(room0)
        room0.print(hero, monster)

    def test_hero_move(self):
        room0 = room()
        hero = Hero(room0)
        monster = Monster(room0)
        room0.print(hero, monster)
        hero.move()
        room0.print(hero, monster)

    def test_pursue_hero(self):
        room0 = room()
        hero = Hero(room0)
        monster = Monster(room0)
        room0.print(hero, monster)
        t1 = time.time()
        monster.pursue_hero(hero, room0.get_room_nodes())
        t0 = time.time()
        exec_time = t0 - t1
        print("Nodes: ", room0.x * room0.y)
        print("Time: ", exec_time)
        print("Edges: ", room0.edges)
        print("done")

    def test_pursue_hero1(self):
        room0 = room(50, 50)
        hero = Hero(room0)
        monster = Monster(room0)

        t1 = time.time()
        monster.pursue_hero(hero, room0.get_room_nodes())
        t0 = time.time()
        exec_time = t0 - t1
        print("Nodes: ", room0.x * room0.y)
        print("Edges: ", room0.edges)
        print("Time: ", exec_time)

        print("done")

    def test_pursue_hero2(self):
        room0 = room(100, 100)
        hero = Hero(room0)
        monster = Monster(room0)


        t1 = time.time()
        monster.pursue_hero(hero, room0.get_room_nodes())
        t0 = time.time()
        exec_time = t0 - t1
        print("Nodes: ", room0.x * room0.y)
        print("Time: ", exec_time)
        print("Edges: ", room0.edges)
        print("done")

    def test_pursue_hero3(self):
        room0 = room(150, 150)
        hero = Hero(room0)
        monster = Monster(room0)


        t1 = time.time()
        monster.pursue_hero(hero, room0.get_room_nodes())
        t0 = time.time()
        exec_time = t0 - t1
        print("Nodes: ", room0.x * room0.y)
        print("Time: ", exec_time)
        print("Edges: ", room0.edges)
        print("done")

    def test_pursue_hero4(self):
        room0 = room(200, 200)
        hero = Hero(room0)
        monster = Monster(room0)

        t1 = time.time()
        monster.pursue_hero(hero, room0.get_room_nodes())
        t0 = time.time()
        exec_time = t0 - t1
        print("Nodes: ", room0.x * room0.y)
        print("Time: ", exec_time)
        print("Edges: ", room0.edges)
        print("done")

    def test_pursue_hero5(self):
        room0 = room(300, 300)
        hero = Hero(room0)
        monster = Monster(room0)

        t1 = time.time()
        monster.pursue_hero(hero, room0.get_room_nodes())
        t0 = time.time()
        exec_time = t0 - t1
        print("Nodes: ", room0.x * room0.y)
        print("Time: ", exec_time)
        print("Edges: ", room0.edges)
        print("done")

    def test_pursue_hero6(self):
        room0 = room(900, 9.00)
        hero = Hero(room0)
        monster = Monster(room0)


        t1 = time.time()
        monster.pursue_hero(hero, room0.get_room_nodes())
        t0 = time.time()
        exec_time = t0 - t1
        print("Nodes: ", room0.x * room0.y)
        print("Time: ", exec_time)
        print("Edges: ", room0.edges)
        print("done")

    def test_pursue_hero7(self):
        room0 = room(800, 800)
        hero = Hero(room0)
        monster = Monster(room0)


        t1 = time.time()
        monster.pursue_hero(hero, room0.get_room_nodes())
        t0 = time.time()
        exec_time = t0 - t1
        print("Nodes: ", room0.x * room0.y)
        print("Time: ", exec_time)
        print("Edges: ", room0.edges)
        print("done")

    def test_pursue_hero8(self):
        room0 = room(1000, 1000)
        hero = Hero(room0)
        monster = Monster(room0)


        t1 = time.time()
        monster.pursue_hero(hero, room0.get_room_nodes())
        t0 = time.time()
        exec_time = t0 - t1
        print("Nodes: ", room0.x * room0.y)
        print("Time: ", exec_time)
        print("Edges: ", room0.edges)
        print("done")