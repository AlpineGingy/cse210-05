from turtle import right
from game.casting.alien import Alien
import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.actor import Actor
from game.casting.cast import Cast
from game.scripting.draw_actors_action import DrawActorsAction

LEFT = Point(-constants.CELL_SIZE, 0)
RIGHT= Point(constants.CELL_SIZE, 0)
UP = Point(0, -constants.CELL_SIZE)
DOWN = Point(0, constants.CELL_SIZE)
STILLRIGHT = Point(0, 0)
STILLLEFT = Point(0, 0)

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
        self._direction = LEFT
        self._direction2 = LEFT
        self._direction3 = RIGHT
        self._bullet_direction = UP
        self.cast = Cast()

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
        if self._keyboard_service.is_key_down('space'):
            self._bullet_direction = UP
            bullet = cast.get_first_actor('bullet')
            bullet._prepare_body(self._bullet_direction, cast)



            


        
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
        
        ship1 = cast.get_first_actor("ship")
        ships = ship1.get_segments()
        for ship in ships:
            if ship.get_position().get_x() == 100:
                if self._keyboard_service.is_key_down('d'):
                    self._direction = RIGHT
                    ship1.turn_head(self._direction)
                else:
                    ship1.turn_head(STILLRIGHT)
            elif ship.get_position().get_x() == 800:
                ship1.turn_head(STILLLEFT)
                if self._keyboard_service.is_key_down('a'):
                    self._direction = LEFT
                    ship1.turn_head(self._direction)
                else:
                    ship1.turn_head(STILLRIGHT)
                
            else:
                ship1.turn_head(self._direction)

                

        first_alienLine1:Alien = cast.get_first_actor('alienLine1')
        first_line_aliens = first_alienLine1.get_aliens()
        move_down_right = False
        move_down_left = False
        for alien in first_line_aliens:
            if alien.get_position().get_x() >= 800:
                move_down_right = True
            elif alien.get_position().get_x() <= 100:
                move_down_left = True

        if move_down_right:
            first_alienLine1.turn_aliens(self._direction2)
            first_alienLine1.move_down()
        elif move_down_left:
            first_alienLine1.turn_aliens(self._direction3)
            first_alienLine1.move_down()

        # first_alienLine2 = cast.get_first_actor('alienLine2')
        # second_line_aliens = first_alienLine2.get_aliens()
        # for alien in second_line_aliens:
        #     if alien.get_position().get_x() == 800:
        #         first_alienLine2.turn_aliens(self._direction2)
        #         first_alienLine2.move_down()


        #     elif alien.get_position().get_x() <= 100:
        #         first_alienLine2.turn_aliens(self._direction3)
        #         first_alienLine2.move_down()



        # first_alienLine3 = cast.get_first_actor('alienLine3')
        # third_line_aliens = first_alienLine2.get_aliens()
        # for alien in third_line_aliens:
        #     if alien.get_position().get_x() == 800:
        #         first_alienLine3.turn_aliens(self._direction2)
        #         first_alienLine3.move_down()


        #     elif alien.get_position().get_x() <= 100:
        #         first_alienLine3.turn_aliens(self._direction3)
        #         first_alienLine3.move_down()

        # first_alienLine4 = cast.get_first_actor('alienLine4')
        # fourth_line_aliens = first_alienLine4.get_aliens()
        # for alien in fourth_line_aliens:
        #     if alien.get_position().get_x() == 800:
        #         first_alienLine4.turn_aliens(self._direction2)
        #         first_alienLine4.move_down()


        #     elif alien.get_position().get_x() <= 100:
        #         first_alienLine4.turn_aliens(self._direction3)
        #         first_alienLine4.move_down()



            # cycle2 = cast.get_second_actor("cycles")
            # cycle2.turn_head(self._direction2)