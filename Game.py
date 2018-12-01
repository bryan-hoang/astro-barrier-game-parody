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
SPRITE_SCALING_BULLET = 0.8
TARGET_COUNT = 1

class gameState(Enum):
    MAIN_MENU = 0
    PLAYING = 1
    GAME_OVER = 2

class AstroBarrier(arcade.Window):
    def __init__(self):
        # initialize window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, title="Club Penguin - Astro Barrier")

        self.player = None
        self.target_sprites = None
        self.bullet_sprites = None
        self.shoot = None
        # use Bryan's code for setting up window
        arcade.set_background_color(arcade.color.LIGHT_GREEN)

    def setup(self):

        self.level = 1

        self.player = arcade.SpriteList()
        self.target_sprites = arcade.SpriteList()
        self.bullet_sprites = arcade.SpriteList()
        self.shoot = False
        # use more of Bryan's code #hypercarry

        self.player_sprite = arcade.Sprite(
            "textures/Astro_Barrier_Ship_pin.png", SPRITE_SCALING_SHIP)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 40
        self.player.append(self.player_sprite)

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

   # initialize a shit ton of variables

        def on_key_press(self, symbol, modifiers):
            # check for user input
            if symbol == arcade.key.SPACE:
                self.shoot = True

            if symbol == arcade.key.RIGHT:
                self.moveRight = True

            if symbol == arcade.key.LEFT:
                self.moveLeft = True

    # Draw the sprites
    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.

        self.player.draw()
        self.target_sprites.draw()
        self.bullet_sprites.draw()

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10,
                         20, arcade.color.WHITE, 14)
        arcade.draw_text(f"Level: {self.level}", 10,
                         40, arcade.color.WHITE, 14)

    def on_update(self, delta_time):
        """ Movement and game logic """

        for bullet in self.bullet_sprites:
            hit_list = arcade.check_for_collision_with_list(
                bullet, self.target_sprites)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.kill()

            # For every coin we hit, add to the score and remove the coin
            for target in hit_list:
                target.hit()

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.kill()
                
            # Call update on everything
            self.bullet_sprites.update()
            self.target_sprites.update()
            self.player.update()


def main():
    """ Main method """
    game = AstroBarrier()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
