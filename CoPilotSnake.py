import pygame
import time
import random

WIDTH, HEIGHT = 640, 480
ROWS, COLS = 20, 20
SQUARE_SIZE = WIDTH // COLS

# RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Snake:
    def __init__(self):
        self.body = [[5, 10], [5, 11], [5, 12]]
        self.direction = "UP"

    def move(self, apple):
        head = self.body[0].copy()
        if self.direction == "UP":
            head[0] -= 1
        if self.direction == "DOWN":
            head[0] += 1
        if self.direction == "LEFT":
            head[1] -= 1
        if self.direction == "RIGHT":
            head[1] += 1
        self.body.insert(0, head)
        if head == apple.position:
            apple.new_position(self)
            return True
        self.body.pop()
        return False

    def draw(self, win):
        for part in self.body:
            pygame.draw.rect(win, WHITE, (part[1]*SQUARE_SIZE, part[0]*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

class Apple:
    def __init__(self, snake):
        self.position = [random.randint(0, ROWS-1), random.randint(0, COLS-1)]
        while self.position in snake.body:
            self.position = [random.randint(0, ROWS-1), random.randint(0, COLS-1)]

    def new_position(self, snake):
        self.position = [random.randint(0, ROWS-1), random.randint(0, COLS-1)]
        while self.position in snake.body:
            self.position = [random.randint(0, ROWS-1), random.randint(0, COLS-1)]

    def draw(self, win):
        pygame.draw.rect(win, RED, (self.position[1]*SQUARE_SIZE, self.position[0]*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def main():
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    snake = Snake()
    apple = Apple(snake)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_UP]:
                    snake.direction = "UP"
                if keys[pygame.K_DOWN]:
                    snake.direction = "DOWN"
                if keys[pygame.K_LEFT]:
                    snake.direction = "LEFT"
                if keys[pygame.K_RIGHT]:
                    snake.direction = "RIGHT"

        win.fill((0,0,0))
        snake.draw(win)
        apple.draw(win)
        pygame.display.update()

        if snake.move(apple):
            print("Score:", len(snake.body))

        clock.tick(10)

    pygame.quit()

main()
