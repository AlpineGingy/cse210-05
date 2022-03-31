from itertools import cycle
from turtle import position
import constants
import random
from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.cast import Cast


class Bullet(Actor):
    """
    An Awesome Light Cycle
    
    The responsibility of Cycle is to move itself and leave a trail behind.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self._bullets = []

    def get_bullets(self):
        return self._bullets

    def __iter__(self):
        for bullet in self._bullets:
            yield bullet

    def move_next(self):
        # move all segments
        for bullet in self._bullets:
            bullet.move_next()

    


        # update velocities
        for i in range(len(self._bullets) - 1, 0, -1):
            trailing = self._bullets[i]
            previous = self._bullets[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_bullet(self):
        return self._bullets[0]
    
    def remove_bullet(self, i):
        self._bullets.pop(i)
        


    def turn_head(self, velocity):
        self._bullets[0].set_velocity(velocity)

    def _prepare_body(self, velocity, cast):
        ship = cast.get_first_actor("ship")
        position = ship.get_position()
        text = "^"
        color = constants.WHITE
        
        bullet = Actor()
        bullet.set_position(position)
        bullet.set_velocity(velocity)
        bullet.set_text(text)
        bullet.set_color(color)
        self._bullets.append(bullet)
