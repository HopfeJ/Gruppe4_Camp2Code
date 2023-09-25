from pynput.keyboard import Key, Controller
from gpiozero import Robot
import time
robot = Robot(left=(4,14), right=(17, 18))

keyboard = Controller()

def main():
    a = input('gib was an')
    if a == 'w':
        robot.forward(1)
        time.sleep(1)
    #elif kp.Key() == 's':
    #    robot.backward(1)
    #elif kp.Key() == 'a':
    #    robot.left(0.5)
    #elif kp.Key() == 'd':
    #    robot.right(0.5)
    else:
        robot.stop()

def key_test():




if __name__ == '__main__':
    #while True:
        #main()
    key_test()