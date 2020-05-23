"""Holds both the snake and apple classes."""
import random
import Values as v


class Apple():
    """Handles the spawned apples that give points."""

    def __init__(self, snake):
        self.snake = snake
        self.randomize_pos()

    def randomize_pos(self):
        """Randomizes a new position for the apple, sets it and returns it."""
        self.position = [random.randint(
            0, v.BLOCK_WIDTH - 1), random.randint(0, v.BLOCK_WIDTH - 1)]

        # Generate new position if the position is within the snake.
        while self.position in self.snake.position:
            self.position = [random.randint(
                0, v.BLOCK_WIDTH), random.randint(0, v.BLOCK_WIDTH)]

        return self.position

    def detect_eaten(self):
        """Determines if the snake has eaten the apple. Returns true if it has."""
        if self.position in self.snake.position:
            return True



class Snake:
    """Holds the values for the player Snake."""

    def __init__(self):
        self.position = [[10, 10], [9, 10], [8, 10], [7, 10], [6, 10]]
        self.direction = 0
        self.score = 0

    def update_dir(self, key):
        """Updates the snake's direction."""
        # TODO find easier way to do this
        if not key in (v.down, v.up, v.left, v.right):
            return
        if key == v.down and self.direction == v.up:
            return
        if key == v.up and self.direction == v.down:
            return
        if key == v.left and self.direction == v.right:
            return
        if key == v.right and self.direction == v.left:
            return

        self.direction = key

    def move(self):
        """Move the snake one block in its direction."""
        for i in range(len(self.position) - 1, 0, -1):
            self.position[i] = self.position[i-1].copy()

        if self.direction == v.down:
            self.position[0][1] += 1
        elif self.direction == v.up:
            self.position[0][1] -= 1
        elif self.direction == v.left:
            self.position[0][0] -= 1
        elif self.direction == v.right:
            self.position[0][0] += 1

        return not self.detect_collision()

    def detect_collision(self):
        """Determines if the snake has lost by colliding with wall or its own tail.
        Returns true if snake collided."""
        if self.position[0][0] < 0 or self.position[0][0] > v.BLOCK_WIDTH - 1:
            return True
        if self.position[0][1] < 0 or self.position[0][1] > v.BLOCK_WIDTH - 1:
            return True

        if len(self.position) > 3:
            for i in range(3, len(self.position)):
                if positions_equal(self.position[0], self.position[i]):
                    return True

        return False

    def grow(self):
        """Increases the snake's length by 1."""
        self.position.append(self.position[len(self.position) - 1].copy())

def positions_equal(pos1, pos2):
    """Returns true if x and y values in pos1 and pos2 are equal."""
    return pos1[0] == pos2[0] and pos1[1] == pos2[1]
