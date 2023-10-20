import pygame
import sys

# Iniciar el juego
pygame.init()

# Constantes
WIDTH, HEIGHT = 800, 600
MENU_FONT = pygame.font.Font(None, 36)
MENU_COLOR = (255, 255, 255)
BUTTON_COLOR = (0, 128, 255)
BUTTON_HOVER_COLOR = (0, 100, 200)

# La pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

# Texto en pantalla
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Botones del menu
def create_button(text, x, y, width, height):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, (x, y, width, height))
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, (x, y, width, height))

    draw_text(text, MENU_FONT, MENU_COLOR, x + width // 2, y + height // 2)
    return False

# Main menu loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    if create_button("Start Game", 300, 200, 200, 50):
        # Start your game here (replace this line)
        print("Starting the game!")

    if create_button("Options", 300, 300, 200, 50):
        # Add code to handle options (replace this line)
        print("Opening options menu!")

    if create_button("Quit", 300, 400, 200, 50):
        running = False

    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
