import pygame

SIZE_BLOCK = 20
FRAME_COLOR = (0, 255, 204)
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
size = [500, 600]
COUNT_BLOCKS = 20
MARGIN = 1

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Змейка")

while True:
    for event in pygame.event.get():
        try:
            if event.type == pygame.QUIT:
                pygame.quit()
        except Exception as ex:
            print(ex)

    screen.fill(FRAME_COLOR)

    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = WHITE
            pygame.draw.rect(screen, color, [10 + column * SIZE_BLOCK + MARGIN * (column + 1),
                                             20 + row * SIZE_BLOCK + MARGIN * (row + 1),
                                             SIZE_BLOCK,
                                             SIZE_BLOCK])

    pygame.display.flip()
