import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.alien import Alien

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

    def _handle_segment_collision(self, cast):
        ship = cast.get_first_actor('ship')
        bullet_object = cast.get_first_actor('bullet')
        bullets = bullet_object.get_bullets()
        first_alienLine1:Alien = cast.get_first_actor('alienLine1')
        first_line_aliens = first_alienLine1.get_aliens()
        hit_alien_index = 0
        for alien in first_line_aliens:
            if alien.get_position().get_y() == 500:                
                self._is_game_over = True
                self._message = "You got invaded..."
            hit_bullet_index = 0
            for bullet in bullet_object:
                if alien.get_position().equals(bullet.get_position()):
                    bullet_object.remove_bullet(hit_bullet_index)
                    first_alienLine1.remove_alien(hit_alien_index)
                hit_bullet_index += 1
            hit_alien_index += 1

        x = 0
        for bullet in bullets:
            if bullet.get_position().get_y() <= 20:
                bullet_object.remove_bullet(x)
            x += 1
        
        if len(first_line_aliens):
            pass

        else:
            self._is_game_over = True
            self._message = "Congratulations! You beat the Space Invaders"
    
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
