from turtle import right
import constants
from game.scripting.action import Action
from game.shared.point import Point

LEFT = Point(-constants.CELL_SIZE, 0)
RIGHT= Point(constants.CELL_SIZE, 0)
UP = Point(0, -constants.CELL_SIZE)
DOWN = Point(0, constants.CELL_SIZE)

class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = RIGHT

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        # left
        if self._keyboard_service.is_key_down('a') and self._direction != RIGHT:
            self._direction = LEFT
        
        # right
        if self._keyboard_service.is_key_down('d') and self._direction != LEFT:
            self._direction = RIGHT
        
        # up
        if self._keyboard_service.is_key_down('w') and self._direction != DOWN:
            self._direction = UP
        
        # down
        if self._keyboard_service.is_key_down('s') and self._direction != UP:
            self._direction = DOWN
        
        cycles = cast.get_actors("cycles")

        for cycle in cycles:
            cycle.turn_head(self._direction)