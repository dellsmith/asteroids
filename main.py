import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    Shot.containers = (shots_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group,)
    AsteroidField()

    Player.containers = (updatable_group, drawable_group)

    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
    
    dt = 0      
    
    while True:      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

        updatable_group.update(dt)

        for asteroid in asteroid_group:
            if asteroid.collides_with(player):
                raise SystemExit("Game over!")
            
            for shot in shots_group:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()


        screen.fill("black")
        
        for obj in drawable_group:
            obj.draw(screen)

        pygame.display.flip()


        
        

if __name__ == "__main__":
    main()