

from Source.Rogue import room
from Source.Rogue import Hero
from Source.Rogue import Monster
import keyboard

#print("Welcome to Rogue\n")
#start = input("Press 'p' to Play\nPress 'q' to Quit")

ans = True
high_score = 0
once = False

while ans:
    print("Welcome to Rogue\n")
    start = input("Press 'p' to Play.\nPress 'q' to Quit.\n")
    score = 1
    if start == 'p':
        print("~~Game Start~~\n")
        room0 = room()
        hero = Hero(room0)
        monster = Monster(room0)

        while hero.die(monster):  # edge case for hero and monster starting at same spot
            hero = Hero(room0)

        room0.print(hero, monster)
        print("Game Start:\n")

        while 1:
            hero.move()
            if hero.at_exit is True:
                room0.print(hero, monster)
                print("\nYOU WON!\nPlay Again?\n")
                if not once:
                    high_score = score
                    once = True
                elif high_score > score and once:
                    high_score = score
                break
            if hero.die(monster):
                room0.print(hero, monster)
                print("High Score:", high_score, "\nYOU LOSE!\nGAME OVER.\n")
                break
            monster.pursue_hero(hero, room0.get_room_nodes())

            if hero.die(monster):
                room0.print(hero, monster)
                print("High Score:", high_score, "\nYOU LOSE!\nGAME OVER.\n")
                break
            room0.print(hero, monster)
            print("Current Score:", score, "\nHigh Score:", high_score, "\n")


            score = score + 1

    elif start == 'q':
        print("High Score:", high_score, "\nThank you for playing.")
        ans = False