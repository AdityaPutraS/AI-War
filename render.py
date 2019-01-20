import numpy as np
from config import config
import pyglet

# Graphic
batchPesawat = pyglet.graphics.Batch()
for r in config.robot:
    r.setSpriteBatch(batchPesawat)

window = pyglet.window.Window(config.width, config.height, caption = 'AI-War Sekolah URO')

@window.event
def on_key_press(symbol, modifiers):
    print(symbol)
    if(symbol == 97):
        print('Ti Teng : ',config.robot[0].titikTengah)
        print('Targ Teng : ',config.robot[0].targetTengah)
        print('Arah : ',config.robot[0].arah)
        print('Targ Arah : ',config.robot[0].targetArah)
    elif(symbol == 115):
        print(config.robot[0].getPosisi())
        print(config.robot[0].getArah())
    elif(symbol == 100):
        for r in range(config.banyakRobotAktif):
            print(config.robot[r])

@window.event
def on_draw():
    window.clear()
    #Batch Drawing
    batchPesawat.draw()

def updateAll(dt):
    for r in range(config.banyakRobotAktif):
        config.robot[r].update()

pyglet.clock.schedule_interval(updateAll,1/60)
