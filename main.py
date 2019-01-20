import pyglet
import threading
from config import config
from control import play
import render
import server

if(__name__ == "__main__"):
    # GUI
    #config.robot[0].maju(0)
    serverThread = threading.Thread(target=server.startServerURO)
    serverThread.start()
    pyglet.app.run()