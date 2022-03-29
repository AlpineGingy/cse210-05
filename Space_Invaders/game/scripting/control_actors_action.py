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
        self._direction2 = LEFT
        self._direction3 = RIGHT

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = LEFT
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = RIGHT
        
        # # Space
        # if self._keyboard_service.is_key_down('space'):
        #     self._direction = UP
        
        # # down
        # if self._keyboard_service.is_key_down('s') and self._direction != UP:
        #     self._direction = DOWN

        #         # left
        # if self._keyboard_service.is_key_down('j') and self._direction2 != RIGHT:
        #     self._direction2 = LEFT
        
        # # right
        # if self._keyboard_service.is_key_down('l') and self._direction2 != LEFT:
        #     self._direction2 = RIGHT
        
        # # up
        # if self._keyboard_service.is_key_down('i') and self._direction2 != DOWN:
        #     self._direction2 = UP
        
        # # down
        # if self._keyboard_service.is_key_down('k') and self._direction2 != UP:
        #     self._direction2 = DOWN
        
        ship = cast.get_first_actor("ship")
        ship.turn_head(self._direction)
        first_alien = cast.get_first_actor('alien')
        aliens = first_alien.get_aliens()
        for alien in aliens:
            if alien.get_position().get_x() >= 800:
                first_alien.turn_aliens(self._direction2)
                # y = alien.get_position().get_y() + 20
                # x = alien.get_position().get_x()
                # alien.set_position(x, y)


            elif alien.get_position().get_x() <= 100:
                first_alien.turn_aliens(self._direction3)
                # y = alien.get_position().get_y() + 20
                # x = alien.get_position().get_x()
                # alien.set_position(x, y)
            # cycle2 = cast.get_second_actor("cycles")
            # cycle2.turn_head(self._direction2)