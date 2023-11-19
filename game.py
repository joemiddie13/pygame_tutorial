import pygame
from PIL import Image
from random import choice, randint
from constants import SCREEN_SIZE, FRAME_RATE
from Player import Player
from Mushroom import Mushroom
from Princess import Princess
from Cloud import Cloud
from Bowser import Bowser

def extract_gif_frames(gif_path, size):
  """
  Extracts frames from a GIF file and returns a list of pygame surfaces.

  Parameters:
  - gif_path (str): The path to the GIF file.
  - size (tuple): The desired size of the frames.

  Returns:
  - frames (list): A list of pygame surfaces representing the frames of the GIF.
  """
  frames = []
  gif = Image.open(gif_path)
  while True:
    frame = gif.copy()
    frame_pygame = pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode)
    frame_pygame = pygame.transform.scale(frame_pygame, size)
    frames.append(frame_pygame)
    try:
      gif.seek(gif.tell() + 1)
    except EOFError:
      break
  return frames

def main():
  """
  The main function that runs the game loop.

  This function initializes the game, sets up the game window, creates game objects,
  handles user input, updates game state, and renders the game on the screen.

  Returns:
    None
  """
  pygame.init()
  pygame.mixer.init()
  screen = pygame.display.set_mode(SCREEN_SIZE)

  pygame.mixer.music.load('music&sounds/mario_music.mp3')
  pygame.mixer.music.play(-1)

  powerup_sound = pygame.mixer.Sound('music&sounds/powerup.wav')

  gif_frames = extract_gif_frames('images/duck-hunt.gif', SCREEN_SIZE)
  current_frame = 0
  frame_counter = 0

  player = Player()
  mushroom = Mushroom()
  princess = Princess()
  cloud = Cloud()
  bowser = Bowser()

  cloud_sprites = pygame.sprite.Group(cloud)
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

    frame_counter += 1
    if frame_counter >= FRAME_RATE:
      frame_counter = 0
      current_frame = (current_frame + 1) % len(gif_frames)
    screen.blit(gif_frames[current_frame], (0, 0))

    for cloud in cloud_sprites:
      cloud.move()
      cloud.render(screen)

    for entity in all_sprites:
      entity.move()
      entity.render(screen)

    fruit_hit = pygame.sprite.spritecollideany(player, ally_sprites)
    if fruit_hit:
      fruit_hit.reset()
      powerup_sound.play()

    bomb_hit = pygame.sprite.spritecollideany(player, bowser_sprites)
    if bomb_hit:
      running = False

    pygame.display.flip()
    clock.tick(FRAME_RATE)

  pygame.quit()

if __name__ == "__main__":
  main()