import pygame
from random import randint, choice
import random

pygame.init()

screen = pygame.display.set_mode([500, 500])

lanes = [93, 218, 343]

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
        self.rect.x += (self.dx - self.rect.x) * 0.1
        self.rect.y += (self.dy - self.rect.y) * 0.1

    def reset(self):
        self.dx = lanes[self.current_h_lane]
        self.dy = lanes[self.current_v_lane]
        self.rect.center = (self.dx, self.dy)

    def update_dx_dy(self):
        self.dx = lanes[self.current_h_lane]
        self.dy = lanes[self.current_v_lane]

class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, 0, 'apple.png')
        self.direction = 1
        self.reset()

    def move(self):
        self.rect.y += self.dy * self.direction
        if self.direction == 1 and self.rect.y > 500:
            self.reset()
        elif self.direction == -1 and self.rect.y < -64:
            self.reset()

    def reset(self):
        self.rect.x = choice(lanes)
        if random.choice([True, False]):
            self.direction = 1
            self.rect.y = -64
        else:
            self.direction = -1
            self.rect.y = 500
        self.dy = (randint(0, 200) / 100) + 1


class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, 0, 'strawberry.png')
        self.direction = 1
        self.reset()

    def move(self):
        self.rect.x += self.dx * self.direction
        if self.direction == 1 and self.rect.x > 500:
            self.reset()
        elif self.direction == -1 and self.rect.x < -64:
            self.reset()

    def reset(self):
        self.rect.y = choice(lanes)
        if random.choice([True, False]):
            self.direction = 1
            self.rect.x = -64
        else:
            self.direction = -1
            self.rect.x = 500
        self.dx = (randint(0, 200) / 100) + 1

# class Bomb(GameObject):
#     def __init__(self):
#         super(Bomb, self).__init__(0, 0, 'bomb.png')
#         self.direction = random.choice(['up', 'down', 'left', 'right'])
#         self.reset()
    
#     def resize_bomb(self):
#       new_size = (50, 50)
#       self.surf = pygame.transform.scale(self.surf, new_size)
#       self.rect = self.surf.get_rect(center=self.rect.center)

#     def move(self):
#       if self.direction == 'up':
#           self.rect.y -= self.dy
#           if self.rect.y < -64:
#               self.reset()
#       elif self.direction == 'down':
#           self.rect.y += self.dy
#           if self.rect.y > 500:
#               self.reset()
#       elif self.direction == 'left':
#           self.rect.x -= self.dx
#           if self.rect.x < -64:
#               self.reset()
#       elif self.direction == 'right':
#           self.rect.x += self.dx
#           if self.rect.x > 500:
#               self.reset()

#     def reset(self):
#       self.rect.x = choice(lanes) if self.direction in ['up', 'down'] else -64 if self.direction == 'left' else 500
#       self.rect.y = choice(lanes) if self.direction in ['left', 'right'] else -64 if self.direction == 'up' else 500
#       self.direction = random.choice(['up', 'down', 'left', 'right'])
#       self.dx = (randint(0, 200) / 100) + 1
#       self.dy = (randint(0, 200) / 100) + 1

player = Player()
apple = Apple()
strawberry = Strawberry()
bomb = Bomb()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(bomb)

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

    pygame.display.flip()

    clock.tick(60)

pygame.quit()