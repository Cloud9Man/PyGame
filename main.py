import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

keys = pygame.key.get_pressed()

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_ESCAPE):
                pygame.quit()

    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()