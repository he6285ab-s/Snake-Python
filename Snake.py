import pygame
pygame.init()

# set up
BLOCK_SIZE = 25
BLOCK_WIDTH = 20
SCREEN_SIZE = BLOCK_WIDTH * BLOCK_SIZE + (BLOCK_WIDTH - 1)
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
screen.fill((0, 0, 0))
pygame.display.set_caption("Snake")
pygame.display.flip()

# pygame values
down, up, left, right = pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT

# game statics and values
snake_c, bkgrnd_c, line_c = (100, 200, 80), (12, 12, 12), (72, 72, 72)

class Snake:
    """Holds the values for the player Snake."""
    def __init__(self):
        self.head_x = 9 * BLOCK_SIZE + 9
        self.head_y = 9 * BLOCK_SIZE + 9
        self.direction = 0

    def update_dir(self, key):
        """Updates the snake's direction."""
        if not key in (down, up, left, right):
            return
        self.direction = key

    def move(self):
        """Move the snake one block in its direction."""
        if self.direction == down:
            if SCREEN_SIZE - self.head_y >= BLOCK_SIZE:
                self.head_y += BLOCK_SIZE + 1
        elif self.direction == up:
            self.head_y -= BLOCK_SIZE + 1
        elif self.direction == left:
            self.head_x -= BLOCK_SIZE + 1
        elif self.direction == right:
            self.head_x += BLOCK_SIZE + 1

    def draw(self):
        """Draws the snake's head at the correct position."""
        draw_block(self.head_x, self.head_y, snake_c)


def draw_block(x_top_left, y_top_left, color):
    """Draw a block at corcer with width BLOCK_SIZE in passed color."""
    pygame.draw.rect(screen, color, (x_top_left,
                                     y_top_left, BLOCK_SIZE, BLOCK_SIZE))


def draw_lines():
    """Draw game layout."""
    x_line = 1
    while x_line <= BLOCK_WIDTH:
        pygame.draw.line(screen, line_c, (x_line*BLOCK_SIZE + x_line - 1, 0),
                         (x_line*BLOCK_SIZE + x_line - 1, SCREEN_SIZE), 1)
        x_line += 1

    y_line = 1
    while y_line <= BLOCK_WIDTH:
        pygame.draw.line(screen, line_c, (0, y_line*BLOCK_SIZE + y_line - 1),
                         (SCREEN_SIZE, y_line*BLOCK_SIZE + y_line - 1), 1)
        y_line += 1


def __main__():
    running = True
    snake = Snake()

    while running:
        ## Handle game timing and input events
        pygame.time.delay(250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            if event.type == pygame.KEYDOWN:
                snake.update_dir(event.key)

        ## Redraw background
        # TODO optimize this somehow? seems ineffective
        screen.fill(bkgrnd_c)
        draw_lines()

        ## Move and draw the snake
        snake.move()
        snake.draw()

        ## Update changes to the display
        pygame.display.update()


if __name__ == "__main__":
    __main__()
