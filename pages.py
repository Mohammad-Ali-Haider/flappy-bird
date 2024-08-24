import pygame
import math
import os
from globals import BG, GROUND_SPRITE, BIRD_SPRITE, GAME_HEIGHT, GAME_WIDTH, FPS
from classes import Ground, Bird, Pipes


class Page:
    def __init__(self, game) -> None:
        self.game = game
        self.screen = game.screen

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

    def update(self) -> None:
        pass

    def render(self) -> None:
        pass

    def run(self) -> None:
        self.handle_events()
        self.update()
        self.render()
        pygame.display.flip()


class MainMenu(Page):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.time = 0

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game.switch_page(Gameplay)


    def render(self) -> None:
        super().render()
        dt = self.game.clock.tick(FPS)/ 1000
        self.time += 15 * dt
        Bird = pygame.transform.scale_by(BIRD_SPRITE, math.sin(self.time) * 0.1 + 4)
        self.screen.blit(BG, (0, 0))
        self.screen.blit(GROUND_SPRITE, (0, GAME_HEIGHT * 0.9))
        self.screen.blit(Bird, (GAME_WIDTH / 2 - Bird.get_width() / 2, GAME_HEIGHT / 2  - Bird.get_height() / 2))


class Gameplay(Page):
    def __init__(self, game) -> None:
        super().__init__(game)

        self.birds = [Bird()]
        self.grounds = [Ground(0), Ground(pygame.transform.scale_by(pygame.image.load(os.path.join(os.curdir, "imgs", "base.png")), 1.5).get_width())]
        self.pipes = [Pipes()]

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.switch_page(MainMenu)


    def update(self) -> None:
        super().update()
        dt = self.game.clock.tick(FPS)/1000

        for bird in self.birds:
            bird.move(dt)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and not bird.jumped and bird.controls:
                bird.jumped = True
                bird.jump()
            elif not keys[pygame.K_SPACE]: bird.jumped = False
        for ground in self.grounds:
            ground.move()
            for bird in self.birds:
                ground.collided(bird, self.grounds)
        for pipe in self.pipes:
            pipe.move()
            for bird in self.birds:
                pipe.collided(bird, self.grounds)

    def render(self, birds, grounds, pipes) -> None:
        super().render()
        self.screen.fill("white")
        self.screen.blit(BG, (0, 0))
        for bird in birds:
            bird.draw(self.screen)
        for ground in grounds:
            ground.draw(self.screen)
        for pipe in pipes:
            pipe.draw(self.screen)

    def run(self):
        self.handle_events()
        self.update()
        self.render(self.birds, self.grounds, self.pipes)
        pygame.display.flip()

    
