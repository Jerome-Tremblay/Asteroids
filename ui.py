import pygame
from constants import *

sidebar_width = SCREEN_WIDTH - GAME_WIDTH
center_x = GAME_WIDTH + (sidebar_width // 2)
class UI:
    def __init__(self):
        self.score_font = pygame.font.SysFont("Arial", 32)
        self.sig_font = pygame.font.SysFont("Arial", 12)
        self.score = 0
        self.high_score = 0


    def draw_score(self, screen):
        score_surface = self.score_font.render(f"Score: {self.score}", True, ("white"))
        final_x = center_x - (score_surface.get_width() // 2)
        screen.blit(score_surface, (final_x, 20))

        high_score_surf = self.score_font.render(f"Best: {self.high_score}", True, "gold")
        high_x = center_x - (high_score_surf.get_width() // 2)
        screen.blit(high_score_surf, (high_x, 60))

    def update_score(self, points):
        self.score += points
        if self.score > self.high_score:
            self.high_score = self.score

    def reset_score(self):
        self.score = 0

    def draw_signature(self, screen):
        sig_surface = self.sig_font.render(f"Made by Jerome Tremblay @ 2026", True, ("white"))
        sig_x = center_x - (sig_surface.get_width() // 2)
        sig_y = SCREEN_HEIGHT - sig_surface.get_height() - 20
        screen.blit(sig_surface, (sig_x, sig_y))