from main import GAME_HEIGHT, GAME_WIDTH
from globals import BLUE_BIRD_IMGS, GRAVITY, SPEED, HIT_BOXES, HIT_SOUND, DIE_SOUND, WING_SOUND
import pygame
import os
import random

class Bird:

    def __init__(self) -> None:
        self.x = GAME_WIDTH*0.1
        self.y = GAME_HEIGHT*0.6
        self.jumped = False
        self.jump_vel = 400
        self.movement = True
        self.controls = True
        self.sprites = [pygame.transform.scale_by(pygame.image.load(x), 1.5) for x in BLUE_BIRD_IMGS]
        self.frame = 0
        self.velocity = 0
        self.rect = pygame.Rect((self.x, self.y), (self.sprites[0].get_width(), self.sprites[0].get_height()))

    def draw(self, screen):
        if HIT_BOXES: pygame.draw.rect(screen, "green", self.rect, 2)
        self.sprites = [pygame.transform.rotate(pygame.transform.scale_by(pygame.image.load(x), 1.5), 20-self.velocity/10) for x in BLUE_BIRD_IMGS]
        if self.frame < 2.9: self.frame += 0.1
        else: self.frame = 0
        if int(self.frame) == 0: screen.blit(self.sprites[0], (self.x, self.y))
        if int(self.frame) == 1: screen.blit(self.sprites[1], (self.x, self.y))
        if int(self.frame) == 2: screen.blit(self.sprites[2], (self.x, self.y))

    def move(self, dt):
        if self.movement:
            self.y += self.velocity * dt + 0.5 * GRAVITY * dt**2
            self.velocity = self.velocity + GRAVITY * dt
            if self.velocity > 1000: self.velocity = 1000
            self.rect = pygame.Rect((self.x, self.y), (self.sprites[0].get_width(), self.sprites[0].get_height()))

    def jump(self):
        if self.movement and self.controls:
            self.velocity = -self.jump_vel
            WING_SOUND.play()

class Ground:

    def __init__(self, x) -> None:
        self.x = x
        self.y = GAME_HEIGHT * 0.9
        self.movement = True
        self.sprite = pygame.transform.scale_by(pygame.image.load(os.path.join(os.curdir, "imgs", "base.png")), 1.5)
        self.rect = pygame.Rect((self.x, self.y), (self.sprite.get_width(), self.sprite.get_height()))

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
        if HIT_BOXES: pygame.draw.rect(screen, "red", self.rect, 2)

    def move(self, dt):
        if self.movement:
            if self.x < -self.sprite.get_width(): self.x += 2*self.sprite.get_width()
            self.x -= SPEED * dt
            self.rect = pygame.Rect((self.x, self.y), (self.sprite.get_width(), self.sprite.get_height()))

    def collided(self, bird, grounds, pipes):
        if self.rect.colliderect(bird.rect):
            if bird.controls: HIT_SOUND.play()
            for ground in grounds: ground.movement = False
            for pipe in pipes: pipe.movement = False
            bird.movement = False
            bird.controls = False
            return True

class Pipes:

    def __init__(self) -> None:
        self.sprite_up = pygame.transform.rotate(pygame.transform.scale_by(pygame.image.load(os.path.join(os.curdir, "imgs", "pipe.png")), 1.5), 180)
        self.sprite_down = pygame.transform.scale_by(pygame.image.load(os.path.join(os.curdir, "imgs", "pipe.png")), 1.5)
        self.x = GAME_WIDTH
        self.y = random.randint(-self.sprite_up.get_height()+100, -100)
        self.distance = 150
        self.movement = True
        self.rect_up = pygame.Rect((self.x, self.y), (self.sprite_up.get_width(), self.sprite_up.get_height()))
        self.rect_down = pygame.Rect((self.x, self.y+self.sprite_up.get_height()+self.distance), (self.sprite_down.get_width(), self.sprite_down.get_height()))
        self.pointer = ScoreCollider(self.x + self.sprite_up.get_width() / 2, self.y + self.sprite_up.get_height())

    def draw(self, screen):
        screen.blit(self.sprite_up, (self.x, self.y))
        screen.blit(self.sprite_down, (self.x, self.y+self.sprite_up.get_height()+self.distance))

        self.pointer.draw(screen)

        if HIT_BOXES:
            pygame.draw.rect(screen, "red", self.rect_up, 2)
            pygame.draw.rect(screen, "red", self.rect_down, 2)

    def move(self, dt):
        if self.movement:
            if self.x < -self.sprite_up.get_width():
                self.x = GAME_WIDTH
                self.y = random.randint(-self.sprite_up.get_height()+100, -100)
                self.pointer.collided = False
            self.x -= SPEED * dt
            self.rect_up = pygame.Rect((self.x, self.y), (self.sprite_up.get_width(), self.sprite_up.get_height()))
            self.rect_down = pygame.Rect((self.x, self.y+self.sprite_up.get_height()+self.distance), (self.sprite_down.get_width(), self.sprite_down.get_height()))
            self.pointer.x, self.pointer.y = self.x + self.sprite_up.get_width() / 2, self.y + self.sprite_up.get_height()
            self.pointer.move()

    def collided(self, bird, grounds):
        if self.rect_up.colliderect(bird.rect) or self.rect_down.colliderect(bird.rect):
            if self.movement:
                HIT_SOUND.play()
                DIE_SOUND.play()
            self.movement = False
            bird.controls = False
            for ground in grounds: ground.movement = False
            return True
        
class ScoreCollider:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.collided = False

        self.rect = pygame.Rect((self.x, self.y), (10, 150))

    def draw(self, screen):
        if HIT_BOXES:
            pygame.draw.rect(screen, "orange", self.rect, 2)

    def move(self):
        self.rect = pygame.Rect((self.x, self.y), (25, 150))

    def collision(self, bird: Bird):
        return self.rect.colliderect(bird.rect)