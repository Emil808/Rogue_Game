
from Source.Rogue import room
from Source.Rogue import Hero
from Source.Rogue import Monster

class Test_room(object):
    def setup_class(self):
        print("Starting Test for Room")

    def test_room_generation(self):
        room0 = room()
        room0.print()

    def test_room_generation_1(self):
        room0 = room()
        room0.print()

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
        monster.pursue_hero(hero.get_position(), room0.get_room_nodes())
        print("done")