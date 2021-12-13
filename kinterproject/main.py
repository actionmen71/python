# import tkinter
# somehow this above line doesn't work
from tkinter import *
from PIL import Image, ImageTk
# PIL was image manipulating package discontinued in 2011, Pillow forked PIL as base and now default
# by default it is not preinstalled
# imagetk is function created for tinker inside pillow

basicgui_root= Tk()
# basic skeleton of gui initiated in basicgui variable

# setting weidth and height for windows gui in this precise order it takes
basicgui_root.geometry("720x480") #it takes argument with small x
# still we can resize this window gui size by mouse as just any other os elements
# so to keep a minimum safe size for this window we use max size and min size function

basicgui_root.minsize(480,240)
basicgui_root.maxsize(1280,720)
# now the windows will limit itself to these upper and lower limit even if we resize
# with the help of mouse pointer but by default it will open to the size of specified
# geometry size



mylabel = Label(text="This is the first label")
mylabel.pack()
# to display label into windows we use pack
# label is an ui element which user doesn't interact with
# even images are packed in label to display it




# for png images
myImage= PhotoImage(file="logo.png")
# setting image file into myImage variable
Imagelabel= Label(image=myImage)
# making myImage as label
Imagelabel.pack()
# here jpg format images are not supported so we use pillow module to workaround



# for jpeg images
myImage2= Image.open("program.jpg")


basicgui_root.mainloop()

# just like pygame this will run loop and update views and settings

