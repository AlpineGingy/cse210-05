import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.
    """

    def __init__(self):
        #Constructs a new HandleCollisionsAction.
        self._is_game_over = False

    def execute(self, cast, script):
         #Executes the handle collisions action.
         if not self._is_game_over:
             self._handle_segment_collision(cast)
             self._handle_game_over(cast)
        
    def _handle_game_over(self, cast):
    # Shows the 'game over' message and turns the cycle and food white if the game is over.
         if self._is_game_over:

             x = int(constants.MAX_X / 2)
             y = int(constants.MAX_Y / 2)
             position = Point(x, y)

             message = Actor()
             message.set_text(f"Game Over! {self._message}")
             message.set_position(position)
             cast.add_actor("messages", message)
