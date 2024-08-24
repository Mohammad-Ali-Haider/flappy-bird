import pygame
from globals import GAME_RES
from pages import MainMenu

class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Flappy Bird")
        self.screen = pygame.display.set_mode(GAME_RES)
        self.clock = pygame.time.Clock()

        self.running = True
        self.current_page = MainMenu(self)

    def switch_page(self, new_page):
        self.current_page = new_page(self)

    def run(self):
        while self.running:
            self.current_page.run()

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()