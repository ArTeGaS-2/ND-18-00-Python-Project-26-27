import pygame
import sys
import random

# --- Налаштування ---
WIDTH, HEIGHT = 800, 600 # Ширина і висота
BG_COLOR = (20, 20, 20) # RGB колір фону
TEXT_COLOR = (255, 255, 255) # Колір тексту
FPS = 60 # Кадри на секунду

BUTTON_IMAGE_PATH = "button.png" # PNG зображення як кнопка
TEXT_TEMPLATE = "Кліків: {}" # Форматований рядок

def main():
    pygame.init() # Ініціалізація
    pygame.display.set_caption("Супер пупер мега клікер 1337 2026 ULTRA PRO") # Заголовок
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Встановлюємо ширину, висоту і потенційно інше
    clock = pygame.time.Clock() # екземпляр годинника

    # Шрифт
    font = pygame.font.SysFont("arial", 36) # Системний шрифт, його розмір

    # Завантаження зображення кнопки
    button_img = pygame.image.load(BUTTON_IMAGE_PATH).convert_alpha()
    # Зміна розміру
    button_img = pygame.transform.scale(button_img,(200, 200))
    # Розміщення
    button_rect = button_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # Завантаження зображення
    background_img = pygame.image.load("background.png").convert_alpha()
    # Зміна розміру
    background_img = pygame.transform.scale(background_img,(WIDTH, HEIGHT))
    # Розміщення
    background_rect = background_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    clicks = 0

    button_pos_x = random.randint(0, WIDTH)
    button_pos_y = random.randint(0, HEIGHT)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect.collidepoint(event.pos):
                    clicks += 1
                    button_pos_x = random.randint(0, WIDTH)
                    button_pos_y = random.randint(0, HEIGHT)
                    # Розміщення
                    button_rect = button_img.get_rect(
                        center=(button_pos_x, button_pos_y))
                else:
                    clicks -= 1

        screen.fill(BG_COLOR) # заливаємо фон

        screen.blit(background_img, background_rect) # Малюємо кнопку
        screen.blit(button_img, button_rect) # Малюємо кнопку

        # Формуємо текст лічильника
        text_str = TEXT_TEMPLATE.format(clicks)
        text_surf = font.render(text_str, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(midtop=(WIDTH // 2, 20))
        screen.blit(text_surf, text_rect)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()


