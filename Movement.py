# -*- coding: utf-8 -*-

import arcade

SCREEN_WIDTH = NONE
SCREEN_HEIGHT = NONE

BULLET_SPEED = 5

class shape(arcade.Sprite):
    
    def _init_ (self):
        
        self.change_x
        
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1
            
class bullet(arcade.Sprite):
    
    def _init_ (self):
        
        self.bullet_list = None
        
    def update(self, delta_time):
        
        self.bullet_list.update
        
            hit_list = arcade.check_for_collision_with_list(bullet, self.shape_list)
            
            if len(hit_list) > 0:
                bullet.kill()
                
            if bullet.bottom > SCREEN_HEIGHT:
                bullet:kill()
                
    def on_space_bar_press (self, x, y, button, modifiers):
        
        bullet.angle = 90
        
        bullet.change_y = BULLET_SPEED
        
        bullet.center_x = self.player_sprite.center_x
        bullet.bottom = self.player_sprite.top
        
            
            
class player(arcade.Sprite):
    
    def _init_(self):
        
        self.change_x
        
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1
