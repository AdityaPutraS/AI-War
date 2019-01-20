import sys
from config import config
def play(no_robot):
    tmpPath = sys.path
    sys.path.append("..")
    tmpModule = __import__('robot.robot'+str(no_robot),globals(),locals(),['control'],0)
    sys.path = tmpPath
    tmpModule.control(config.robot[no_robot-1])
    
    