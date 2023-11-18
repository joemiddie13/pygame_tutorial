import pygame
from GameObject import GameObject
from constants import LANES, SCREEN_SIZE
from random import choice, randint

class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(250, 250, 'images/Mario.png')
    self.dx = self.x
    self.dy = self.y
    self.speed = 20
    self.smoothness = 0.1
    self.resize_mario()

  def resize_mario(self):
    new_size = (100, 100)
    self.surf = pygame.transform.scale(self.surf, new_size)
    self.rect = self.surf.get_rect(center=(self.x, self.y))
  
  def left(self):
    self.dx -= self.speed

  def right(self):
    self.dx += self.speed

  def up(self):
    self.dy -= self.speed

  def down(self):
    self.dy += self.speed

  def move(self):
    # Gradually move towards the target position for smooth floating effect
    self.x += (self.dx - self.x) * self.smoothness
    self.y += (self.dy - self.y) * self.smoothness

    # Update the rect position based on the new position
    self.rect.x = self.x
    self.rect.y = self.y

    # Ensure the player doesn't move off the screen
    self.rect.x = max(0, min(self.rect.x, SCREEN_SIZE[0] - self.rect.width))
    self.rect.y = max(0, min(self.rect.y, SCREEN_SIZE[1] - self.rect.height))

  def reset(self):
    # Reset the player's position and target position
    self.x = 250
    self.y = 250
    self.dx = self.x
    self.dy = self.y
    self.rect.center = (self.x, self.y)
    self.resize_mario()