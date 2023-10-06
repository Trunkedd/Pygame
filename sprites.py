import pygame as pg
import random
player_image = pg.image.load("beter2.png")


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_image
        self.rect = self.image.get_rect()
        self.pos_x = (0,600)
        self.pos_y = random.randint(1,10)
    def update(self):
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y

        
        self.pos_x += self.speed

        if self.pos_x > 900:
            self.kill()
        keys = pg.key.get_pressed()
        if keys[pg.K_w]: # oppover
            pos_y -= 5
        if keys[pg.K_s]: # nedover
         pos_y += 5
        if keys[pg.K_a]: # venstre
            pos_x -= 5
        if keys[pg.K_d]: # høyre
            pos_x += 5 