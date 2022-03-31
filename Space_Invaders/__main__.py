import constants

from game.casting.cast import Cast
from game.casting.ship import Ship
from game.casting.alien import Alien
from game.casting.bullet import Bullet   
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point



def main():
     
    # create the cast
    cast = Cast()
    cast.add_actor("bullet", Bullet())
    cast.add_actor("ship", Ship())
    cast.add_actor("alienLine1", Alien())
    # cast.add_actor("alienLine2", Alien())
    # first_alienLine2 = cast.get_first_actor('alienLine2')
    # first_alienLine2.move_down()
    # cast.add_actor("alienLine3", Alien())
    # first_alienLine3 = cast.get_first_actor('alienLine3')
    # first_alienLine3.move_down()
    # first_alienLine3.move_down()
    # cast.add_actor("alienLine4", Alien())
    # first_alienLine4 = cast.get_first_actor('alienLine4')
    # first_alienLine4.move_down()
    # first_alienLine4.move_down()
    # first_alienLine4.move_down()
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()