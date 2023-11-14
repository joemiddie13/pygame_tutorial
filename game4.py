import pygame
from random import choice, randint

pygame.init()

screen = pygame.display.set_mode([500, 500])

lanes = [93, 218, 343]

class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image)
    self.x = x
    self.y = y
    self.rect = self.surf.get_rect(center=(self.x, self.y))

  def render(self, screen):
    screen.blit(self.surf, self.rect.topleft)

class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(250, 250, 'player.png')
    self.current_h_lane = 1
    self.current_v_lane = 1
    self.dx = lanes[self.current_h_lane]
    self.dy = lanes[self.current_v_lane]
    self.reset()

  def left(self):
    if self.current_h_lane > 0:
      self.current_h_lane -= 1
      self.update_dx_dy()

  def right(self):
    if self.current_h_lane < len(lanes) - 1:
      self.current_h_lane += 1
      self.update_dx_dy()

  def up(self):
    if self.current_v_lane > 0:
      self.current_v_lane -= 1
      self.update_dx_dy()

  def down(self):
    if self.current_v_lane < len(lanes) - 1:
      self.current_v_lane += 1
      self.update_dx_dy()

  def move(self):
    self.x += (self.dx - self.x) * 0.1
    self.y += (self.dy - self.y) * 0.1
    self.rect.center = (self.x, self.y)

  def reset(self):
    self.dx = lanes[self.current_h_lane]
    self.dy = lanes[self.current_v_lane]
    self.rect.center = (self.dx, self.dy)

  def update_dx_dy(self):
    self.dx = lanes[self.current_h_lane]
    self.dy = lanes[self.current_v_lane]

class Apple(GameObject):
  def __init__(self):
    x = choice(lanes)
    y = -64
    super(Apple, self).__init__(x, y, 'apple.png')
    self.direction = 1
    self.reset()

  def move(self):
    self.y += self.dy * self.direction
    if self.direction == 1 and self.y > 500:
      self.reset()
    elif self.direction == -1 and self.y < -64:
      self.reset()
    self.rect.center = (self.x, self.y)

  def reset(self):
    self.x = choice(lanes)
    self.direction = 1 if self.y < 0 else -1
    self.y = -64 if self.direction == 1 else 500
    self.dy = (randint(0, 200) / 100) + 1

class Strawberry(GameObject):
  def __init__(self):
    x = -64
    y = choice(lanes)
    super(Strawberry, self).__init__(x, y, 'strawberry.png')
    self.direction = 1
    self.reset()

  def move(self):
    self.x += self.dx * self.direction
    if self.direction == 1 and self.x > 500:
      self.reset()
    elif self.direction == -1 and self.x < -64:
      self.reset()
    self.rect.center = (self.x, self.y)

  def reset(self):
    self.y = choice(lanes)
    self.direction = 1 if self.x < 0 else -1
    self.x = -64 if self.direction == 1 else 500
    self.dx = (randint(0, 200) / 100) + 1

class Bomb(GameObject):
  def __init__(self):
    self.direction = choice(['up', 'down', 'left', 'right'])
    super(Bomb, self).__init__(0, 0, 'bomb.png')
    self.dx = (randint(0, 200) / 100) + 1
    self.dy = (randint(0, 200) / 100) + 1
    self.reset()

  def resize_bomb(self):
    new_size = (50, 50)
    self.surf = pygame.transform.scale(self.surf, new_size)
    self.rect = self.surf.get_rect(center=(self.x, self.y))

  def move(self):
    if self.direction == 'up':
      self.y -= self.dy
    elif self.direction == 'down':
      self.y += self.dy
    elif self.direction == 'left':
      self.x -= self.dx
    elif self.direction == 'right':
      self.x += self.dx
    self.rect.center = (self.x, self.y)
    if self.off_screen():
      self.reset()

  def off_screen(self):
    return self.y < -64 or self.y > 500 or self.x < -64 or self.x > 500

  def random_position_offscreen(self):
    if self.direction == 'up':
      return choice(lanes), 500
    elif self.direction == 'down':
      return choice(lanes), -64
    elif self.direction == 'left':
      return 500, choice(lanes)
    else:
      return -64, choice(lanes)

  def reset(self):
    self.x, self.y = self.random_position_offscreen()
    self.direction = choice(['up', 'down', 'left', 'right'])
    self.resize_bomb()

player = Player()
apple = Apple()
strawberry = Strawberry()
bomb = Bomb()

all_sprites = pygame.sprite.Group(player, apple, strawberry, bomb)
fruit_sprites = pygame.sprite.Group(apple, strawberry)
bomb_sprites = pygame.sprite.Group(bomb)

clock = pygame.time.Clock()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_LEFT:
        player.left()
      elif event.key == pygame.K_RIGHT:
        player.right()
      elif event.key == pygame.K_UP:
        player.up()
      elif event.key == pygame.K_DOWN:
        player.down()

  for entity in all_sprites:
    entity.move()

  screen.fill((0, 0, 0))

  for entity in all_sprites:
    entity.render(screen)

  fruit_hit = pygame.sprite.spritecollideany(player, fruit_sprites)
  if fruit_hit:
    fruit_hit.reset()

  bomb_hit = pygame.sprite.spritecollideany(player, bomb_sprites)
  if bomb_hit:
    running = False

  pygame.display.flip()
  clock.tick(60)

pygame.quit()
