import pygame

# Key presses
down, up, left, right = pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT

# Window constants
BLOCK_SIZE = 25
BLOCK_WIDTH = 21
PLAY_AREA = BLOCK_WIDTH * BLOCK_SIZE + (BLOCK_WIDTH - 1)
SCORE_AREA = 150


# Colors
snake_c, bkgrnd_c, line_c, apple_c = (100, 200, 80), (12, 12, 12), (72, 72, 72), (240, 0, 0)
