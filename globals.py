import pygame
import os

pygame.mixer.init()

BG = pygame.transform.scale_by(pygame.image.load(os.path.join(os.curdir, "imgs", "bg.png")),1.5)
GAME_RES = (GAME_WIDTH, GAME_HEIGHT) = (BG.get_width(), BG.get_height())
GROUND_SPRITE = pygame.transform.scale_by(pygame.image.load(os.path.join(os.curdir, "imgs", "base.png")), 1.5)
MAINMENU = pygame.transform.scale_by(pygame.image.load(os.path.join(os.curdir, "imgs", "message.png")), 1)
GAMEOVER = pygame.transform.scale_by(pygame.image.load(os.path.join(os.curdir, "imgs", "gameover.png")), 1)
FPS = 60

YELLOW_BIRD_IMGS = [os.path.join(os.curdir, "imgs", "yellowbird-upflap.png"), os.path.join(os.curdir, "imgs", "yellowbird-midflap.png"), os.path.join(os.curdir, "imgs", "yellowbird-downflap.png")]
BLUE_BIRD_IMGS = [os.path.join(os.curdir, "imgs", "bluebird-upflap.png"), os.path.join(os.curdir, "imgs", "bluebird-midflap.png"), os.path.join(os.curdir, "imgs", "bluebird-downflap.png")]
RED_BIRD_IMGS = [os.path.join(os.curdir, "imgs", "redbird-upflap.png"), os.path.join(os.curdir, "imgs", "redbird-midflap.png"), os.path.join(os.curdir, "imgs", "redbird-downflap.png")]
GRAVITY = 1000
SPEED = 200
HIT_BOXES = True

WHITE = (255, 255, 255)

DIE_SOUND = pygame.mixer.Sound(os.path.join(os.curdir, "audio", "die.wav"))
WING_SOUND = pygame.mixer.Sound(os.path.join(os.curdir, "audio", "wing.wav"))
SWOOSH_SOUND = pygame.mixer.Sound(os.path.join(os.curdir, "audio", "swoosh.wav"))
HIT_SOUND = pygame.mixer.Sound(os.path.join(os.curdir, "audio", "hit.wav"))
POINT_SOUND = pygame.mixer.Sound(os.path.join(os.curdir, "audio", "point.wav"))