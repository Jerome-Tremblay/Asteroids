import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from entities.logger import log_state
from entities.logger import log_event
from entities.player import Player
from entities.asteroid import Asteroid
from entities.asteroidfield import AsteroidField
from entities.shot import Shot
from ui import UI

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

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    game_ui = UI()
    
    while True:
        log_state()
        screen.fill("black")
        for entity in drawable:
            entity.draw(screen)
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
