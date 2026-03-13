import pygame
import sys
from constants import *
from entities.logger import log_state
from entities.logger import log_event
from entities.player import Player
from entities.asteroid import Asteroid
from entities.asteroidfield import AsteroidField
from entities.shot import Shot
from ui import *

def main():
    print("Starting Asteroids with pygame version: VERSION")
    print(
        f"Screen width: {SCREEN_WIDTH}"
        f"Screen height: {SCREEN_HEIGHT}"
    )
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    player = Player(GAME_WIDTH / 2, GAME_HEIGHT / 2)
    asteroid_field = AsteroidField()
    game_ui = UI()

    current_state = GameState.MENU

    def reset_game():
            for sprite in updatable:
                sprite.kill()
            new_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            AsteroidField()
            game_ui.reset_score()
            return new_player, GameState.PLAYING
    
    while True:
        if current_state == GameState.MENU:
            screen.fill("black")

            title_font = pygame.font.SysFont("Arial", 80)
            start_font = pygame.font.SysFont("Arial", 40)
            title_surf = title_font.render("ASTEROIDS", True, "white")
            instruction_surf = start_font.render("Press SPACE to Start", True, "green")

            screen.blit(title_surf, (SCREEN_WIDTH // 2 - title_surf.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
            screen.blit(instruction_surf, (SCREEN_WIDTH // 2 - instruction_surf.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player, current_state = reset_game()

        elif current_state == GameState.PLAYING:
            log_state()
            screen.fill("black")
            for entity in drawable:
                entity.draw(screen)
            
            pygame.draw.rect(screen, "black", (GAME_WIDTH, 0, SCREEN_WIDTH - GAME_WIDTH, SCREEN_HEIGHT))        
            pygame.draw.line(screen, "white", (GAME_WIDTH, 0), (GAME_WIDTH, SCREEN_HEIGHT), 2)
            game_ui.draw_score(screen)
            game_ui.draw_signature(screen)
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   return
            updatable.update(dt)
            
            for asteroid in asteroids:
               if asteroid.collides_with(player):
                    print("Game over!")
                    current_state = GameState.GAME_OVER
            
            for asteroid in asteroids:
              for shot in shots:
                  if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    game_ui.update_score(1)
        
        elif current_state == GameState.GAME_OVER:
            screen.fill("black")

            font = pygame.font.SysFont("Arial", 64)
            game_over_surf = font.render("GAME OVER", True, "red")
            restart_surf = font.render("Press 'R' to Restart", True, "white")

            game_over_x = (SCREEN_WIDTH // 2) - (game_over_surf.get_width() // 2)
            restart_x = (SCREEN_WIDTH // 2) - (restart_surf.get_width() // 2)

            screen.blit(game_over_surf, (game_over_x, SCREEN_HEIGHT // 2 - 50))
            screen.blit(restart_surf, (restart_x, SCREEN_HEIGHT // 2 + 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        player, current_state = reset_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.display.flip()            
        dt = Clock.tick(60) / 1000

if __name__ == "__main__":
    main()
