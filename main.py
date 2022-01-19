import pygame
import math
import random

pygame.init()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Estimating Pi")

R = HEIGHT/2
WHITE = (255, 255, 255)

pause = False

FPS = 60

total_dots = 0
dots_in = 0

PI = 0

text_surface = pygame.font.Font(None, 32).render("π: 0", True, (10, 10, 10))


def draw_random_dot(surface):
    global total_dots
    global dots_in
    global PI
    global text_surface

    random_x = (random.random() - 1 / 2) * 2 * R
    random_y = (random.random() - 1 / 2) * 2 * R
    pygame.draw.circle(surface, (1, 1, 1), (random_x + WIDTH/2, random_y + HEIGHT/2), 2)

    if (random_y**2) + (random_x**2) <= R**2:
        dots_in += 1
    total_dots += 1

    PI = (dots_in / total_dots) * 4
    text_surface = pygame.font.Font(None, 32).render(f"π: {round(PI, 5)}", True, (10, 10, 10))


def main():
    global pause

    running = True
    pause = False

    dot_surface = pygame.Surface((WIDTH, HEIGHT))
    dot_surface.set_colorkey((0, 0, 0))

    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pause = not pause

        if not pause:
            WIN.fill(WHITE)
            square = pygame.Rect((WIDTH / 2 - R, 0), (R * 2, R * 2))
            pygame.draw.rect(WIN, (200, 200, 200), square)
            pygame.draw.circle(WIN, (100, 100, 100), (WIDTH / 2, HEIGHT / 2), R)

            draw_random_dot(dot_surface)
            WIN.blit(dot_surface, (0, 0))

            WIN.blit(text_surface, (10, 10))
            pygame.display.update()


main()