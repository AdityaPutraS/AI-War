from objek import Objek
import numpy as np
import math
import pyglet


class Peluru(Objek):
    
    def __init__(self,titikTengah, arah):
        im = pyglet.image.load('sprite/peluru.png',
                                decoder=pyglet.image.codecs.png.PNGImageDecoder())
        super().__init__(titikTengah,arah,im)
        