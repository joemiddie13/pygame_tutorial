import pygame
from random import randint
import random

# Initialize Pygame
pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Define the GameObject class
class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.rect = self.surf.get_rect(topleft=(x, y))

    def render(self, screen):
        screen.blit(self.surf, self.rect)

# Subclass GameObject for Apple that falls
class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, 0, 'apple.png')
        self.dy = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.rect.y += self.dy
        # Check the y position of the apple
        if self.rect.y > 500: 
            self.reset()

    # Reset the apple to the top of the screen at a random x position
    def reset(self):
        # self.rect.x = randint(50, 400)
        # self.rect.y = -64
        lanes = [93, 218, 343]
        self.rect.x = random.choice(lanes)
        self.rect.y = -64

class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, 0, 'strawberry.png')
        self.dx = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.rect.x += self.dx
        # Check the y position of the apple
        if self.rect.x > 500: 
            self.reset()

    # Reset the apple to the top of the screen at a random x position
    def reset(self):
        self.rect.x = -64
        self.rect.y = randint(0, 436)

# Get the clock
clock = pygame.time.Clock()

# Make an instance of Apple
apple = Apple()
strawberry = Strawberry()

# Create the game loop
running = True
while running:
    # Looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update the apple's position
    apple.move()
    strawberry.move()

    # Clear screen
    screen.fill((0, 0, 0))
    
    # Render the apple
    apple.render(screen)
    strawberry.render(screen)
    
    # Update the window
    pygame.display.flip()
    
    # tick the clock!
    clock.tick(60)

pygame.quit()
