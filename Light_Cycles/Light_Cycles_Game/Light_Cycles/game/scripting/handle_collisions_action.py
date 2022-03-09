import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    # def _handle_food_collision(self, cast):
    #     """Updates the score nd moves the food if the snake collides with the food.
        
    #     Args:
    #         cast (Cast): The cast of Actors in the game.
    #     """
    #     score = cast.get_first_actor("scores")
    #     food = cast.get_first_actor("foods")
    #     cycle = cast.get_first_actor("cycles")
    #     head = cycle.get_head()

    #     if head.get_position().equals(food.get_position()):
    #         points = food.get_points()
    #         cycle.grow_tail(points)
    #         score.add_points(points)
    #         food.reset()
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle = cast.get_first_actor("cycles")
        head = cycle.get_segments()[0]
        segments = cycle.get_segments()[1:]
        cycle2 = cast.get_second_actor("cycles")
        head2 = cycle2.get_segments()[0]
        segments2 = cycle2.get_segments()[1:]
        
        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
            elif head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycle and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycle = cast.get_first_actor("cycles")
            segments = cycle.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)