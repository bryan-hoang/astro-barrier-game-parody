# -*- coding: utf-8 -*-

class target_sprites(arcade.Sprite):
    
    def _init_ (self):
        
        self.change_x
        
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1
            
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
            
    
        


