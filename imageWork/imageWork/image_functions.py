'''
Created on 

@author: Administrator
'''
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
import requests
from io import BytesIO


'''
    Load an image file from disk
    :param filename: The file to load
    :return the image object
'''
def load_image( filename ) :
    try:
        myimage = Image.open(filename)
        myimage.load()
        return myimage
    except:
        return None
    

def save_image( imageObject, outfilename ) :
    '''
    Save an image to disk
    :param imageObject: The Image to save
    :param outfilename: The target file
    '''
    imageObject.save( outfilename )

