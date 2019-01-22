import numpy as np
import math
import pyglet
from objek import Objek

class Pesawat(Objek):

    def __init__(self, titikTengah, arah, nomor):
        im = pyglet.image.load('sprite/pesawat'+str(nomor)+'.png',
                            decoder=pyglet.image.codecs.png.PNGImageDecoder())
        self.hp = 100
        self.ammo = 1000
        super().__init__(titikTengah,arah,im)

    def __str__(self):
        teksTitikTengah = "Titik Tengah : (%d, %d)\n" % (
            self.getPosisi()[0], self.getPosisi()[1])
        teksArah = "Arah : %.3f\n" % (self.getArah())
        teksDarah = "HP : %.3f\n" % (self.getHP())
        teksAmmo = "Ammo : %d\n" % (self.getAmmo())
        s = teksTitikTengah+teksArah + teksDarah + teksAmmo
        return s

    def getHP(self):
        return self.hp

    def getAmmo(self):
        return self.ammo