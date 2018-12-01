# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 12:15:14 2018
@author: Liam
"""

import arcade
from enum import Enum

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SPRITE_SCALING_SHIP = 0.05
SPRITE_SCALING_TARGET = 0.8
SPRITE_SCALING_BULLET = 0.2

TARGET_COUNT = 1

MOVEMENT_SPEED = 8
BULLET_SPEED = 20


class gameState(Enum):
    MAIN_MENU = 0
    PLAYING = 1
    GAME_OVER = 2


class Player(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1


class AstroBarrier(arcade.Window):
    def __init__(self):

        # Call the parent class initializer
        super().__init__(
            SCREEN_WIDTH, SCREEN_HEIGHT, "Club Penguin - Astro Barrier")

        self.player_list = None

        self.player_sprite = None
        self.level = 1

        self.target_sprites = None
        self.bullet_sprites = None
        self.red_targets = None
        self.shoot = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False

        # use Bryan's code for setting up window
        arcade.set_background_color(arcade.color.LIGHT_GREEN)

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.target_sprites = arcade.SpriteList()
        self.bullet_sprites = arcade.SpriteList()
        self.red_targets = arcade.SpriteList()
        self.shoot = False
        # use more of Bryan's code #hypercarry

        self.level = 1

        self.player_sprite = Player(
            "textures/Astro_Barrier_Ship_pin.png", SPRITE_SCALING_SHIP)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 40
        self.player_list.append(self.player_sprite)

        # Create the targets
        for i in range(TARGET_COUNT):

            # Create the targets instance
            # targets image from kenney.nl
            target = arcade.Sprite(
                "textures/Astro_Barrier_Target.png", SPRITE_SCALING_TARGET)

            # Position the targets
            target.center_x = 400
            target.center_y = 300

            # Add the targets to the lists
            self.target_sprites.append(target)

        # Set the background color
        arcade.set_background_color(arcade.color.LIGHT_GREEN)

        # TODO: Eden's code for initializing player
        # self.player = Player()

    # Draw the sprites
    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.

        self.player_list.draw()
        self.target_sprites.draw()
        self.bullet_sprites.draw()

        # Render the text
        arcade.draw_text(f"Level: {self.level}", 10,
                         20, arcade.color.WHITE, 14)

    def update(self, delta_time):
        """ Movement and game logic """

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED

        # Call update on player
        self.player_list.update()

        # Call update on bullet sprites
        self.bullet_sprites.update()

        for bullet in self.bullet_sprites:
            hit_list = arcade.check_for_collision_with_list(
                bullet, self.target_sprites)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.kill()

            # For every target we hit, remove and add to red list
            for target in hit_list:
                self.target_sprites.remove(target)
                target.load_texture(
                    "Red_Target.png", target.center_x, target.center_y,
                    target.width, target.height)
                self.red_targets.append(target)

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.kill()

            if len(arcade.check_for_collision_with_list(
                    bullet, self.red_targets)) > 0:
                bullet.kill()

            # Call update on everything
        self.target_sprites.update()

    # initialize a shit ton of variables
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.SPACE:
            # Create a bullet
            bullet = arcade.Sprite(
                "textures/Bullet.png", SPRITE_SCALING_BULLET)

            # Give the bullet a speed
            bullet.change_y = BULLET_SPEED

            # Position the bullet
            bullet.center_x = self.player_sprite.center_x
            bullet.bottom = self.player_sprite.top

            # Add the bullet to the appropriate lists
            self.bullet_sprites.append(bullet)

        if key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False


def main():
    """ Main method """
    game = AstroBarrier()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
