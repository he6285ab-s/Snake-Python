import pygame
import Values as v
from AdamAndEve import Snake, Apple


# Set up
pygame.init()
screen = pygame.display.set_mode((v.SCREEN_SIZE, v.SCREEN_SIZE))
screen.fill((0, 0, 0))
pygame.display.set_caption("Snake")
pygame.display.flip()


# ---------  Help methods ---------- #

def draw_block(pos, color):
    """Draw a block at corner with width BLOCK_SIZE in passed color. Note that the passed pos is in game block coordinates, not pixel coordinates."""
    pygame.draw.rect(screen, color, (pos[0] * v.BLOCK_SIZE + pos[0], pos[1] * v.BLOCK_SIZE + pos[1], v.BLOCK_SIZE, v.BLOCK_SIZE))

def draw_lines():
    """Draw game layout."""
    x_line = 1
    while x_line <= v.BLOCK_WIDTH:
        pygame.draw.line(screen, v.line_c, (x_line*v.BLOCK_SIZE + x_line - 1, 0),
                         (x_line*v.BLOCK_SIZE + x_line - 1, v.SCREEN_SIZE), 1)
        x_line += 1

    y_line = 1
    while y_line <= v.BLOCK_WIDTH:
        pygame.draw.line(screen, v.line_c, (0, y_line*v.BLOCK_SIZE + y_line - 1),
                         (v.SCREEN_SIZE, y_line*v.BLOCK_SIZE + y_line - 1), 1)
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
        pygame.time.delay(250)
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
            apple.randomize_pos()
            draw_block(apple.position, v.apple_c)
            print(apple.position)

        # Update changes to the display
        pygame.display.update()

    print("\nYou lost!\n")


if __name__ == "__main__":
    __main__()
