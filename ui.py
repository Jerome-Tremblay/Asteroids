import pygame

class UI:
    def __init__(self, font_name = "Arial", size=32):
        self.font = pygame.font.SysFont(font_name, size)
        self.score = 0

    def draw_score(self, screen):
        score_surface = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_surface, (20, 20))

    def update_score(self, points):
        self.score += points