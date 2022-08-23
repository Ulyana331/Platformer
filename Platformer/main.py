# 1. Імпортувати модуль pygame
import pygame 
# 2. Імпортувати модуль os
import os 
# 3. Імпортувати модуль random
import random 
#
import modules.area as area
import modules.settings as settings
import modules.sprites as sprites
import modules.enemy as enemy
# 4. Ініціалізувати налаштування pygame
pygame.init()

win_height = 800
win_width = 800
  
# 8.Cтворюємо ігровое вікно з ім'ям win 
win = pygame.display.set_mode((win_width,win_height))
# 9. Задаємо назву ігрового вікна
pygame.display.set_caption("GAME")
# 10. Створюємо основну функцію гри run_game:
def run_game():
    
    clock = pygame.time.Clock()
    
    # - задаємо змінну game, що відповідає за роботу циклу   
    game = True
    print(area.list_create_area)
    # - задаємо ігровий цикл while, 
    while game:
    # - задаємо умову закриття ігрового вікна,
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
    # - задаємо фон ігрового вікна (мотод fill)
        win.fill((128,0,255))
    # - задіємо об'єкт sprite і викликаємо його метод blit_sprite(), малюємо зображення на ігровому вікні, в центрі екрану
        for el in area.list_create_area:
            pygame.draw.rect(win, el.COLOR, el.RECT)
        #
        sprites.sprite.draw_rect(win)
        enemy.enemy1.draw_rect(win)
        #
        sprites.sprite.blit_sprite(win)
        enemy.enemy1.blit_sprite(win)
        #
        sprites.sprite.can_move_right(area.list_rect)
        sprites.sprite.can_move_left(area.list_rect)
        # sprites.sprite.can_move_up(area.list_rect)
        enemy.enemy1.can_move_right(area.list_rect)
        enemy.enemy1.can_move_left(area.list_rect)
        #
        sprites.sprite.move_sprite()
        enemy.enemy1.move_enemy(area.list_rect)
        #
        sprites.sprite.jump(area.list_rect)
        #
        sprites.sprite.gravity(list_rect= area.list_rect)
        enemy.enemy1.gravity(list_rect= area.list_rect)
        
        # if area.area.RECT.colliderect(sprite.RECT):
        #     print('Hello')
    # - задаємо оновлення ігрового екрану
        clock.tick(60)
        pygame.display.flip()
# 11. І найголовніше – викликаємо основну функцію гри
run_game()