import arcade

# arcade.window_commands.open_window(800, 600, 'Astro Barrier', False)
# arcade.set_background_color([20, 120, 25])
# arcade.start_render()
# arcade.finish_render()
# arcade.window_commands.run()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SPRITE_SCALING_SHIP = 0.05
SPRITE_SCALING_TARGET = 0.8
SPRITE_SCALING_BULLET = 0.8
TARGET_COUNT = 1

BULLET_SPEED = 5


class AstroBarrier(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Astro Barrier")

        # Variables that will hold sprite lists
        self.player_list = None
        self.target_list = None
        self.bullet_list = None

        arcade.set_background_color(arcade.color.LIGHT_GREEN)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.target_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Image from kenney.nl
        self.player_sprite = arcade.Sprite(
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
            self.target_list.append(target)

        # Set the background color
        arcade.set_background_color(arcade.color.LIGHT_GREEN)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.

        self.player_list.draw()
        self.target_list.draw()
        self.bullet_list.draw()

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on bullet sprites
        self.bullet_list.update()

        # Loop through each bullet
        for bullet in self.bullet_list:

            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(
                bullet, self.target_list)

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
