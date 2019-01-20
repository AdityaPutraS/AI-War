import pesawat
import pyglet
from random import randint


class config:
    # Static Variable
    # GUI
    width, height = 500, 500
    # Robot
    banyakRobotAktif = 0
    maxRobot = 20
    robot = [pesawat.Pesawat([-10,-10], randint(0, 360), randint(1, 20)) for _ in range(maxRobot)]
    namaRobot = {}

    def addNewRobot(nama):
        if(config.banyakRobotAktif < config.maxRobot):
            config.banyakRobotAktif += 1
            config.namaRobot[nama] = config.banyakRobotAktif-1
            seed = 10
            x = randint(0,config.width/seed) * seed
            y = randint(0,config.height/seed) * seed
            print(x,y)
            config.robot[config.banyakRobotAktif-1].setTengah(x,y)
            config.robot[config.banyakRobotAktif-1].setTargetTengah(x,y)
            return True
        else:
            return False
