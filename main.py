"""
Space Invaders Clone
Author: Brian Horner
_____________________________
Tutorial from: TechWithTim
Link: https://www.youtube.com/watch?v=Q-__8Xw9KTM
_____________________________
Edit History:
6/1/2022 - Initial Version
6/1/2022 - Set up imports, and loaded assets
6/1/2022 - Added basic run loop, background and player lives/level labels
6/1/2022 - Added ship parent class. Added enemy ship and player ship child
classes
6/1/2022 - Added player movement and movement wrapping
"""

# imports
import pygame
import os
import time
import random

# Initializing font
pygame.font.init()

# Constants
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders Clone")
FPS = 60

# --- Loading Asset Images ---
# Enemy Ships & Lasers
RED_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
BLUE_SHIP = pygame.image.load(
    os.path.join("assets", "pixel_ship_blue_small.png"))
GREEN_SHIP = pygame.image.load(
    os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))

# Player Ship & Laser
PLAYER_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))
PLAYER_LASER = pygame.image.load(
    os.path.join("assets", "pixel_laser_yellow.png"))

# Background
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets",
                                                                   "background_black.png")),
                                    (WIDTH, HEIGHT))


class Ship:
    # Constructor
    def __init__(self, x_pos, y_pos, health=100, width=50, height=50):
        self.x = x_pos
        self.y = y_pos
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
        self.height = height
        self.width = width

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, self.width,
                                               self.height), 0)

    # Get Methods

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height


def main():
    run = True
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 33)

    player_velocity = 5
    ship = Ship(300, 650)


    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BACKGROUND, (0, 0))

        # draw text
        lives_label = main_font.render(f"Lives: {lives}", True, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", True, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        ship.draw(window=WIN)
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:  # up -- GOOD
            ship.y -= player_velocity
            if ship.getY() + (ship.height) < 0:
                ship.y = HEIGHT
        if keys[pygame.K_s]:  # down
            ship.y += player_velocity
            if ship.getY() - (ship.height) > HEIGHT:
                ship.y = 0
        if keys[pygame.K_a]:  # left -- GOOD
            ship.x -= player_velocity
            if ship.getX() + (ship.width) < 0:
                ship.x = WIDTH
        if keys[pygame.K_d]:  # right
            ship.x += player_velocity
            if ship.getX() - (ship.width) > WIDTH:
                ship.x = 0


main()
