import pygame
from PIL import Image
from random import choice, randint

def extract_gif_frames(gif_path, size):
  frames = []
  gif = Image.open(gif_path)
  while True:
    frame = gif.copy()
    frame_pygame = pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode)
    frame_pygame = pygame.transform.scale(frame_pygame, size)  # Scale the frame
    frames.append(frame_pygame)
    try:
      gif.seek(gif.tell() + 1)
    except EOFError:
      break
  return frames

pygame.init()

screen_size = (1000, 1000)
screen = pygame.display.set_mode(screen_size)

gif_frames = extract_gif_frames('duck-hunt.gif', screen_size)
current_frame = 0
frame_rate = 60
frame_counter = 0

lanes = [100, 450, 800]

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
    # Initialize the player at a specific position with an image
    super(Player, self).__init__(250, 250, 'Mario.png')
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
    self.rect.x = max(0, min(self.rect.x, screen_size[0] - self.rect.width))
    self.rect.y = max(0, min(self.rect.y, screen_size[1] - self.rect.height))

  def reset(self):
    # Reset the player's position and target position
    self.x = 250
    self.y = 250
    self.dx = self.x
    self.dy = self.y
    self.rect.center = (self.x, self.y)
    self.resize_mario()

class Mushroom(GameObject):
  def __init__(self):
    x = choice(lanes)
    y = -64
    super(Mushroom, self).__init__(x, y, 'mushroom.png')
    self.direction = 1
    self.reset()

  def move(self):
    self.y += self.dy * self.direction
    if self.direction == 1 and self.y > 1000:
      self.reset()
    elif self.direction == -1 and self.y < -64:
      self.reset()
    self.rect.center = (self.x, self.y)

  def reset(self):
    self.x = choice(lanes)
    self.direction = 1 if self.y < 0 else -1
    self.y = -64 if self.direction == 1 else 1000
    self.dy = (randint(0, 200) / 100) + 1

class Princess(GameObject):
  def __init__(self):
    x = -64
    y = choice(lanes)
    super(Princess, self).__init__(x, y, 'princess.png')
    self.direction = 1
    self.reset()

  def move(self):
    self.x += self.dx * self.direction
    if self.direction == 1 and self.x > 1000:
      self.reset()
    elif self.direction == -1 and self.x < -64:
      self.reset()
    self.rect.center = (self.x, self.y)

  def reset(self):
    self.y = choice(lanes)
    self.direction = 1 if self.x < 0 else -1
    self.x = -64 if self.direction == 1 else 1000
    self.dx = (randint(0, 200) / 100) + 1

class Cloud(GameObject):
  def __init__(self):
    x = -64
    y = randint(0, screen_size[1])
    super(Cloud, self).__init__(x, y, 'clouds.png')
    self.dx = randint(1, 3)  # Horizontal speed of the cloud

  def move(self):
    self.x += self.dx  # Move the cloud horizontally
    if self.x > screen_size[0] + 64:
      self.reset()
    self.rect.x = self.x

  def reset(self):
    self.x = -64
    self.y = randint(0, screen_size[1])
    self.surf = pygame.image.load('clouds.png')
    self.rect = self.surf.get_rect(center=(self.x, self.y))


class Bowser(GameObject):
  def __init__(self):
    self.direction = choice(['up', 'down', 'left', 'right'])
    super(Bowser, self).__init__(0, 0, 'bowser.png')
    self.dx = (randint(0, 200) / 100) + 1
    self.dy = (randint(0, 200) / 100) + 1
    self.reset()

  # def resize_bomb(self):      
  #   new_size = (50, 50)
  #   self.surf = pygame.transform.scale(self.surf, new_size)
  #   self.rect = self.surf.get_rect(center=(self.x, self.y))

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
    return self.y < -64 or self.y > 1000 or self.x < -64 or self.x > 1000

  def random_position_offscreen(self):
    if self.direction == 'up':
      return choice(lanes), 1000
    elif self.direction == 'down':
      return choice(lanes), -64
    elif self.direction == 'left':
      return 1000, choice(lanes)
    else:
      return -64, choice(lanes)

  def reset(self):
    self.x, self.y = self.random_position_offscreen()
    self.direction = choice(['up', 'down', 'left', 'right'])
    # self.resize_bomb()

player = Player()
mushroom = Mushroom()
princess = Princess()
bowser = Bowser()
clouds = Cloud()

cloud_sprites = pygame.sprite.Group()
cloud_sprites.add(clouds)
all_sprites = pygame.sprite.Group(player, mushroom, princess, bowser)
ally_sprites = pygame.sprite.Group(mushroom, princess)
bowser_sprites = pygame.sprite.Group(bowser)

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

  # Background animation
  frame_counter += 1
  if frame_counter >= frame_rate:
    frame_counter = 0
    current_frame = (current_frame + 1) % len(gif_frames)
  screen.blit(gif_frames[current_frame], (0, 0))

  for cloud in cloud_sprites:
    cloud.move()
    cloud.render(screen)

  for entity in all_sprites:
    entity.move()

  for entity in all_sprites:
    entity.render(screen)

  fruit_hit = pygame.sprite.spritecollideany(player, ally_sprites)
  if fruit_hit:
    fruit_hit.reset()

  bomb_hit = pygame.sprite.spritecollideany(player, bowser_sprites)
  if bomb_hit:
    running = False

  pygame.display.flip()
  clock.tick(60)

pygame.quit()