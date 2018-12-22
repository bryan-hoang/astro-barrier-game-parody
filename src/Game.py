# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 12:15:14 2018
@author: Liam, Bryan, Eden
"""

import arcade
from enum import Enum
from Target import Target
# import numpy as np

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SPRITE_SCALING_SHIP = 0.05
SPRITE_SCALING_TARGET = 0.8
SPRITE_SCALING_BULLET = 0.2

TARGET_COUNT = 4

MOVEMENT_SPEED = 8
BULLET_SPEED = 20


class gameState(Enum):
    MAIN_MENU = 0
    PLAYING = 1
    SUCCESS = 2
    GAME_OVER = 3


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
        self.holster = None

        self.player_sprite = None
        self.level = 1

        self.target_sprites = None
        self.bullet_sprites = None
        self.red_targets = None
        self.shoot = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False

        self.state = gameState.MAIN_MENU
        self.total_time = 11.0

        # use Bryan's code for setting up window
        arcade.set_background_color(arcade.color.DARK_GREEN)

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.target_sprites = arcade.SpriteList()
        self.bullet_sprites = arcade.SpriteList()
        self.red_targets = arcade.SpriteList()
        self.shoot = False
        self.holster = 10 + self.level
        # use more of Bryan's code #hypercarry

        self.state = gameState.MAIN_MENU
        self.total_time = 11.0

        self.player_sprite = Player(
            "textures/Astro_Barrier_Ship_pin.png", SPRITE_SCALING_SHIP)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 40
        self.player_list.append(self.player_sprite)

        # Create the targets
        for i in range(TARGET_COUNT + self.level - 1):

            # Create the targets instance
            # targets image from kenney.nl
            target = Target(SPRITE_SCALING_TARGET, 400, 280+i*80)
            target.set_texture(0)
            # Create alternating velocities
            if (i + 1) % 2 == 0:
                target.change_x = -5
            else:
                target.change_x = 5

            # Add the targets to the lists
            self.target_sprites.append(target)

        # Set the background color
        arcade.set_background_color(arcade.color.DARK_GREEN)

    def draw_main_menu(self):
        """
        Draw a main menu.
        """
        output = "Main Menu"
        arcade.draw_text(output, 240, 400, arcade.color.WHITE, 54)

        output = "Press space to start"
        arcade.draw_text(output, 285, 300, arcade.color.WHITE, 24)

    def draw_game(self):
        """
        Draw all the sprites.
        """
        point_list = ((0, 280), (800, 280),
                      (0, 360), (800, 360),
                      (0, 440), (800, 440),
                      (0, 520), (800, 520)
                      )
        arcade.draw_lines(point_list, arcade.color.BLUE, 10)

        # Draw all the sprites.
        self.player_list.draw()
        self.target_sprites.draw()
        self.bullet_sprites.draw()
        self.red_targets.draw()

        # Render the text
        arcade.draw_text(f"Bullet Count: {self.holster}", 650,
                         575, arcade.color.WHITE, 14)
        arcade.draw_text("Press Left and Right to move\n"
                         "Press Space to shoot",
                         10, 575, arcade.color.WHITE, 14)

        # Calculate seconds by using a modulus (remainder)
        seconds = int(self.total_time) % 60

        # Figure out our output
        output = f"Time: {seconds:02d} s"

        # Output the timer text.
        arcade.draw_text(output, 350, 575, arcade.color.WHITE, 14)

    def draw_success(self):
        """
        Draw "Success" across the screen.
        """
        output = "Success"
        arcade.draw_text(output, 280, 400, arcade.color.WHITE, 54)

        output = "Press space to play again"
        arcade.draw_text(output, 225, 300, arcade.color.WHITE, 24)

    def draw_game_over(self):
        """
        Draw "Game Over" across the screen.
        """
        output = "Game Over"
        arcade.draw_text(output, 240, 400, arcade.color.WHITE, 54)

        output = "Press space to restart"
        arcade.draw_text(output, 265, 300, arcade.color.WHITE, 24)

    # Draw the sprites
    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        if self.state == gameState.MAIN_MENU:
            self.draw_main_menu()

        elif self.state == gameState.PLAYING:
            self.draw_game()

        elif self.state == gameState.SUCCESS:
            self.draw_game()
            self.draw_success()
        else:
            self.draw_game()
            self.draw_game_over()

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
                target.set_texture(1)
                self.red_targets.append(target)

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.kill()

            if len(arcade.check_for_collision_with_list(
                    bullet, self.red_targets)) > 0:
                bullet.kill()

            # Call update on everything
        self.target_sprites.update()

        if len(self.red_targets) == 4:
            self.state = gameState.SUCCESS

        elif self.total_time > 1 and self.holster > 0 and \
                (self.state == gameState.PLAYING):
            self.total_time -= delta_time
        elif self.total_time <= 1 or self.holster <= 0:
            self.state = gameState.GAME_OVER
            self.total_time = 0
            self.holster = 0

    # initialize a shit ton of variables

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if self.state == gameState.MAIN_MENU:
            self.setup()
            self.state = gameState.PLAYING
        elif self.state == gameState.PLAYING:
            if key == arcade.key.SPACE:
                # Create a bullet
                self.holster -= 1
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
        elif self.state == gameState.SUCCESS:
            self.state = gameState.MAIN_MENU
            self.setup()
        elif self.state == gameState.GAME_OVER:
            self.state = gameState.MAIN_MENU
            self.setup()

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
