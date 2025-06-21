import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #  Initialize clock
    clock = pygame.time.Clock()
    dt = 0

    # instantiate a Player object
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    Player.draw(player, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        player.update(dt)

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

        


if __name__ == "__main__":
    main()
