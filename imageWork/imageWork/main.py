'''
Created on 

@author: Administrator
'''
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
import requests
from io import BytesIO
# This one is in Main.py only
from image_functions import * # This is from the other filename name"image_functions"

if __name__ == '__main__':
    # open an image file. The default path is where this python module is
    #im = Image.open("SiriusAndViolet.jpg")
    #print(im.width, im.height, im.mode, im.format)  # Display some info about the image
    
    #my_image = load_image("SiriusAndVioletX.jpg")
    #if my_image != None:
    #    my_image.show(my_image)
    #else:
    #    print("Unable to open file")

    #im = Image.open("SiriusAndViolet.jpg")  
    #im_c = im.crop((200,300,400,500)) # (left, top, right, bottom) it's a tuple!
    #im_c.show()
    
    my_image = blur_image(load_image("SiriusAndViolet.jpg"))   #Nested funtion calls
    my_image.show()