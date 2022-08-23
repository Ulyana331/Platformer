import pygame
import os
import modules.settings as settings

win_height = 800
win_width = 800

area_w = 100
area_h = 75

list_area = [
    "000000001",
    "000000001",
    "000010111",
    "110000011",
    "111000001",
    "000001001",
    "000101111",
    "110000001",
    "000110001",
    "000000011",
    "111111111"
]
list_create_area = []
list_rect = []
class Area(settings.Settings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # def draw_rect(self, win, rect):
    #     pygame.draw.rect(win, self.COLOR, rect)

def create_area(level):
    x = 0
    y = 0
    for string in list_area:
        for el in string:
            if el == "1":
                area = Area(
                    x= x,
                    y= y,
                    width= area_w,
                    height= area_h,
                    color= (255, 165, 0)
                )
                list_create_area.append(area)
                list_rect.append(area.RECT)

            x += area_w
        x = 0
        y += area_h

create_area(list_area)





      

