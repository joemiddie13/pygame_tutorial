from GameObject import GameObject
from constants import LANES, SCREEN_SIZE
from random import choice, randint

class Mushroom(GameObject):
  def __init__(self):
    x = choice(LANES)
    y = -64
    super(Mushroom, self).__init__(x, y, 'images/mushroom.png')
    self.direction = 1
    self.reset()

  def move(self):
    self.y += self.dy * self.direction

    if self.direction == 1 and self.y > SCREEN_SIZE[1]:
        self.reset()
    elif self.direction == -1 and self.y < -64:
        self.reset()

    self.rect.center = (self.x, self.y)

  def reset(self):
    self.x = choice(LANES)
    self.direction = 1 if self.y < 0 else -1
    self.y = -64 if self.direction == 1 else SCREEN_SIZE[1]
    self.dy = (randint(0, 200) / 100) + 1
