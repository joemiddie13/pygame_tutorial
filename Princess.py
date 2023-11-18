from GameObject import GameObject
from constants import LANES
from random import choice, randint

class Princess(GameObject):
  def __init__(self):
    x = -64
    y = choice(LANES)
    super(Princess, self).__init__(x, y, 'images/princess.png')
    self.direction = 1
    self.dx = randint(1, 3)
    self.reset()

  def move(self):
    self.x += self.dx * self.direction
    if self.x > 1000 + 64:
        self.reset()
    self.rect.x = self.x
    self.rect.y = self.y

  def reset(self):
    self.x = -64
    self.y = choice(LANES)
    self.rect = self.surf.get_rect(center=(self.x, self.y))