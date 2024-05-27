import pygame, sys, src.level as level
from src.sprites import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = game.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Age Of War - ish")
        self.clock = pygame.time.Clock()
        self.starting = True
        self.running = False
        self.game_over = False
        self.game_won = False
        self.game_won_image = pygame.image.load("Resources/game_won.png").convert_alpha()
        self.game_over_image = pygame.image.load("Resources/game_over.png").convert_alpha()

    def start_menu(self):
        font = pygame.font.SysFont(None, 100)
        easy = font.render("EASY", True, "white")
        normal = font.render("NORMAL", True, "white")
        hard = font.render("HARD", True, "white")
        impossible = font.render("IMPOSSIBLE", True, "white")
        normal_rect = normal.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        easy_rect = easy.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 100))
        hard_rect = hard.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 100))
        impossible_rect = impossible.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 200))
        while self.starting:
            m_pos = pygame.mouse.get_pos()
            self.screen.fill("#720E00")
            self.screen.blit(easy, easy_rect)
            self.screen.blit(normal, normal_rect)
            self.screen.blit(hard, hard_rect)
            self.screen.blit(impossible, impossible_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            if easy_rect.collidepoint(m_pos) and pygame.mouse.get_pressed()[0]:
                self.starting = False
                self.run("easy")
            if normal_rect.collidepoint(m_pos) and pygame.mouse.get_pressed()[0]:
                self.starting = False
                self.run("normal")
            if hard_rect.collidepoint(m_pos) and pygame.mouse.get_pressed()[0]:
                self.starting = False
                self.run("hard")
            if impossible_rect.collidepoint(m_pos) and pygame.mouse.get_pressed()[0]:
                self.starting = False
                self.run("impossible")


            pygame.display.update()

    def run(self, mode):
        self.level = level.Level()
        while True:
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            game_outcome = self.level.end_game()
            if game_outcome:
                self.end(game_outcome)
                break
            dt = self.clock.tick() / 1000
            self.level.run(dt, mode)
            pygame.display.update()

    def end(self, outcome):
        self.display_end_message(outcome)

    def display_end_message(self, outcome):
        image = self.game_won_image if outcome == "win" else self.game_over_image
        image_rect = image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        while True:
            self.screen.fill("#720E00")
            self.screen.blit(image, image_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.start_menu()
