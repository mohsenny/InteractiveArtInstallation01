# Advanced experimental Python script for a wild interactive art experience using Pygame

# Import necessary libraries
import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BG_COLOR = (20, 20, 20)  # Slightly dynamic background color

# Set up the drawing window (canvas)
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Particle class for dynamic effects
class Particle:
    def __init__(self, position):
        self.position = position
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.size = random.randint(2, 5)
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(1, 4)
        self.decay_rate = random.uniform(0.95, 0.98)
        self.expanding = random.choice([True, False])

    def update(self):
        self.position = (self.position[0] + math.cos(self.angle) * self.speed,
                         self.position[1] + math.sin(self.angle) * self.speed)

        if self.expanding and self.size < 10:
            self.size *= 1.05
        else:
            self.size *= self.decay_rate
            self.expanding = False

        # Color transition over time
        self.color = tuple(min(255, max(0, x + random.randint(-15, 15))) for x in self.color)

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.position[0]), int(self.position[1])), int(self.size))

# Function to change background color dynamically
def dynamic_background_color():
    return tuple(min(255, max(0, x + random.randint(-10, 10))) for x in BG_COLOR)

# Main loop
running = True
particles = []
while running:
    # Fill the background with a dynamic color
    screen.fill(dynamic_background_color())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type in [pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN]:
            for _ in range(30):  # More particles for a wilder effect
                particles.append(Particle(pygame.mouse.get_pos()))

        if event.type == pygame.KEYDOWN:
            for _ in range(150):  # Intense burst of particles on key press
                particles.append(Particle((random.randint(0, WIDTH), random.randint(0, HEIGHT))))

    # Update and draw particles
    for particle in particles[:]:
        particle.update()
        particle.draw()
        if particle.size < 0.2 or particle.size > 20:
            particles.remove(particle)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
