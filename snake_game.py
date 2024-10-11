import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 400
GRID_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = (GRID_SIZE, 0)

    def move(self, food):
        # Update the snake's body
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, new_head)

        # Check for collision with food
        if new_head == food.position:
            food.spawn()
        else:
            self.body.pop()

    def check_collision(self):
        # Check for collision with walls or itself
        head = self.body[0]
        if (
            head[0] < 0 or head[0] >= WINDOW_WIDTH or
            head[1] < 0 or head[1] >= WINDOW_HEIGHT or
            head in self.body[1:]
        ):
            return True
        return False

    def change_direction(self, new_direction):
        # Change snake's direction, but prevent going in the opposite direction
        if (new_direction[0] != -self.direction[0] or
            new_direction[1] != -self.direction[1]):
            self.direction = new_direction

    def draw(self, screen):
        # Draw the snake
        for segment in self.body:
            pygame.draw.rect(screen, WHITE, (*segment, GRID_SIZE, GRID_SIZE))

# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.spawn()

    def spawn(self):
        # Spawn food at a random position
        x = random.randrange(0, WINDOW_WIDTH, GRID_SIZE)
        y = random.randrange(0, WINDOW_HEIGHT, GRID_SIZE)
        self.position = (x, y)

    def draw(self, screen):
        # Draw the food
        pygame.draw.rect(screen, RED, (*self.position, GRID_SIZE, GRID_SIZE))

# Main function
def main():
    # Initialize screen
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake Game")

    # Initialize clock
    clock = pygame.time.Clock()

    # Create snake and food objects
    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -GRID_SIZE))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, GRID_SIZE))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-GRID_SIZE, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((GRID_SIZE, 0))

        # Move the snake
        snake.move(food)

        # Check for collision
        if snake.check_collision():
            pygame.quit()
            sys.exit()

        # Draw everything
        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    main()
