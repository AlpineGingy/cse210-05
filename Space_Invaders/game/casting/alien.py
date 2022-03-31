import constants
import random
from game.casting.actor import Actor
from game.shared.point import Point


class Alien(Actor):
    def __init__(self):
        super().__init__()
        self._aliens = []
        self._prepare_body()
        

    def get_aliens(self):
        return self._aliens

    def move_next(self):
        # move all segments
        for alien in self._aliens:
            alien.move_next()


        # # update velocities
        # for i in range(len(self._aliens) - 1, 0, -1):
        #     trailing = self._aliens[i]
        #     previous = self._aliens[i - 1]
        #     velocity = previous.get_velocity()
        #     trailing.set_velocity(velocity)

    def move_down(self):
        for alien in self._aliens:
                y = alien.get_position().get_y() + 20
                x = alien.get_position().get_x()
                alien.set_position(Point(x, y))

    def get_head(self):
        return self._aliens[0]

    def add_alien(self, number_of_aliens):
        for i in range(number_of_aliens):
            tail = self._aliens[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            alien = Actor()
            alien.set_position(position)
            alien.set_velocity(velocity)
            alien.set_text("#")
            alien.set_color(constants.RED)
            self._aliens.append(alien)
    
    def remove_alien(self, i):
        self._aliens.pop(i)

    def turn_aliens(self, velocity):
        for alien in self._aliens:
            alien.set_velocity(velocity)

    def _prepare_body(self):
        DEFAULT_IMAGE_SIZE = (20, 20)
        # invaderImage1 = pygame.image.load('messing_around/images/alien.png')
        # invaderImage = pygame.transform.scale(invaderImage1, DEFAULT_IMAGE_SIZE)
        x = 800
        y = 100

        for row in range(5):
            for i in range(20):
                position = Point(x - i * constants.CELL_SIZE, y + row * constants.CELL_SIZE)
                # if i == 4 and row == 0:
                #     continue
                velocity = Point(1 * constants.CELL_SIZE, 0)
                text = "A"
                #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]
                color = constants.GREEN

                
                alien = Actor()
                alien.set_position(position)
                alien.set_velocity(velocity)
                alien.set_text(text)
                alien.set_color(color)
                self._aliens.append(alien)