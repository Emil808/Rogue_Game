
from Source.Rogue import room


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