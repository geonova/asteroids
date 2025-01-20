import pygame
from constants import *
import player

def main():
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    player_one = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #pygame.Surface.fill(screen,(0,0,0))
        screen.fill("black")
        player_one.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
