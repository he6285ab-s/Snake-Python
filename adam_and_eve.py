"""Holds both the snake and apple classes."""
import random
import constant_values as v

# Values for handling key inputs
horisontal = [v.down, v.up]
vertical = [v.left, v.right]

class Apple():
    """Handles the spawned apples that give points."""

    def __init__(self, snake):
        self.snake = snake
        self.randomize_pos()

    def randomize_pos(self):
        """Randomizes a new position for the apple, sets it and returns it."""
        # Generate new position until position not inside snake.
        # (Python does not have a do while-loop, apparently.)
        self.position = self._new_pos()
        while self.position in self.snake.positions:
            self.position = self._new_pos()

    def _new_pos(self):
        return [random.randint(0, v.BLOCK_WIDTH - 1), random.randint(0, v.BLOCK_WIDTH - 1)]

    def detect_eaten(self):
        """Determines if the snake has eaten the apple. Returns true if it has."""
        return self.position in self.snake.positions


class Snake:
    """Holds the values for the player Snake."""

    def __init__(self):
        self.positions = [[10, 10]]
        self.direction = v.right
        self.score = 0

    def update_dir(self, key):
        """Updates the snake's direction."""
        if not key in (v.down, v.up, v.left, v.right):
            return

        # Ignoring inputs that are the same as or the opposite to snake's direction.
        if key in horisontal and self.direction in horisontal:
            return True
        if key in vertical and self.direction in vertical:
            return True

        self.direction = key


    def move(self):
        """Move the snake one block in its direction."""
        for i in range(len(self.positions) - 1, 0, -1):
            self.positions[i] = self.positions[i-1].copy()

        if self.direction == v.down:
            self.positions[0][1] += 1
        elif self.direction == v.up:
            self.positions[0][1] -= 1
        elif self.direction == v.left:
            self.positions[0][0] -= 1
        elif self.direction == v.right:
            self.positions[0][0] += 1

        return not self.detect_collision()

    def detect_collision(self):
        """Determines if the snake has lost by colliding with wall or its own tail.
        Returns true if snake collided."""
        if self.positions[0][0] < 0 or self.positions[0][0] > v.BLOCK_WIDTH - 1:
            return True
        if self.positions[0][1] < 0 or self.positions[0][1] > v.BLOCK_WIDTH - 1:
            return True

        if len(self.positions) > 3:
            for i in range(3, len(self.positions)):
                if positions_equal(self.positions[0], self.positions[i]):
                    return True

        return False

    def grow(self):
        """Increases both the snake's length and score by 1."""
        self.score += 1
        self.positions.append(self.positions[len(self.positions) - 1].copy())

def positions_equal(pos1, pos2):
    """Returns true if x and y values in pos1 and pos2 are equal."""
    return pos1[0] == pos2[0] and pos1[1] == pos2[1]
