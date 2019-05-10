
from Source.Rogue import room
from Source.Rogue import Hero
from Source.Rogue import Monster
import time
class Test_room(object):
    def setup_class(self):
        print("Starting Test for Room")

    def test_room_generation(self):
        room0 = room()
        print(room0.get_room_nodes())

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

    # todo: times for running: room generation, print room, based on nodes in the room
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

        print("done")

    def test_pursue_hero1(self):
        room0 = room(50, 50)
        hero = Hero(room0)
        monster = Monster(room0)
        room0.print(hero, monster)

        t1 = time.time()
        monster.pursue_hero(hero, room0.get_room_nodes())
        t0 = time.time()
        exec_time = t0 - t1
        print("Nodes: ", room0.x * room0.y)
        print("Time: ", exec_time)

        print("done")

    def test_pursue_hero2(self):
        room0 = room(100, 100)
        hero = Hero(room0)
        monster = Monster(room0)
        room0.print(hero, monster)

        t1 = time.time()
        monster.pursue_hero(hero, room0.get_room_nodes())
        t0 = time.time()
        exec_time = t0 - t1
        print("Nodes: ", room0.x * room0.y)
        print("Time: ", exec_time)

        print("done")

    def test_pursue_hero3(self):
        room0 = room(500, 500)
        hero = Hero(room0)
        monster = Monster(room0)
        room0.print(hero, monster)

        t1 = time.time()
        monster.pursue_hero(hero, room0.get_room_nodes())
        t0 = time.time()
        exec_time = t0 - t1
        print("Nodes: ", room0.x * room0.y)
        print("Time: ", exec_time)

        print("done")