import numpy as np
import math
import pyglet

maxMaju = 200
maxPutar = 180
maxKey = 30


class Objek:

    def __init__(self, titikTengah, arah, im):
        # Arah 0 derajat = menghadap timur
        self.titikTengah = titikTengah
        self.targetTengah = titikTengah
        self.arah = arah
        self.targetArah = arah
        self.sprite = pyglet.sprite.Sprite(
            img=im, x=titikTengah[0], y=titikTengah[1])
        self.sprite.image.anchor_x = self.sprite.image.width / 2
        self.sprite.image.anchor_y = self.sprite.image.height / 2
        self.vLurus = [0, 0]
        self.vPutar = 0
        self.lagiMaju = False
        self.lagiPutar = False
        self.tickAnimasi = 0

    def __str__(self):
        teksTitikTengah = "Titik Tengah : (%d, %d)\n" % (
            self.getPosisi()[0], self.getPosisi()[1])
        teksArah = "Arah : %.3f\n" % (self.getArah())
        s = teksTitikTengah+teksArah
        return s

    def update(self):
        x1, y1 = self.titikTengah
        x2, y2 = self.targetTengah
        if(self.isGerak()):
            if(self.tickAnimasi >= maxKey):
                self.lagiMaju = False
                self.lagiPutar = False
                self.tickAnimasi = 0
            else:
                if(self.lagiMaju):
                    dx,dy = self.vLurus
                    self.setTengah(x1+dx,y1+dy)
                if(self.lagiPutar):
                    self.setArah(self.arah+self.vPutar)
                self.tickAnimasi += 1

        x, y = self.titikTengah
        self.updateSprite(x=x, y=y, rot=-self.arah)

    def putarCW(self, deg):
        #Asumsi deg >= 0 && deg < maxPutar
        self.lagiPutar = True
        self.setTargetArah(deg % 360)
        self.vPutar = -deg/maxKey
        self.tickAnimasi = 0

    def putarCCW(self, deg):
         #Asumsi deg >= 0 && deg < maxPutar
        self.lagiPutar = True
        self.setTargetArah(360 - (deg % 360))
        self.vPutar = deg/maxKey
        self.tickAnimasi = 0

    def maju(self, jarak):
        #Asumsi abs(jarak) < maxMaju
        self.lagiMaju = True
        movVector = [
            jarak*math.cos(np.deg2rad(self.arah)), jarak*math.sin(np.deg2rad(self.arah))]
        x,y = self.titikTengah
        self.setTargetTengah(x+movVector[0], y+movVector[1])
        speedX = movVector[0]/maxKey
        speedY = movVector[1]/maxKey
        self.vLurus = [speedX,speedY]
        self.tickAnimasi = 0

    def majuPutar(self, jarak, sudut):
        pass

    def setTengah(self, x, y):
        self.titikTengah = [x, y]

    def setTargetTengah(self,x,y):
        self.targetTengah = [x, y]

    def setArah(self, arah):
        self.arah = arah

    def setTargetArah(self,arah):
        self.targetArah = arah

    def getArah(self):
        return self.arah

    def getTargetArah(self):
        return self.targetArah

    def getPosisi(self):
        return self.titikTengah

    def getSprite(self):
        return self.sprite

    def updateSprite(self, x=None, y=None, rot=None, scale=None, s_x=None, s_y=None):
        self.sprite.update(x=x, y=y, rotation=rot,
                           scale=scale, scale_x=s_x, scale_y=s_y)

    def setSpriteBatch(self, batch):
        self.sprite.batch = batch

    def isGerak(self):
        return self.lagiMaju or self.lagiPutar
