from game.shared.color import Color
import random

COLUMNS = 40
ROWS = 20
CELL_SIZE = 20
MAX_X = 900
MAX_Y = 600
FRAME_RATE = 10
FONT_SIZE = 15
CAPTION = "Cycle"
CYCLE_LENGTH = 8
WHITE = Color(255, 255, 255)
R = random.randint(1,255)
G = random.randint(1,255)
B = random.randint(1,255)
PLAYER1 = Color(R,G,B)
PLAYER2 = Color(G,B,R)
GREEN = Color(0, 255, 0)
YELLOW = Color(255, 255, 0)
RED = Color(255, 0, 0)
BLUE = Color(0, 0, 255)