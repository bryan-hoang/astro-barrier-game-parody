# -*- coding: utf-8 -*-

class target_sprites(arcade.Sprite):
    
    def _init_ (target_sprites):
        
    def update(target_sprites)
        
    target_sprites.change_x = TARGET_SPEED
    
    def move(target_sprites, change_x: float):
        
        for sprite in target_sprites.sprite_list:
            sprite.center_x += change_x

    def on_draw(delta_time):
        
        arcade.start_render()
    
        arcade.draw_rectangle_filled(on_draw.center_x, on_draw.center_y,
                                     RECT_WIDTH, RECT_HEIGHT,
                                     arcade.color.ALIZARIN_CRIMSON)

        on_draw.center_x += on_draw.delta_x * delta_time
        on_draw.center_y += on_draw.delta_y * delta_time

        if on_draw.center_x < RECT_WIDTH // 2 \
                or on_draw.center_x > SCREEN_WIDTH - RECT_WIDTH // 2:
            on_draw.delta_x *= -1

    on_draw.center_x = 100
    on_draw.delta_x = 115
        
    def main():

        arcade.schedule(on_draw, 1 / 80)
    
        arcade.run()
        
        if target_sprites.left < 0:
            target_sprites.left = 0
        elif target_sprites.right > SCREEN_WIDTH - 1:
            target_sprites.right = SCREEN_WIDTH - 1
            
class bullet_sprites(arcade.Sprite):
    
    def _init_ (self):
        
        self.bullet_sprites = None
                
    def on_space_bar_press (self, x, y, button, modifiers):
        
        bullet_sprites.angle = 90
        
        bullet_sprites.change_y = BULLET_SPEED
        
        bullet_sprites.center_x = self.player_sprite.center_x
        bullet_sprites.bottom = self.player_sprite.top
            
class player(arcade.Sprite):
    
    def _init_(self):
        
        self.change_x
        
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1
            
    
        


