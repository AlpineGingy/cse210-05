from game.casting.cycle import Cycle
from game.casting.actor import Actor
from game.shared.point import Point
import constants


class Cycle2(Cycle):

    def __init__(self):
        super().__init__()

        def _prepare_body(self):
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)

            for i in range(constants.CYCLE_LENGTH):
                position = Point(x - i * constants.CELL_SIZE, y)
                velocity = Point(1 * constants.CELL_SIZE, 0)
                text = "8" if i == 0 else "#"
                color = constants.RED if i == 0 else constants.RED
                
                segment = Actor()
                segment.set_position(position)
                segment.set_velocity(velocity)
                segment.set_text(text)
                segment.set_color(color)
                self._segments.append(segment)