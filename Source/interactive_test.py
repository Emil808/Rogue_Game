

from Source.Rogue import room
from Source.Rogue import Hero
from Source.Rogue import Monster
import keyboard



room0 = room()
hero = Hero(room0)
monster = Monster(room0)
room0.print(hero, monster)
print("Game Start\n")

while 1:
    hero.move()
    room0.print(hero, monster)
    if hero.die(monster):
        print("YOU LOSE!\nGAME OVER.\n")
        break