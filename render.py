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
        config.robot[0].maju(100)
    elif(symbol == 115):
        print(config.robot[0].getPosisi())
        print(config.robot[0].getArah())
    elif(symbol == 100):
        print(config.robot[0].isGerak())
    elif(symbol == 113):
        print('Arah : ',config.robot[0].getArah())
        print('Target Arah : ',config.robot[0].getTargetArah())
        config.robot[0].putar(120)
        print('Arah : ',config.robot[0].getArah())
        print('Target Arah : ',config.robot[0].getTargetArah())
    elif(symbol == 101):
        print('Arah : ',config.robot[0].getArah())
        print('Target Arah : ',config.robot[0].getTargetArah())
        config.robot[0].putar(-120)
        print('Arah : ',config.robot[0].getArah())
        print('Target Arah : ',config.robot[0].getTargetArah())

@window.event
def on_draw():
    window.clear()
    #Batch Drawing
    batchPesawat.draw()

def updateAll(dt):
    for r in config.robot:
        r.update()

pyglet.clock.schedule_interval(updateAll,1/60)
