import pyautogui
# this module will let you automate the key pressing feature
from PIL import Image, ImageGrab
# this module is related to images and their actions

def takeScreenshot():
        image=ImageGrab.grab()
        image.show()

def hit(key):
        pyautogui.keyDown(key)

def draw():











if __name__ == '__main__':
        takeScreenshot()



