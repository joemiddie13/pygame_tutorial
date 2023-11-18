from GameObject import GameObject
from constants import LANES, SCREEN_SIZE
from random import choice, randint
import pygame

class Bowser(GameObject):
  def __init__(self):
    self.direction = choice(['up', 'down', 'left', 'right'])
    # Call the superclass constructor with initial position and image
    super(Bowser, self).__init__(0, 0, 'images/bowser.png')
    # Set the movement speed
    self.dx = (randint(0, 200) / 100) + 1
    self.dy = (randint(0, 200) / 100) + 1
    self.reset()

  def move(self):
    if self.direction == 'up':
        self.y -= self.dy
    elif self.direction == 'down':
        self.y += self.dy
    elif self.direction == 'left':
        self.x -= self.dx
    elif self.direction == 'right':
        self.x += self.dx

    # Update Bowser's position
    self.rect.center = (self.x, self.y)
    
    # Reset Bowser if it moves off the screen
    if self.off_screen():
        self.reset()

  def off_screen(self):
    # Check if Bowser is off the screen
    return self.y < -64 or self.y > SCREEN_SIZE[1] or self.x < -64 or self.x > SCREEN_SIZE[0]

  def random_position_offscreen(self):
    # Choose a random off-screen position based on the current direction
    if self.direction == 'up':
        return choice(LANES), SCREEN_SIZE[1]
    elif self.direction == 'down':
        return choice(LANES), -64
    elif self.direction == 'left':
        return SCREEN_SIZE[0], choice(LANES)
    else:
        return -64, choice(LANES)

  def reset(self):
    self.x, self.y = self.random_position_offscreen()
    self.direction = choice(['up', 'down', 'left', 'right'])
