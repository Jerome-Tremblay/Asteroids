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
    
    while True:
        log_state()
        screen.fill("black")
        for entity in drawable:
            entity.draw(screen)
        pygame.draw.rect(screen, "black", (GAME_WIDTH, 0, SCREEN_WIDTH - GAME_WIDTH, SCREEN_HEIGHT))        
        pygame.draw.line(screen, "white", (GAME_WIDTH, 0), (GAME_WIDTH, SCREEN_HEIGHT), 2)
        game_ui.draw_score(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    game_ui.update_score(1)
        dt = Clock.tick(60) / 1000

if __name__ == "__main__":
    main()
