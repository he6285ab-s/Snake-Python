"""Main part of the structure that holds the main game loop."""
import pygame
from adam_and_eve import Snake, Apple
from screen import Screen

def __main__():
    # Set up game
    snake = Snake()
    apple = Apple(snake)
    screen = Screen(snake, apple)

    running = True

    while running:
        # Game timing & input events
        if screen.handle_events() == "quit":
            running = False
            return

        # Game logic
        snake.move()
        if apple.detect_eaten():
            snake.grow()
            apple.randomize_pos()
        if snake.detect_collision():
            snake.try_write_hs()
            screen.refresh_high_score()
            pygame.time.delay(500)
            snake.__init__()
            apple.randomize_pos()

        # Update screen
        screen.refresh()


    print("\nYou lost!\n")



if __name__ == "__main__":
    __main__()
