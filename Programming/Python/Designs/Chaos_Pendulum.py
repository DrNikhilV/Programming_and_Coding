import pygame
import math

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LENGTH1 = 150
LENGTH2 = 150
MASS1 = 20
MASS2 = 20

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chaos Pendulum")
clock = pygame.time.Clock()

# Convert degrees to radians
def to_radians(degrees):
    return degrees * math.pi / 180

# Draw the pendulum
def draw_pendulum(screen, theta1, theta2):
    x0, y0 = WIDTH // 2, HEIGHT // 4
    x1 = x0 + LENGTH1 * math.sin(theta1)
    y1 = y0 + LENGTH1 * math.cos(theta1)
    x2 = x1 + LENGTH2 * math.sin(theta2)
    y2 = y1 + LENGTH2 * math.cos(theta2)
    
    pygame.draw.line(screen, WHITE, (x0, y0), (x1, y1), 2)
    pygame.draw.circle(screen, RED, (int(x1), int(y1)), MASS1)
    pygame.draw.line(screen, WHITE, (x1, y1), (x2, y2), 2)
    pygame.draw.circle(screen, RED, (int(x2), int(y2)), MASS2)
    pygame.draw.line(screen, WHITE, (x1, y1), (x2, y2), 2)  # Draw a line from second ball

# Simulation loop
def main():
    theta1 = to_radians(120)
    theta2 = to_radians(160)
    omega1 = 0
    omega2 = 0
    dt = 0.01  # Decreased time step for faster simulation
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Calculate angular accelerations
        num1 = -9.8 * (2 * MASS1 + MASS2) * math.sin(theta1)
        num2 = - MASS2 * 9.8 * math.sin(theta1 - 2 * theta2)
        num3 = -2 * math.sin(theta1 - theta2) * MASS2 * (omega2 ** 2 * LENGTH2 + omega1 ** 2 * LENGTH1 * math.cos(theta1 - theta2))
        den = LENGTH1 * (2 * MASS1 + MASS2 - MASS2 * math.cos(2 * theta1 - 2 * theta2))
        alpha1 = (num1 + num2 + num3) / den
        
        num1 = 2 * math.sin(theta1 - theta2)
        num2 = (omega1 ** 2 * LENGTH1 * (MASS1 + MASS2))
        num3 = 9.8 * (MASS1 + MASS2) * math.cos(theta1)
        num4 = omega2 ** 2 * LENGTH2 * MASS2 * math.cos(theta1 - theta2)
        den = LENGTH2 * (2 * MASS1 + MASS2 - MASS2 * math.cos(2 * theta1 - 2 * theta2))
        alpha2 = (num1 * (num2 + num3 + num4)) / den
        
        # Update velocities and angles
        omega1 += alpha1 * dt
        omega2 += alpha2 * dt
        theta1 += omega1 * dt
        theta2 += omega2 * dt
        
        # Wrap angles to [-pi, pi]
        theta1 %= 2 * math.pi
        theta2 %= 2 * math.pi
        
        # Clear screen
        screen.fill(BLACK)
        
        # Draw pendulum
        draw_pendulum(screen, theta1, theta2)
        
        # Update display
        pygame.display.flip()
        clock.tick(120)  # Increased frame rate for smoother animation

    pygame.quit()

if __name__ == "__main__":
    main()
