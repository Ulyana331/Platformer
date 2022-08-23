import pygame
import os

import modules.sprites as sprites
win_height = 800
win_width = 800

class Enemy(sprites.Sprite):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.COUNT_MOVE = 0
        self.STEP = 1
        self.RANGE_MOVE = 320
         
    def gravity(self, list_rect):
        super().gravity("player/1.png",list_rect)     

    #
    def move_enemy(self, list_rect):
        # if self.COUNT_MOVE < self.RANGE_MOVE:
        self.DIRECTION = "R"
        if not self.CAN_MOVE_RIGHT:
            self.DIRECTION = 'R'
        if self.CAN_MOVE_RIGHT:
            
            self.X += self.STEP
            self.RECT.x = self.RECT.x + self.STEP
            self.animation(folder= "player",count_while=5,last_img= 11, first_img=5)
            # if self.CAN_MOVE_LEFT:                     
            #     # if self.DIRECTION == 'L':
            #     self.X -= self.STEP
            #     self.RECT.x -= 10
        if not self.CAN_MOVE_LEFT:
            self.DIRECTION = 'L'
        if self.CAN_MOVE_LEFT:
            
            self.X -= self.STEP
            self.RECT.x = self.RECT.x - self.STEP
            self.animation(folder= "player",count_while=5,last_img= 11, first_img=5)
        print(self.CAN_MOVE_LEFT)
        # else:
        #     self.COUNT_MOVE = 0
        #     if self.DIRECTION == "R":
        #         self.DIRECTION = "L"
        #     elif self.DIRECTION == "L":
        #         self.DIRECTION = "R"         
        self.COUNT_MOVE += 1
        self.animation(folder= "player",count_while= 5,last_img= 11, first_img=5)
#
enemy1 = Enemy(
    width = 50,
    height = 75,
    x = 0,
    y = 0,
    name_image = "images/robot/1.png",
    color= (255, 0, 0)
)