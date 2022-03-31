from itertools import cycle
import constants
import random
from game.casting.actor import Actor
from game.shared.point import Point


class Ship(Actor):
    """
    An Awsome Light Cycle
    
    The responsibility of Cycle is to move itself and leave a trail behind.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self._segments = []
        self._prepare_body()

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()


        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]
    
    def get_position(self):
        return self.get_head().get_position()

    def turn_head(self, velocity):
        for segment in self._segments:
            segment.set_velocity(velocity)

    def _prepare_body(self):
        x = 800
        y = 500

        for i in range(1):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = ".^." if i == 0 else "#"
            color = constants.WHITE if i == 0 else constants.RED

            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)