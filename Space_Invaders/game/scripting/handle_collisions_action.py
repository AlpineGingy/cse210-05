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
    #     """Sets the game over flag if the cycle collides with one of its segments.
        
    #     Args:
    #         cast (Cast): The cast of Actors in the game.
    #     """
    #     cycle = cast.get_first_actor("cycles")
    #     self.head = cycle.get_segments()[0]
    #     segments = cycle.get_segments()[1:]
    #     cycle2 = cast.get_second_actor("cycles")
    #     self.head2 = cycle2.get_segments()[0]
    #     segments2 = cycle2.get_segments()[1:]
        ship = cast.get_first_actor('ship')
        Bullet = cast.get_first_actor('bullet')
        bullets = Bullet.get_bullets()
        first_alienLine1 = cast.get_first_actor('alienLine1')
        first_line_aliens = first_alienLine1.get_aliens()
        first_alienLine2 = cast.get_first_actor('alienLine2')
        second_line_aliens = first_alienLine2.get_aliens()
        first_alienLine3 = cast.get_first_actor('alienLine3')
        third_line_aliens = first_alienLine3.get_aliens()
        first_alienLine4 = cast.get_first_actor('alienLine4')
        fourth_line_aliens = first_alienLine4.get_aliens()

        for alien in first_line_aliens:
            if alien.get_position().get_y() >= 500:
                self._is_game_over = True
                self._message = "Aliens Win"
            else:
                for bullet in bullets:
                    if alien.get_position().equals(bullet.get_position()):
                        Bullet.remove_bullet(bullet + 1)

        for alien in second_line_aliens:
            if alien.get_position().get_y() >= 500:
                self._is_game_over = True
                self._message = "Aliens Win"
        for alien in third_line_aliens:
            if alien.get_position().get_y() >= 500:
                self._is_game_over = True
                self._message = "Aliens Win"
        for alien in fourth_line_aliens:
            if alien.get_position().get_y() >= 500:
                self._is_game_over = True
                self._message = "Aliens Win"

        for bullet in bullets:
            x =+ 1
            if bullet.get_position().get_y() <= 10:
                Bullet.remove_bullet(x)


    #     for segment in segments:
    #         if self.head.get_position().equals(segment.get_position()):
    #             self._is_game_over = True
    #             self._winner = "Player 2 Wins"
    #         elif self.head2.get_position().equals(segment.get_position()):
    #             self._is_game_over = True
    #             self._winner = "Player 1 Wins"
    #         elif self.head.get_position().equals(self.head2.get_position()):
    #             self._is_game_over = True
    #             self._winner = "Nobody Wins"

    #     for segment2 in segments2:
    #         if self.head.get_position().equals(segment2.get_position()):
    #             self._is_game_over = True
    #             self._winner = "Player 2 Wins"
    #         elif self.head2.get_position().equals(segment2.get_position()):
    #             self._is_game_over = True
    #             self._winner = "Player 1 Wins"
    #         elif self.head.get_position().equals(self.head2.get_position()):
    #             self._is_game_over = True
    #             self._winner = "Nobody Wins"
        
    def _handle_game_over(self, cast):
    #     """Shows the 'game over' message and turns the cycle and food white if the game is over.
        
    #     Args:
    #         cast (Cast): The cast of Actors in the game.
    #     """
         if self._is_game_over:

             x = int(constants.MAX_X / 2)
             y = int(constants.MAX_Y / 2)
             position = Point(x, y)

             message = Actor()
             message.set_text(f"Game Over! {self._message}")
             message.set_position(position)
             cast.add_actor("messages", message)
