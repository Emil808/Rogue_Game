
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