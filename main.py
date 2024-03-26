import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
n = 0
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("Image/Dalle1.jpg")
pygame.display.set_icon(icon)
target_img = pygame.image.load("Image/klipartz.com.png")
target_width = 80
target_height = 80

font_size = 30  # Размер шрифта для отображения счета
font = pygame.font.Font(None, font_size)  # Создание объекта Font

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                n += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    screen.blit(target_img, (target_x, target_y))

    text = font.render(f'Счет: {n}', True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, 50)
    screen.blit(text, text_rect)

    pygame.display.update()

pygame.quit()
