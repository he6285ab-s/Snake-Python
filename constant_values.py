"""Holds game related constant values."""
import pygame

# Key presses
down, up, left, right = pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT
p, r = pygame.K_p, pygame.K_r

# Window constants
BLOCK_SIZE = 25
BLOCK_WIDTH = 21
PLAY_AREA = BLOCK_WIDTH * BLOCK_SIZE + (BLOCK_WIDTH - 1)
SCORE_AREA = 200

# Instruction string
instructions = "'p' to pause, 'r' to restart."

# Colors
color_snake = (100, 200, 80)
color_bkgrnd = (12, 12, 12)
color_line = (72, 72, 72)
color_apple = (240, 0, 0)
color_score_text = (255, 215, 0)
