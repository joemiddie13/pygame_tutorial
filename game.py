# Challenge 1

# # Import and initialize pygame
# import pygame 
# pygame.init()

# # Configure the screen
# screen = pygame.display.set_mode([500, 500])

# # Create the game loop
# running = True
# while running:
#     # Looks at events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Clear the screen
#     screen.fill((0, 0, 0))
    
#     # Define the colors
#     red = (255, 0, 0)
#     orange = (255, 165, 0)
#     yellow = (255, 255, 0)
#     green = (0, 255, 0)
#     blue = (0, 0, 255)
    
#     # Draw the circles
#     pygame.draw.circle(screen, red, (100, 100), 50)   # Top-left circle
#     pygame.draw.circle(screen, orange, (300, 100), 50) # Top-right circle
#     pygame.draw.circle(screen, yellow, (200, 200), 50)  # Middle circle
#     pygame.draw.circle(screen, green, (100, 300), 50)   # Bottom-left circle
#     pygame.draw.circle(screen, blue, (300, 300), 50)    # Bottom-right circle
    
#     # Update the display
#     pygame.display.flip()

    
# Challenge 2

import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((500, 500))

# Define colors
dark_gray = (50, 50, 50)

# Starting positions for the first circle
start_x = 50  # adjust as necessary
start_y = 50  # adjust as necessary
offset = 100  # distance between the centers of the circles
radius = 50   # radius of circles

# Create the game loop
running = True 
while running: 
    # Looks at events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill((0, 0, 0))
    
    # Draw the circles in a grid pattern using a single loop
    for i in range(9):
        # Calculate row number (by dividing i by 3 and rounding down)
        row = i // 3
        # Calculate column number (remainder of i divided by 3)
        col = i % 3
        
        # Calculate position for each circle
        position = (start_x + col * offset, start_y + row * offset)
        pygame.draw.circle(screen, dark_gray, position, radius)
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
