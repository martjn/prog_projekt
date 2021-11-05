import os
from pixboard import *
from PIL import Image
import imghdr
#import Image
#from matplotlib import pyplot as plt

# Seab kõik failid kaustast järjendisse
def files(path="."):
    return os.listdir(path)

# Teeb hulga olemasolevatest piltidest kaustas
def imgs_in_folder(arg):
    images = set()
    for el in arg:
        img = imghdr.what(el)
        if img:
            images.add(el)
    if len(images):
        return images
    return None

def kuvaFailiSisu(fail):
    f = open(fail, "r+", encoding="UTF-8")
    for data in f:
        print(data)
    f.close()

def lisaFail(fail):
    f = open(fail, "a+", encoding="UTF-8")
    f.close()

def kustutaFail(fail):
    if os.path.exists(fail):
        os.remove(fail)
    else:
        print("The file does not exist")

def kuvaPilt(fail):
    image = Image.open(fail)
    image.show()
    
#kuvaPilt("wut.png")
