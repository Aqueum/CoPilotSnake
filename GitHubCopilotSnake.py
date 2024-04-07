import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 1200
window_height = 800
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Set up colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Set up the snake
snake_block_size = 20
snake_speed = 15
snake_list = []

# Set up the initial position of the snake
snake_x = window_width // 2
snake_y = window_height // 2
snake_x_change = 0
snake_y_change = 0

# Set up the initial position of the food
food_x = round(random.randrange(0, window_width - snake_block_size) / 20.0) * 20.0
food_y = round(random.randrange(0, window_height - snake_block_size) / 20.0) * 20.0

# Set up the game clock
clock = pygame.time.Clock()

# Set up the game over flag
game_over = False

# Game loop
while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        snake_x_change = -snake_block_size
        snake_y_change = 0
      elif event.key == pygame.K_RIGHT:
        snake_x_change = snake_block_size
        snake_y_change = 0
      elif event.key == pygame.K_UP:
        snake_y_change = -snake_block_size
        snake_x_change = 0
      elif event.key == pygame.K_DOWN:
        snake_y_change = snake_block_size
        snake_x_change = 0

  # Update the position of the snake
  snake_x += snake_x_change
  snake_y += snake_y_change

  # Draw the snake and the food on the game window
  window.fill(black)
  pygame.draw.rect(window, red, [food_x, food_y, snake_block_size, snake_block_size])
  snake_head = []
  snake_head.append(snake_x)
  snake_head.append(snake_y)
  snake_list.append(snake_head)
  if len(snake_list) > 1:
    del snake_list[0]

  for x in snake_list[:-1]:
    if x == snake_head:
      game_over = True

  for x in snake_list:
    pygame.draw.rect(window, white, [x[0], x[1], snake_block_size, snake_block_size])

  pygame.display.update()

  # Check if the snake has eaten the food
  if snake_x == food_x and snake_y == food_y:
    food_x = round(random.randrange(0, window_width - snake_block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, window_height - snake_block_size) / 20.0) * 20.0

  # Set the game speed
  clock.tick(snake_speed)

# Quit the game
pygame.quit()