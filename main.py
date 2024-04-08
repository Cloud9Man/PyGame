import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_ESCAPE):
                pygame.quit()
            elif (event.key == pygame.K_1):
                print("Item 1 selected!")
            elif (event.key == pygame.K_2):
                print("Item 2 selected!")
            elif (event.key == pygame.K_3):
                print("Item 3 selected!")
            elif (event.key == pygame.K_4):
                print("Item 4 selected!")

    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt  

    pygame.display.flip()

    dt = clock.tick(60) / 1000
pygame.quit()