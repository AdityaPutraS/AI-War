import numpy as np
import math
import pyglet

maxMaju = 200
maxPutar = 180
maxKey = 60


class Pesawat:

    def __init__(self, titikTengah, arah,nomor):
        # Arah 0 derajat = menghadap timur
        self.titikTengah = titikTengah
        self.targetTengah = titikTengah
        self.arah = arah
        self.targetArah = arah
        im = pyglet.image.load('sprite/pesawat'+str(nomor)+'.png')
        self.sprite = pyglet.sprite.Sprite(im,x=titikTengah[0],y=titikTengah[1])
        self.sprite.image.anchor_x = self.sprite.image.width / 2
        self.sprite.image.anchor_y = self.sprite.image.height / 2
        self.hp = 100
        self.ammo = 1000
        self.vLurus = [0,0]
        self.vPutar = 0
        self.lagiGerak = False

    def update(self):
        x1,y1 = self.titikTengah
        x2,y2 = self.targetTengah
        self.lagiGerak = False
        if(abs(x2-x1)+abs(y2-y1) > 0.001):
            self.lagiGerak = True
            dx,dy = self.vLurus
            self.titikTengah = x1+dx, y1+dy

        if(abs(abs(self.targetArah)-abs(self.arah)) > 0.001):
            self.lagiGerak = True
            self.arah += self.vPutar
            if(self.arah > 0):
                self.arah = self.arah % 360
            else:
                self.arah = -abs(self.arah)%360

        x,y = self.titikTengah
        self.updateSprite(x=x,y=y,rot=-self.arah)

    def putar(self, deg):
        if(not(self.lagiGerak)):
            self.lagiGerak = True
            self.targetArah = self.arah + deg
            self.vPutar = deg/((abs(deg)//maxPutar+1)*maxKey)
        else:
            print('Lagi Gerak')

    def maju(self, jarak):
        if(not(self.lagiGerak)):
            self.lagiGerak = True
            movVector = [jarak*math.cos(np.deg2rad(self.arah)),jarak*math.sin(np.deg2rad(self.arah))]
            self.targetTengah = [self.titikTengah[0] + movVector[0], self.titikTengah[1] + movVector[1]]
            speed = jarak/((abs(jarak)//maxMaju+1)*maxKey)
            self.vLurus = [speed*math.cos(np.deg2rad(self.arah)), speed*math.sin(np.deg2rad(self.arah))]

    def majuPutar(self, jarak, sudut):
        if(not(self.lagiGerak)):
            self.maju(jarak)
            self.lagiGerak = False
            self.putar(sudut)

    def getHP(self):
        return self.hp

    def getAmmo(self):
        return self.ammo

    def getArah(self):
        return self.arah

    def getTargetArah(self):
        return self.targetArah

    def getPosisi(self):
        return self.titikTengah

    def getSprite(self):
        return self.sprite

    def updateSprite(self,x=None,y=None,rot=None,scale=None,s_x=None,s_y=None):
        self.sprite.update(x=x,y=y,rotation=rot,scale=scale,scale_x=s_x,scale_y=s_y)

    def setSpriteBatch(self, batch):
        self.sprite.batch = batch

    def isGerak(self):
        return self.lagiGerak
