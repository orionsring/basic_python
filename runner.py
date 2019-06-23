


from amaze.maze import NORTH, SOUTH, WEST, EAST

DIRECTIONS = [EAST, NORTH, WEST, SOUTH]
LEFT_HAND_DIR = [NORTH, WEST, SOUTH, EAST]

def run(maze):
    """Solves the maze by a simple search: always keep
	wall, starting top left and ending at bottom right
	"""
	
	runner = Runner(maze)
	yield runner.location
    while not runner.destination_reached():
        runner.step()
        yield runner.location 
            import pdb
        pdb.set_trace()

class Runner(object):
    """This class runs the maze by keeping its 'left hand
	It starts at the bottom left and ends at the bottom right
    """
    def __init__(self, maze):
        self._dir = 0
        self._x   = 0
        self._y   = 0
        self._maze = maze

    @property 
    def location(self):
        return self._x, self._y 

    @property 
    def direction(self):
        return self._dir 

    def step(self):
    """

    """	
	
	
	