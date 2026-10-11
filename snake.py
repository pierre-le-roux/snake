import pygame
import random

class SnakeGame:
    def __init__(self, window_size, grid_size, speed):
        # Initialize pygame
        pygame.init()

        # Set the window size
        self.window_size = window_size

        # Create the window
        self.screen = pygame.display.set_mode(window_size)

        # Set the title of the window
        pygame.display.set_caption("Snake")

        # Set the dimensions of each grid square
        self.grid_size = grid_size

        # Set the width and height of the grid in squares
        self.grid_width = window_size[0] // grid_size
        self.grid_height = window_size[1] // grid_size

        # Set the colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)

        # Set the initial position of the snake
        self.snake_positions = [(self.grid_width // 2, self.grid_height // 2)]

        # Set the initial direction of the snake
        self.snake_direction = (1, 0)

        # Set the initial previous direction of the snake
        self.prev_direction = (1, 0)

        # Set the initial speed of the snake (in squares per frame)
        self.speed = speed

        # Set the font for rendering the score
        self.font = pygame.font.Font(None, 36)

        # Set the initial score
        self.score = 0

        # Generate the initial position of the food
        self.food_position = (random.randint(0, self.grid_width - 1), random.randint(0, self.grid_height - 1))

        # Set the game clock
        self.clock = pygame.time.Clock()

        # Set the game over flag
        self.game_over = False

    def run_game(self):
        while not self.game_over:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        # Don't allow the snake to turn directly upon itself
                        if self.prev_direction != (0, 1):
                            self.snake_direction = (0, -1)
                    elif event.key == pygame.K_DOWN:
                        # Don't allow the snake to turn directly upon itself
                        if self.prev_direction != (0, -1):
                            self.snake_direction = (0, 1)
                    elif event.key == pygame.K_LEFT:
