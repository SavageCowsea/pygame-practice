import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter Espacial")

# Colores
WHITE = (255, 255, 255)

# Cargar imágenes y ajustar su tamaño
player_img = pygame.transform.scale(pygame.image.load("player.png"), (20, 20))
enemy_img = pygame.transform.scale(pygame.image.load("enemy.png"), (20, 20))

# Tamaño de la nave y enemigo
player_size = 20
enemy_size = 20

# Posición inicial del jugador
player_x = (WIDTH - player_size) // 2
player_y = HEIGHT - player_size

# Velocidad del jugador
player_speed = 1

# Proyectiles del jugador
bullets = []
bullet_size = 20
bullet_speed = 2

# Enemigos
enemies = []
enemy_speed = 0.1

# Función para dibujar al jugador
def draw_player(x, y):
    screen.blit(player_img, (x, y))

# Función para dibujar un enemigo
def draw_enemy(x, y):
    screen.blit(enemy_img, (x, y))

# Función para dibujar un proyectil
def draw_bullet(x, y):
    pygame.draw.rect(screen, (255, 0, 0), (x, y, bullet_size, bullet_size))

# Bucle principal del juego
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Disparar proyectiles
    if keys[pygame.K_SPACE]:
        bullet_x = player_x + player_size / 2 - bullet_size / 2
        bullet_y = player_y
        bullets.append((bullet_x, bullet_y))

    # Crear enemigos aleatoriamente
    if len(enemies) < 5:
        enemy_x = random.randint(0, WIDTH - enemy_size)
        enemy_y = 0
        enemies.append((enemy_x, enemy_y))

    # Mover y dibujar proyectiles
    new_bullets = []
    for bullet in bullets:
        bullet_x, bullet_y = bullet
        draw_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_speed
        if bullet_y > 0:
            new_bullets.append((bullet_x, bullet_y))
    bullets = new_bullets

    # Mover y dibujar enemigos
    new_enemies = []
    for enemy in enemies:
        enemy_x, enemy_y = enemy
        draw_enemy(enemy_x, enemy_y)
        enemy_y += enemy_speed
        if enemy_y < HEIGHT:
            new_enemies.append((enemy_x, enemy_y))
    enemies = new_enemies

    # Detectar colisiones entre proyectiles y enemigos
    new_enemies = []
    for enemy in enemies:
        enemy_hit = False
        for bullet in bullets:
            if (
                enemy[0] < bullet[0] < enemy[0] + enemy_size
                and enemy[1] < bullet[1] < enemy[1] + enemy_size
            ):
                enemy_hit = True
                bullets.remove(bullet)
                break
        if not enemy_hit:
            new_enemies.append(enemy)
    enemies = new_enemies

    draw_player(player_x, player_y)
    pygame.display.update()

# Salir del juego
pygame.quit()
