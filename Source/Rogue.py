
import random
import sys
class room:
    def __init__(self):
        self.x = random.randint(10, 30)  # x dimension of the room
        self.y = random.randint(10, 15)  # y dimension of the room

    def print(self):
        print("")
        for j in range(self.y):
            for i in range(self.x):
                print('#', end='')
            print("")