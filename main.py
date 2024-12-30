import pygame
import os
from classes import *

pygame.init()
BG = pygame.transform.scale_by(pygame.image.load(os.path.join(os.curdir, "imgs", "bg.png")),1.5)
GAME_RES = (GAME_WIDTH, GAME_HEIGHT) = (BG.get_width(), BG.get_height())
FPS = 60

class App:
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode(GAME_RES)
        self.clock = pygame.time.Clock()

    def draw(self, birds, grounds, pipes):
        self.screen.fill("white")
        self.screen.blit(BG, (0, 0))
        for bird in birds:
            bird.draw(self.screen)
        for ground in grounds:
            ground.draw(self.screen)
        for pipe in pipes:
            pipe.draw(self.screen)
        pygame.display.flip()

    def run(self):
        running = True

        birds = [Bird()]
        grounds = [Ground(0), Ground(pygame.transform.scale_by(pygame.image.load(os.path.join(os.curdir, "imgs", "base.png")), 1.5).get_width())]
        pipes = [Pipes()]
        dt = 0

        while running:
            [exit() for event in pygame.event.get() if event.type == pygame.QUIT]
            self.draw(birds, grounds, pipes)
            for bird in birds:
                bird.move(dt)

                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE] and not bird.jumped and bird.controls:
                    bird.jumped = True
                    bird.jump()
                elif not keys[pygame.K_SPACE]: bird.jumped = False
            for ground in grounds:
                ground.move(dt)
                for bird in birds:
                    ground.collided(bird, grounds, pipes)
            for pipe in pipes:
                pipe.move(dt)
                for bird in birds:
                    pipe.collided(bird, grounds)
            dt = self.clock.tick(FPS)/1000



if __name__ == "__main__":
    APP = App()
    APP.run()