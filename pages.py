import pygame
import math
import os
from globals import BG, GROUND_SPRITE, MAINMENU, GAMEOVER, GAME_HEIGHT, GAME_WIDTH, FPS, WHITE, POINT_SOUND
from classes import Ground, Bird, Pipes
from score import HighScore


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
        self.time += 2 * dt
        mainmenu = pygame.transform.scale_by(MAINMENU, math.sin(self.time) * 0.1 + 1.5)
        self.screen.blit(BG, (0, 0))
        self.screen.blit(GROUND_SPRITE, (0, GAME_HEIGHT * 0.9))
        self.screen.blit(mainmenu, (GAME_WIDTH / 2 - mainmenu.get_width() / 2, GAME_HEIGHT / 2  - mainmenu.get_height() / 2))


class Gameplay(Page):
    def __init__(self, game) -> None:
        super().__init__(game)

        self.birds = [Bird()]
        self.grounds = [Ground(0), Ground(pygame.transform.scale_by(pygame.image.load(os.path.join(os.curdir, "imgs", "base.png")), 1.5).get_width())]
        self.pipes = [Pipes()]

        self.score_obj = HighScore.retrieve("score.pkl")
        self.score = 0

        if self.score_obj:
            self.highscore = self.score_obj.highscore
        else: self.highscore = 0

        self.canPlayAgain = False

        self.time = 1

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.switch_page(MainMenu)
                elif event.key == pygame.K_SPACE and self.canPlayAgain:
                    self.game.switch_page(Gameplay)


    def update(self) -> None:
        super().update()
        self.dt = self.game.clock.tick(FPS)/1000

        for bird in self.birds:
            bird.move(self.dt)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and not bird.jumped and bird.controls:
                bird.jumped = True
                bird.jump()
            elif not keys[pygame.K_SPACE]: bird.jumped = False
        for ground in self.grounds:
            ground.move(self.dt)
            for bird in self.birds:
                if ground.collided(bird, self.grounds, self.pipes):
                    self.canPlayAgain = True
        for pipe in self.pipes:
            pipe.move(self.dt)
            for bird in self.birds:
                pipe.collided(bird, self.grounds)
                
                if pipe.pointer.collision(bird) and not pipe.pointer.collided:
                    pipe.pointer.collided = True
                    self.score += 1
                    POINT_SOUND.play()

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

        if self.canPlayAgain:
            text = self.game.font.render(f"Highscore: {self.highscore}", True, WHITE)
            text2 = self.game.font.render(f"Your score: {self.score}", True, WHITE)
            text2_rect = text2.get_rect(center=(GAME_WIDTH/2, GAME_HEIGHT * 0.2))
            self.screen.blit(text2, text2_rect)
            text_rect = text.get_rect(center=(GAME_WIDTH/2, GAME_HEIGHT * 0.1))
            self.screen.blit(text, text_rect)

            gameover = pygame.transform.scale_by(GAMEOVER, math.sin(self.time) * 0.1 + 1.5)
            self.time += 2 * self.dt

            self.screen.blit(gameover, (GAME_WIDTH / 2 - gameover.get_width() / 2, GAME_HEIGHT / 2 - gameover.get_height() / 2))

            if not self.score_obj:
                self.score_obj = HighScore()

            self.score_obj.update(self.score)
            self.score_obj.store()

        else:
            text = self.game.font.render(f"{self.score}", True, WHITE)
            text_rect = text.get_rect(center=(GAME_WIDTH/2, GAME_HEIGHT * 0.1))
            self.screen.blit(text, text_rect)

    def run(self):
        self.handle_events()
        self.update()
        self.render(self.birds, self.grounds, self.pipes)
        pygame.display.flip()

    
