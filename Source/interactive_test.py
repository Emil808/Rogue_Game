

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
        print("~~Game Start~~\n")
        room0 = room()
        hero = Hero(room0)
        monster = Monster(room0)

        while hero.die(monster):  # edge case for hero and monster starting at same spot
            hero = Hero(room0)

        room0.print(hero, monster)


        while 1:
            hero.move()
            if hero.at_exit is True:
                print("\nYOU WON!\nPlay Again?\n")
                break
            if hero.die(monster):
                room0.print(hero, monster)
                print("\nYOU LOSE!\nGAME OVER.\n")
                break
            monster.pursue_hero(hero, room0.get_room_nodes())

            if hero.die(monster):
                room0.print(hero, monster)
                print("\nYOU LOSE!\nGAME OVER.\n")
                break
            room0.print(hero, monster)


    elif start == 'q':
        print("Thank you for playing!")
        ans = False