import os
import sys
import pygame
from constants import *

def show_game_over():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font_large = pygame.font.SysFont("Arial", 72)
    font_small = pygame.font.SysFont("Arial", 36)
    game_over_text = font_large.render("GAME OVER", True, RED)
    prompt_text = font_small.render("Press any key to restart", True, WHITE)

    # Center the text on the screen
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    prompt_rect = prompt_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                os.execl(sys.executable, sys.executable, *sys.argv)  # Exit game over screen on key press

        # Fill the screen with a background color
        screen.fill(BLACK)
        # Draw the texts
        screen.blit(game_over_text, game_over_rect)
        screen.blit(prompt_text, prompt_rect)
        # Update the display
        pygame.display.flip()