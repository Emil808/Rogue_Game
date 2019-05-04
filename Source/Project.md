
# Rogue

Goals:
	
	Implement rogue game
	Implement automatic Monster
	Implement Automatic Player Character

Needed for game:
    
    map generator
    Characters, position [x][y] 
 	    player, will Die if monster is in same space
 	    monster, monster needs to Pursue player

characters can Move within a map

possible functions
    
    Map generation
    Move
    Position
    Pursue
    Die
    Player: Move, Die
    Monster: Move, Pursue

Map generation will be a grid of nodes

player and monster will have positions within it

at initialization of map, 
      
    monster will use a graph algorithm to find path to player
	after player move, monster moves
 	graph algorithm from last player position to update path for monster. 

Also need to make an automatic player character,
	
	graph algorithm for pathfinding to avoid monster