"""Holds the Screen class."""
import pygame
import constant_values as v


class Screen:
    """Handles the screen related actions, such as drawing and updating."""

    def __init__(self, snake, apple):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.window = pygame.display.set_mode(
            (v.PLAY_AREA, v.PLAY_AREA + v.SCORE_AREA))
        self.window.fill(v.color_bkgrnd)
        # self._draw_score()
        self.snake = snake
        self.apple = apple
        self._init_score_field()
        self.refresh()
        pygame.display.flip()


    def refresh(self):
        """Redraws everything in the window. Use this as an update method."""
        self.window.fill(v.color_bkgrnd)
        self._draw_lines()
        self._draw_objects()
        self.refresh_score_field()
        self.window.blit(self.score_surf, self.score_rect.center)
        self.window.blit(self.high_score_surf, self.high_score_rect.center)
        self.window.blit(self.instr_surf, self.instr_rect)
        pygame.display.update()
        pygame.time.delay(200 - self.snake.score * 1)


    def _init_score_field(self):
        self.score_text_style = pygame.font.Font('freesansbold.ttf', 50)
        self.score_surf = self.score_text_style.render("Score: 0", True, v.color_score_text)
        self.score_rect = self.score_surf.get_rect()
        self.score_rect.center = (int((v.PLAY_AREA - self.score_rect.width) / 2),
                                  int(v.PLAY_AREA + (v.SCORE_AREA - self.score_rect.height) / 6))
        
        try:
            with open("hs.txt") as file:
                hs = file.read()
        except:
            with open("hs.txt", "w") as file:
                file.write("0")
                hs = 0
        
        self.high_score_surf = self.score_text_style.render("High Score: {}".format(hs), True, v.color_score_text)
        self.high_score_rect = self.high_score_surf.get_rect()
        self.high_score_rect.center = (int((v.PLAY_AREA - self.high_score_rect.width) / 2),
                                  int(v.PLAY_AREA + (v.SCORE_AREA - self.high_score_rect.height) / 2))

        self.instr_text_style = pygame.font.Font('freesansbold.ttf', 20)
        self.instr_surf = self.instr_text_style.render(v.instructions, True, v.color_score_text)
        self.instr_rect = self.instr_surf.get_rect()
        self.instr_rect.center = (int(v.PLAY_AREA / 2),
                                  int(v.PLAY_AREA + (v.SCORE_AREA - self.instr_rect.height * 2)))

    def refresh_high_score(self):
        """Sets the value in highscore textfield to the snakes current highscore. 
        Use to update between games."""
        with open("hs.txt") as file:
            hs = int(file.read())
        setattr(self, "high_score_surf", self.score_text_style.render("High Score: {}".format(hs), True, v.color_score_text))

    def refresh_score_field(self):
        """Increases the snake's score by 1 and updates the score text field."""
        setattr(self, "score_surf", self.score_text_style.render(
            "Score: {}".format(self.snake.score), True, v.color_score_text))

    def _draw_lines(self):
        """Draw game layout."""
        x_line = 1
        while x_line <= v.BLOCK_WIDTH:
            pygame.draw.line(self.window, v.color_line, (x_line*v.BLOCK_SIZE + x_line - 1, 0),
                             (x_line*v.BLOCK_SIZE + x_line - 1, v.PLAY_AREA), 1)
            x_line += 1

        y_line = 1
        while y_line <= v.BLOCK_WIDTH:
            pygame.draw.line(self.window, v.color_line, (0, y_line*v.BLOCK_SIZE + y_line - 1),
                             (v.PLAY_AREA, y_line*v.BLOCK_SIZE + y_line - 1), 1)
            y_line += 1

    def _draw_objects(self):
        """(Re)draws both the snake and the apple"""
        for pos in self.snake.positions:
            self._draw_block(pos, v.color_snake)
        self._draw_block(self.apple.position, v.color_apple)

    def _draw_block(self, pos, color):
        """Draw a block at corner with width BLOCK_SIZE in passed color.
        Note that the passed pos is in game block coordinates, not pixel coordinates."""
        coord_x = pos[0] * (v.BLOCK_SIZE + 1)
        coord_y = pos[1] * (v.BLOCK_SIZE + 1)
        pygame.draw.rect(self.window, color, (coord_x, coord_y, v.BLOCK_SIZE, v.BLOCK_SIZE))

    def handle_events(self):
        """Handles game events such as key presses or clicking close button."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                self.snake.update(event.key)
