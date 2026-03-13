import pygame
from constants import *

class UI:
    def __init__(self, font_name = "Arial", size=32):
        self.font = pygame.font.SysFont(font_name, size)
        self.score = 0

    def draw_score(self, screen):
        score_surface = self.font.render(f"Score: {self.score}", True, ("white"))
        sidebar_width = SCREEN_WIDTH - GAME_WIDTH
        center_x = GAME_WIDTH + (sidebar_width // 2)
        final_x = center_x - (score_surface.get_width() // 2)
        screen.blit(score_surface, (final_x, 20))

    def update_score(self, points):
        self.score += points