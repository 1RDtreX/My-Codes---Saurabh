import pygame
import random

# Initialize the game
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong Game by RDtreX")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red=(255, 0, 0)

# paddle properties
paddle_width, paddle_height = 10, 100
paddle_speed = 10

# my Ball properties
ball_radius = 10
ball_speed_x = 3
ball_speed_y = 3

# Player positions
player1_x, player1_y = 50, height // 2 - paddle_height // 2
player2_x, player2_y = width - 50, height // 2 - paddle_height // 2

# Ball position
ball_x, ball_y = width // 2, height // 2

# Score
player1_score = 0
player2_score = 0

# Game loop
running = True
while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= paddle_speed
    if keys[pygame.K_s] and player1_y < height - paddle_height:
        player1_y += paddle_speed
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_y < height - paddle_height:
        player2_y += paddle_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= height:
        ball_speed_y *= -1

    if (player1_x < ball_x < player1_x + paddle_width and
        player1_y < ball_y < player1_y + paddle_height) or \
       (player2_x < ball_x < player2_x + paddle_width and
        player2_y < ball_y < player2_y + paddle_height):
        ball_speed_x *= -1

    if ball_x - ball_radius <= 0:
        player2_score += 1
        ball_x, ball_y = width // 2, height // 2
        ball_speed_x *= random.choice([1, -1])
        ball_speed_y *= random.choice([1, -1])

    if ball_x + ball_radius >= width:
        player1_score += 1
        ball_x, ball_y = width // 2, height // 2
        ball_speed_x *= random.choice([1, -1])
        ball_speed_y *= random.choice([1, -1])

    pygame.draw.rect(screen, white, (player1_x, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (player2_x, player2_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)

    font = pygame.font.Font(None, 74)
    Aura = font.render(str("Aura"), 1, white)
    screen.blit(Aura, (250-140, 10))
    Aera = font.render(str("Aera"), 1, white)
    screen.blit(Aera, (510+50, 10))

    text = font.render(str(player1_score), 1, white)
    screen.blit(text, (250, 10))
    text = font.render(str(player2_score), 1, white)
    screen.blit(text, (510, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
