# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 12:15:14 2018

@author: Liam
"""

import arcade

class Game(arcade.Window):
    """
    Bryan's Code for window
    """
    
    def on_key_press(self, symbol, modifiers):
        #check for user input
        if symbol == arcade.key.SPACE:
            self.shoot = True
            
        if symbol == arcade.key.RIGHT:
            self.moveRight = True
            
        if symbol == arcade.key.LEFT:
            self.moveLeft = True
            
    def on_update(self):
        #updates game state based on vars above
        if self.shoot:
            self.player.shoot()
            #arcade.play_sound(SOUNDS['shoot']) optional if want sounds
            self.shoot = False
            
        for bullet in self.bullet_sprites:
            #kill bullets not on screen or if impacted with target
            if bullet.bottom >= self.height or bullet.collide:
                bullet.kill()
                
        for target in self.target_sprites:
            if target.collide:
                target.scored()
                
        
        self.bullet_sprites.update()
        self.target_sprites.update()
        self.player.update()
        

                
            