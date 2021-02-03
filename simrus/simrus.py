import sys
import pygame


if __name__ == "__main__":
    print("Simrus 0.1.0")
    pygame.display.init()

    size = width, height = 1024, 768
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Simrus")

    keep_running = True
    while keep_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_running = False

    pygame.display.quit()
    sys.exit()
