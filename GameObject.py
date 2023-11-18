import pygame

class GameObject(pygame.sprite.Sprite):
  """
  Represents a game object in the pygame tutorial.

  Attributes:
    x (int): The x-coordinate of the game object.
    y (int): The y-coordinate of the game object.
    image (str): The path to the image file for the game object.
    surf (pygame.Surface): The surface object representing the game object image.
    rect (pygame.Rect): The rectangle that encloses the game object image.
  """

  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image)
    self.x = x
    self.y = y
    self.rect = self.surf.get_rect(center=(self.x, self.y))

  def render(self, screen):
    """
    Renders the game object on the screen.

    Args:
      screen (pygame.Surface): The surface object representing the game screen.
    """
    screen.blit(self.surf, self.rect.topleft)
