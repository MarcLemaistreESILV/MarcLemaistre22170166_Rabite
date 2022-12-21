import species
import shape
import time
import pygame

def plot(screen_size_x, screen_size_y, parameters):
    #main function
    pygame.init()  
    clock = pygame.time.Clock()
    running = True
    screen = pygame.display.set_mode((screen_size_x, screen_size_y))
    pygame.display.set_caption("Desktop background featuring evolutive AI simulation")
    icon = pygame.image.load('../evolutive_ai/sources/icone.ico')
    pygame.display.set_icon(icon)
    while running:  
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                running = False
        clock.tick(50)
        pygame.display.flip()  
    pygame.quit()
