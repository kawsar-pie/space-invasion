import pygame
import random

# Initialize Pygame and set up the window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Shooting Game")

# Load and set up the player and enemy sprites
player_image = pygame.image.load("img/ship.bmp")
player_rect = player_image.get_rect()
player_rect.center = (400, 500)

enemy_image = pygame.image.load("img/alien.bmp")
enemy_rect = enemy_image.get_rect()

# Set up the player's bullets
bullet_image = pygame.image.load("img/bullet.ico")
bullet_rect = bullet_image.get_rect()
bullets = []

# Set up the game clock
clock = pygame.time.Clock()

# Set up game variables
score = 0
game_over = False

# Main game loop
while not game_over:
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        # Fire a bullet when the space bar is pressed
        bullet_rect.center = player_rect.center
        bullets.append(bullet_rect)

  # Update the player's position
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    player_rect.x -= 5
  if keys[pygame.K_RIGHT]:
    player_rect.x += 5

  # Update the enemy's position
  enemy_rect.y += 5
  if enemy_rect.y > 600:
    # If the enemy goes off the bottom of the screen, reset its position
    enemy_rect.y = 0
    enemy_rect.x = random.randint(0, 800)

  # Update the bullets
  for bullet in bullets:
    bullet.y -= 10
    if bullet.y < 0:
      # If the bullet goes off the top of the screen, remove it
      bullets.remove(bullet)

  # Check for collisions
  if enemy_rect.colliderect(player_rect):
    # If the player and enemy collide, the game is over
    game_over = True
  for bullet in bullets:
    if enemy_rect.colliderect(bullet):
      # If a bullet hits the enemy, increase the score and reset the enemy's position
      score += 1
      enemy_rect.y = 0
      enemy_rect.x = random.randint(0, 800)
      bullets.remove(bullet)

  # Draw the screen
  screen.fill((230, 230, 230))
  screen.blit(player_image, player_rect)
  screen.blit(enemy_image, enemy_rect)
  for bullet in bullets:
    screen.blit(bullet_image, bullet)
  pygame.display.flip()

  # Limit the frame rate to 60 FPS
  clock.tick(60)
