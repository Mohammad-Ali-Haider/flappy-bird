import pygame
import os

BG = pygame.transform.scale_by(pygame.image.load(os.path.join(os.curdir, "imgs", "bg.png")),1.5)
GAME_RES = (GAME_WIDTH, GAME_HEIGHT) = (BG.get_width(), BG.get_height())
GROUND_SPRITE = pygame.transform.scale_by(pygame.image.load(os.path.join(os.curdir, "imgs", "base.png")), 1.5)
BIRD_SPRITE = pygame.transform.scale_by(pygame.image.load(os.path.join(os.curdir, "imgs", "bird1.png")), 1)
FPS = 60