import pesawat
import pyglet

class config:
    # Static Variable
    # GUI
    width, height = 500,500
    # Robot
    banyakRobot = 2
    robot = [pesawat.Pesawat([50,50],0,1), pesawat.Pesawat([100,100],45,2)]
    namaRobot = {'robot1' : 0, 'robot2' : 1}