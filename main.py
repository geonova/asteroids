import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Shot.containers = (shots,updatable, drawable)

    Player.containers = (updatable, drawable)
    player_one = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #pygame.Surface.fill(screen,(0,0,0))
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_check(player_one):
                print("Game over!")
                return
            for bullet in shots:
                if asteroid.collision_check(bullet):
                    bullet.kill()
                    asteroid.split()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
