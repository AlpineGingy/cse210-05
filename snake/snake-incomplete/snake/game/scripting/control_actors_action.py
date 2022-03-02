from turtle import right
import constants
from game.scripting.action import Action
from game.shared.point import Point

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
        self._direction = Point(constants.CELL_SIZE, 0)
        self._facing = "right"

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        # left
        if self._keyboard_service.is_key_down('a'): # and self._facing != "right":
            self._direction = Point(-constants.CELL_SIZE, 0)
            #self._facing = "left"
        
        # right
        if self._keyboard_service.is_key_down('d'): #and self._facing != "left":
            self._direction = Point(constants.CELL_SIZE, 0)
            #self._facing = "right"
        
        # up
        if self._keyboard_service.is_key_down('w'): #and self._facing != "down":
            self._direction = Point(0, -constants.CELL_SIZE)
           # self._facing = "up"
        
        # down
        if self._keyboard_service.is_key_down('s'): #and self._facing != "up":
            self._direction = Point(0, constants.CELL_SIZE)
           # self._facing = "down"
        
        snake = cast.get_first_actor("snakes")
        snake.turn_head(self._direction)