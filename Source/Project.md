
# Rogue

Goals:
	
	Implement rogue game
	Implement automatic Monster
	Implement Automatic Player Character

Needed for game:
    
    map generator (completed: map generation, undirected-connections for the spaces, printing room)
    Characters, position [x][y] 
 	    player, will Die if monster is in same space
 	    monster, monster needs to Pursue player

characters can Move within a map

Possible Featuers

    Map generation (done) 
    Character generation
    
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
 	

Also need to make an automatic player character,
	
	graph algorithm for pathfinding to avoid monster