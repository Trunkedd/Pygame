import pygame as pg
from sprites import *
pg.init() # starter pygame modul


BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
 
screen = pg.display.set_mode((800,600)) # lager spill vindu, 800x600
 
clock = pg.time.Clock()


player = Player()

 

all_sprites = pg.sprite.Group()
all_sprites.add(player)


pos_x = 100
pos_y = 100
size_x = 50
size_y = 50
box_1_dir = 5
 

 
i = 0
playing = True
while playing: # game loop

    clock.tick(120)
    #print("FPS: ", i)
    i += 1
    for event in pg.event.get():
        if event.type == pg.QUIT: # hvis vi trykker på krysset i spillvinduet
            playing = False
            pg.quit()
 
    if len(all_sprites)<1:
        new_player = Player()
        all_sprites.add(new_player)

    all_sprites.update()
 
    screen.fill(WHITE)
    all_sprites.draw(screen)
    

    pg.display.update()