"""Main part of the structure that holds the main game loop."""
from adam_and_eve import Snake, Apple
from screen import Screen

def __main__():
    # Set up game
    running = True
    snake = Snake()
    apple = Apple(snake)
    screen = Screen(snake, apple)

    while running:
        # Game timing & input events
        if screen.handle_events() == "quit":
            running = False
            return

        # Game logic
        snake.move()
        if snake.detect_collision():
            running = False
            return
        if apple.detect_eaten():
            snake.grow()
            apple.randomize_pos()

        # Update screen
        screen.refresh()

    print("\nYou lost!\n")


if __name__ == "__main__":
    __main__()
