import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("spacebar was pressed")
            if event.key == pygame.K_q:
                done = True

pygame.quit()