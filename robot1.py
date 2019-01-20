from URORobotLib import *
import math, numpy as np

rob = RobotCakru(nama='Lolz1')

def putarKe(sudut):
    dat = rob.status()
    arah = dat['Arah']
    CW = (arah-sudut)%360
    CCW = (sudut-arah)%360
    if(CW < CCW):
        rob.putarCW(CW)
    else:
        rob.putarCCW(CCW)

def gerakKe(x,y):
    dat = rob.status()
    xPos, yPos = dat['Posisi']
    if(x != xPos):
        sudut = np.rad2deg(math.atan((y-yPos)/(x-xPos))) % 180
        if(x > xPos):
            if(y >= yPos):
                if(y == yPos):
                    sudut = 0
            else:
                # x > xPos && y < yPos
                sudut += 180
        else:
            if(y >= yPos):
                if(y == yPos):
                    sudut = 180
            else:
                # x > xPos && y < yPos
                sudut += 180
    else:
        if(y >= yPos):
            if(y > yPos):
                sudut = 90
        else:
            sudut = 270
    if(xPos != x or yPos != y):
        putarKe(sudut)
        maju = math.sqrt((x-xPos)**2+(y-yPos)**2)
        rob.maju(maju)
    


for i in range(10):
    print('Ke Bagian Bawah Kiri')
    gerakKe(100,100)
    print('Ke Bagian Bawah Kanan')
    gerakKe(400,100)
    print('Ke Bagian Atas Kanan')
    gerakKe(400,400)
    print('Ke Bagian Atas Kiri')
    gerakKe(100,400)
    
