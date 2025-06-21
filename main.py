import sys
import pygame
from constants import *

from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Game state variables
    paused = False
    font = pygame.font.Font(None, 74)  # Font for pause text
    
    # Add groups to reduce complexity
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # instantiate the asteroid and shots models
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField() 

    # instantiate the player model
    Player.containers = (updatable, drawable)

    # instantiate a Player object
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
    dt = 0
    
    # infinite loop to keep screen up
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused  # Toggle pause state
        
        # Only update game logic if not paused
        if not paused:
            updatable.update(dt)

            # Collision logic
            for asteroid in asteroids: 
                if asteroid.collides_with(player):
                    print("Game over!")
                    sys.exit()

            # Bullet collision logic
            for shot in shots:
                for asteroid in asteroids:
                    if asteroid.collides_with(shot):
                        shot.kill()
                        asteroid.split()
                        break

        # Always draw the game (even when paused)
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        
        # Draw pause overlay if paused
        if paused:
            pause_text = font.render("PAUSED", True, "white")
            instruction_text = font.render("Press P to resume", True, "white")
            
            # Center the text on screen
            pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50))
            instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 50))
            
            screen.blit(pause_text, pause_rect)
            screen.blit(instruction_text, instruction_rect)
        
        pygame.display.flip()

        # Only advance time if not paused
        if not paused:
            dt = clock.tick(60) / 1000
        else:
            clock.tick(60)  # Still limit framerate but don't advance dt

if __name__ == "__main__":
    main()
