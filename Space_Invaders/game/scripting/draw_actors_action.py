from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        #score = cast.get_first_actor("scores")
        #food = cast.get_first_actor("foods")
        ship = cast.get_first_actor("ship")
        # cycle = cast.get_first_actor("cycles")
        # cycle2 = cast.get_second_actor("cycles")
        segment = ship.get_segments()
        bullet = cast.get_first_actor('bullet')
        bullets = bullet.get_bullets()
        alienLine1 = cast.get_first_actor("alienLine1")
        aliensLine1 = alienLine1.get_aliens()

        # alienLine2 = cast.get_first_actor("alienLine2")
        # aliensLine2 = alienLine2.get_aliens()

        # alienLine3 = cast.get_first_actor("alienLine3")
        # aliensLine3 = alienLine3.get_aliens()

        # alienLine4 = cast.get_first_actor("alienLine4")
        # aliensLine4 = alienLine4.get_aliens()
        # segments = cycle.get_segments()
        # segments2 = cycle2.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actors(segment)
        self._video_service.draw_actors(aliensLine1)
        # self._video_service.draw_actors(aliensLine2)
        # self._video_service.draw_actors(aliensLine3)
        # self._video_service.draw_actors(aliensLine4)
        self._video_service.draw_actors(bullet)
        #self._video_service.draw_actor(food)
        # self._video_service.draw_actors(segments)
        # self._video_service.draw_actors(segments2)
        #self._video_service.draw_actor(score)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()