import pygame

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Platformer")


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 60)  # Player size
        self.vel_y = 0
        self.speed = 5
        self.jump_power = -15
        self.on_ground = False
        self.jump_count = 0 #track jumps

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = self.jump_power  # Jump
            self.jump_count += 1 #increment jump count

    def apply_gravity(self):
        self.vel_y += 1  # Gravity effect
        self.rect.y += self.vel_y
        if self.rect.y > HEIGHT - 60:  # Stop at the bottom
            self.rect.y = HEIGHT - 60
            self.vel_y = 0
            self.on_ground = True
        else:
            self.on_ground = False

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 0, 100), self.rect)  # Red player


class Platform:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 0, 200), self.rect)  # Green platform


# Create player and platforms
player = Player(100, HEIGHT - 100)
platforms = [
    Platform(150, 500, 150, 20),
    Platform(300, 400, 150, 20),
    Platform(450, 300, 150, 20),
]

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(30)  # 30 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)
    player.apply_gravity()

    # Platform collision
    for platform in platforms:
        if player.rect.colliderect(platform.rect) and player.vel_y > 0:
            player.rect.bottom = platform.rect.top
            player.vel_y = 0
            player.on_ground = True

    # Drawing everything
    screen.fill((135, 206, 235))  # Background color
    player.draw(screen)
    for platform in platforms:
        platform.draw(screen)

    pygame.display.flip()

pygame.quit()