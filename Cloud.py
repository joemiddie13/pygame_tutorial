from GameObject import GameObject
from constants import SCREEN_SIZE
from random import randint

class Cloud(GameObject):
  def __init__(self):
    x = -64
    y = randint(0, SCREEN_SIZE[1])
    super(Cloud, self).__init__(x, y, 'images/clouds.png')
    self.dx = randint(1, 3)

  def move(self):
    # Move the cloud horizontally
    self.x += self.dx
    # If the cloud moves off-screen to the right, reset it
    if self.x > SCREEN_SIZE[0] + 64:
        self.reset()
    # Update the position of the cloud's rect
    self.rect.x = self.x
    self.rect.y = self.y

  def reset(self):
    # Reset the cloud's position off-screen to the left and at a random height
    self.x = -64
    self.y = randint(0, SCREEN_SIZE[1])
    self.rect = self.surf.get_rect(center=(self.x, self.y))