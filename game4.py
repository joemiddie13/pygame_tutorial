import pygame

pygame.init()

screen = pygame.display.set_mode([500, 500])

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.rect = self.surf.get_rect(center=(x, y))

    def render(self, screen):
        screen.blit(self.surf, self.rect)

class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(250, 250, 'player.png')
        self.horizontal_lanes = [93, 218, 343]
        self.vertical_lanes = [93, 218, 343]
        self.current_h_lane = 1
        self.current_v_lane = 1
        self.dx = self.horizontal_lanes[self.current_h_lane]
        self.dy = self.vertical_lanes[self.current_v_lane]

    def left(self):
        if self.current_h_lane > 0:
            self.current_h_lane -= 1
            self.dx = self.horizontal_lanes[self.current_h_lane]

    def right(self):
        if self.current_h_lane < len(self.horizontal_lanes) - 1:
            self.current_h_lane += 1
            self.dx = self.horizontal_lanes[self.current_h_lane]

    def up(self):
        if self.current_v_lane > 0:
            self.current_v_lane -= 1
            self.dy = self.vertical_lanes[self.current_v_lane]

    def down(self):
        if self.current_v_lane < len(self.vertical_lanes) - 1:
            self.current_v_lane += 1
            self.dy = self.vertical_lanes[self.current_v_lane]

    def move(self):
        self.rect.x += (self.dx - self.rect.x) * 0.1
        self.rect.y += (self.dy - self.rect.y) * 0.1

player = Player()

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


    player.move()

    screen.fill((0, 0, 0))
    
    player.render(screen)
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()