# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 12:15:14 2018

@author: Liam
"""

import arcade

class Game(arcade.Window):
    def __init__(self,width,height):
        #initialize window
        super().__init__(width,height,title="Club Penguin")
        
        self.bullet_sprites = None
        self.target_sprites = None
        self.player = None
        #use Bryan's code for setting up window
        
    def setup(self):
        self.level = 1
        self.bullet_sprites = arcade.SpriteList()
        self.target_sprites = arcade.SpriteList()
        self.player = arcade.SpriteList()
        #use more of Bryan's code #hypercarry
        self.player = Player() #Eden's code for initializing player
        
   
   #initialize a shit ton of variables
        
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
            
            if player.holster == 0:
                self.state = gameState.GAME_OVER
                
                    
            
            self.bullet_sprites.update()
            self.target_sprites.update()
            self.player.update()
        

                
            