

from Source.Rogue import room
from Source.Rogue import Hero
from Source.Rogue import Monster
import keyboard

#print("Welcome to Rogue\n")
#start = input("Press 'p' to Play\nPress 'q' to Quit")

ans = True
while ans:
    print("Welcome to Rogue\n")
    start = input("Press 'p' to Play.\nPress 'q' to Quit.\n")
    if start == 'p':
        room0 = room()
        hero = Hero(room0)
        monster = Monster(room0)

        while hero.die(monster):  # edge case for hero and monster starting at same spot
            hero = Hero(room0)

        room0.print(hero, monster)
        print("Game Start:\n")

        while 1:
            hero.move()
            if hero.die(monster):
                room0.print(hero, monster)
                print("YOU LOSE!\nGAME OVER.\n")
                break
            monster.pursue_hero(hero.get_position(), room0.get_room_nodes())
            if hero.die(monster):
                room0.print(hero, monster)
                print("YOU LOSE!\nGAME OVER.\n")
                break
            room0.print(hero, monster)


    elif start == 'q':
        print("Thank you for playing.")
        ans = False