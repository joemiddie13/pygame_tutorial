import pygame

# Initialize Pygame
pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Define the GameObject class
class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.rect = self.surf.get_rect(center=(x, y))

    def render(self, screen):
        screen.blit(self.surf, self.rect)

# Calculate positions and create GameObjects
rows, cols = 3, 3
fruit_size = 64
x_spacing = (500 - (cols * fruit_size)) // (cols + 1)
y_spacing = (500 - (rows * fruit_size)) // (rows + 1)
fruit_types = ['apple.png', 'strawberry.png']

# Generate a list of fruit GameObjects in a grid
fruits = []
for row in range(rows):
    for col in range(cols):
        x = (col * fruit_size) + (x_spacing * (col + 1)) + (fruit_size // 2)
        y = (row * fruit_size) + (y_spacing * (row + 1)) + (fruit_size // 2)
        fruit_image = fruit_types[(row + col) % len(fruit_types)]
        fruits.append(GameObject(x, y, fruit_image))

# Create the game loop
running = True
while running:
    # Looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((0, 0, 0))

    # Render all fruits
    for fruit in fruits:
        fruit.render(screen)

    # Update the window
    pygame.display.flip()

pygame.quit()
