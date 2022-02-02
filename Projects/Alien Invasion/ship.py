import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """
    A class to manage the ship.
    """

    def __init__(self, game):
        """
        Initializes the ship and set its starting position
        :param game: current instance of the AlienInvasion class,
        give ship access to all the game resources defined in AlienInvasion class
        """
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.settings = game.settings

        # Load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")  # surface represents the ship
        self.rect = self.image.get_rect() # get attributes rect of surface

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom # get attribute midbottom of rect of surface

        # object rect only keep integers value => convert to float to keep accurately value
        self.x = float(self.rect.x)

        # flag moving
        self.moving_left = False
        self.moving_right = False

    def blitme(self):
        """
        Draw the ship at its current location.
        :return:
        """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """
        Update the ship's position based on the movement flag.
        Change from update ship's rect => update ship.x
        Update ship's rect from ship.x
        :return: None
        """
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def center_ship(self):
        """
        Center the ship on the screen.
        :return:
        """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
