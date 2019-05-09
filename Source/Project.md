
# Rogue

Accomplished:

    Generate one rectangle room
    spawn one Hero, and one Monster in room
    Implemented exit woor for Hero to get too
    score keeps track of amount of moves Hero stayed alive
    win state when Hero reaches door way 
Goals:

	Fix automatic Monster
	Implement Automatic Player Character
	Implement attacking/defending, health
	Implement treasure to boost attacking/defending, health 
	Level system to improve A/D/H
	More rooms
	halways between rooms
	Multiple monsters
	GUI?

BUGS:

    monster not going next to player, always one space away. this was done to allow player to move around monster
Essentials for game:
    
    Room generation 
    Characters, position [x][y] 
 	    player, will Die if monster is in same space
 	    monster, monster needs to Pursue player

Possible Features

    ?
Character class
    
    Generation: randomly places character within limits of the room
    Move : take command input from keyboard or from a movement queue. validate that commanded
           move is within the map limits
           
    Position : save previous and current position
    Pursue   : path finding function for monster to player. shortest path function, use Dijkstra
    Die      : if monster and player share same position, player dies
    
    child class of Character class
    Player: Move, Die
    Monster: Move, Pursue

Map generation will be a grid of nodes

player and monster will have positions within it

at initialization of map, 
      
    monster will use a graph algorithm to find path to player

Monster Pursue Player

	after player move, update path to player 
	    graph algorithm from last player position to update path for monster. 
	from movement queue, monster moves
 	
