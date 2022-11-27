"""
stores game settings and constants
"""

# Constant Variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Game settings
WINDOW_SIZE = [1280, 720]
MAX_SCORE = 5

BALL_VELOCITY = 5
BALL_COLOR = WHITE
BALL_SIZE = 20

PLAYER_VELOCITY = 3
PLAYER_HEIGHT = 75
PLAYER_WIDTH = 5

# Ball settings
BALL_SETTINGS = {
    "velocity": BALL_VELOCITY,
    "color": WHITE,
    "size": BALL_SIZE,
    "change_color": True,
    "change_size": True,
    "change_velocity": True,
}

# Player 1 settings
PLAYER1_SETTINGS = {
    "velocity": PLAYER_VELOCITY,
    "width": PLAYER_WIDTH,
    "height": PLAYER_HEIGHT,
    "color": WHITE,
    "name": ""
}

# Player 2 settinfs
PLAYER2_SETTINGS = {
    "velocity": PLAYER_VELOCITY,
    "width": PLAYER_WIDTH,
    "height": PLAYER_HEIGHT,
    "color": WHITE,
    "name": ""
}