import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size
WINDOW_SIZE = (400, 400)

# Create the window
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the title of the window
pygame.display.set_caption("Snake")

# Set the dimensions of each grid square
GRID_SIZE = 20

# Set the width and height of the grid in squares
GRID_WIDTH = WINDOW_SIZE[0] // GRID_SIZE
GRID_HEIGHT = WINDOW_SIZE[1] // GRID_SIZE

# Set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set the initial position of the snake
snake_positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]

# Set the initial direction of the snake
snake_direction = (1, 0)

# Set the initial speed of the snake (in squares per frame)
speed = 10

# Set the font for rendering the score
font = pygame.font.Font(None, 36)

# Set the initial score
score = 0

# Generate the initial position of the food
food_position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Set the game clock
clock = pygame.time.Clock()

# Set the game over flag
game_over = False

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                snake_direction = (1, 0)

    # Update the snake position
    snake_positions.insert(0, (snake_positions[0][0] + snake_direction[0], snake_positions[0][1] + snake_direction[1]))

    # Check if the snake has eaten the food
    if snake_positions[0] == food_position:
        # Increment the score
        score += 1

        # Generate a new food position
        food_position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        # Remove the last square of the snake
        snake_positions.pop()

    # Check if the snake has collided with the wall or itself
    if (
        snake_positions[0][0] < 0
        or snake_positions[0][0] >= GRID_WIDTH
        or snake_positions[0][1] < 0
        or snake_positions[0][1] >= GRID_HEIGHT
        or snake_positions[0] in snake_positions[1:]
    ):
        game_over = True

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the snake
    for position in snake_positions:
        pygame.draw.rect(
            screen, WHITE, pygame.Rect(position[0] * GRID_SIZE, position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        )

    # Draw the food
    pygame.draw.rect(
        screen, RED, pygame.Rect(food_position[0] * GRID_SIZE, food_position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    )

    # Render the score
    score_text = font.render("Score: {}".format(score), 1, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(speed)

# Display the game over screen
game_over_text = font.render("Game Over", 1, WHITE)
screen.blit(game_over_text, (100, 200))
pygame.display.update()

# Wait for the user to close the window
pygame.time.wait(3000)

# Quit pygame
pygame.quit()