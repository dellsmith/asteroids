import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    
    while True:      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

        updatable_group.update(dt)

        screen.fill("black")
        
        for obj in drawable_group:
            obj.draw(screen)

        pygame.display.flip()


        
        

if __name__ == "__main__":
    main()