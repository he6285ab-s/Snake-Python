"""Main part of the structure that holds the main game loop."""
import pygame
import Values as v
from AdamAndEve import Snake, Apple


# Set up
pygame.init()
screen = pygame.display.set_mode((v.PLAY_AREA, v.PLAY_AREA + v.SCORE_AREA))
screen.fill((0, 0, 0))
pygame.display.set_caption("Snake")
pygame.display.flip()

# Set up score rect
scoreText = pygame.font.Font('freesansbold.ttf', 60)
scoreSurf = scoreText.render("Score: 0", True, pygame.Color(255, 255, 255))
scoreRect = scoreSurf.get_rect()
scoreRect.center = (int((v.PLAY_AREA - scoreRect.width) / 2),
                    int(v.PLAY_AREA + (v.SCORE_AREA - scoreRect.height) / 2))
screen.blit(scoreSurf, scoreRect.center)

# ---------  Help methods ---------- #


def incr_score(snake):
    """Increases the snake's score by 1 and updates the score text field."""
    snake.score += 1
    global scoreSurf
    scoreSurf = scoreText.render("Score: {}".format(
        snake.score), True, pygame.Color(255, 255, 255))


def draw_block(pos, color):
    """Draw a block at corner with width BLOCK_SIZE in passed color.
    Note that the passed pos is in game block coordinates, not pixel coordinates."""
    pygame.draw.rect(screen, color, (pos[0] * v.BLOCK_SIZE + pos[0],
                                     pos[1] * v.BLOCK_SIZE + pos[1], v.BLOCK_SIZE, v.BLOCK_SIZE))


def draw_lines():
    """Draw game layout."""
    x_line = 1
    while x_line <= v.BLOCK_WIDTH:
        pygame.draw.line(screen, v.line_c, (x_line*v.BLOCK_SIZE + x_line - 1, 0),
                         (x_line*v.BLOCK_SIZE + x_line - 1, v.PLAY_AREA), 1)
        x_line += 1

    y_line = 1
    while y_line <= v.BLOCK_WIDTH:
        pygame.draw.line(screen, v.line_c, (0, y_line*v.BLOCK_SIZE + y_line - 1),
                         (v.PLAY_AREA, y_line*v.BLOCK_SIZE + y_line - 1), 1)
        y_line += 1


# --------- Main method ---------- #


def __main__():
    # Set up game
    running = True
    snake = Snake()

    snake.direction = v.right
    apple = Apple(snake)

    while running:
        # Handle game timing and input events
        pygame.time.delay(200 - snake.score * 1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            if event.type == pygame.KEYDOWN:
                snake.update_dir(event.key)

        # Redraw background
        # TODO optimize this somehow? seems ineffective
        screen.fill(v.bkgrnd_c)
        draw_lines()

        draw_block(apple.position, v.apple_c)

        # Move and draw the snake unless collision occured
        if snake.move():
            for pos in snake.position:
                draw_block(pos, v.snake_c)
        else:
            running = False

        # Detect if the snake has eaten an apple
        if apple.detect_eaten():
            snake.grow()
            draw_block(apple.randomize_pos(), v.apple_c)
            incr_score(snake)

        # Drawing the score
        screen.blit(scoreSurf, scoreRect.center)

        # Update changes to the display
        pygame.display.update()

    print("\nYou lost!\n")


if __name__ == "__main__":
    __main__()
