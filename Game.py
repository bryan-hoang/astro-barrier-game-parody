# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 12:15:14 2018

@author: Liam
"""

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SPRITE_SCALING_SHIP = 0.05
SPRITE_SCALING_TARGET = 0.8
SPRITE_SCALING_BULLET = 0.8
TARGET_COUNT = 1


class AstroBarrier(arcade.Window):
    def __init__(self):
        # initialize window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, title="Club Penguin - Astro Barrier")

        self.player = None
        self.target_sprites = None
        self.bullet_sprites = None

        self.score = 0

        # use Bryan's code for setting up window
        arcade.set_background_color(arcade.color.LIGHT_GREEN)

    def setup(self):

        # Set up the player and levels
        self.score = 0
        self.level = 1

        self.player = arcade.SpriteList()
        self.target_sprites = arcade.SpriteList()
        self.bullet_sprites = arcade.SpriteList()

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

        # Load sounds. Sounds from kenney.nl
        self.gun_sound = arcade.sound.load_sound("sounds/laser1.wav")
        self.hit_sound = arcade.sound.load_sound("sounds/phaseJump1.wav")

        # Set the background color
        arcade.set_background_color(arcade.color.LIGHT_GREEN)

        # TODO: Eden's code for initializing player
        # self.player = Player()

    # initialize a shit ton of variables

        def on_key_press(self, symbol, modifiers):
            # check for user input
            if symbol == arcade.key.SPACE:
                self.shoot = True
                # Gunshot sound

            if symbol == arcade.key.RIGHT:
                self.moveRight = True

            if symbol == arcade.key.LEFT:
                self.moveLeft = True

        def on_update(self):
            # updates game state based on vars above
            if self.shoot:
                self.player.shoot()

                arcade.sound.play_sound(self.gun_sound)
                # Create a bullet
                # bullet = arcade.Sprite("images/laserBlue01.png", SPRITE_SCALING_LASER)

                # arcade.play_sound(SOUNDS['shoot']) optional if want sounds
                self.shoot = False

            for bullet in self.bullet_sprites:
                # kill bullets not on screen or if impacted with target
                if bullet.bottom >= self.height or bullet.collide:
                    bullet.kill()

            for target in self.target_sprites:
                if target.collide:
                    target.scored()

            # if player.holster == 0:
            #     self.state = gameState.GAME_OVER

            self.bullet_sprites.update()
            self.target_sprites.update()
            self.player.update()

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

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on bullet sprites
        self.bullet_sprites.update()

        # Loop through each bullet
        for bullet in self.bullet_sprites:

            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(
                bullet, self.target_sprites)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.kill()

            # For every coin we hit, add to the score and remove the coin
            for target in hit_list:
                target.kill()

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.kill()


def main():
    """ Main method """
    game = AstroBarrier()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
