import os
from pixboard import *
from PIL import Image
#import Image
#from matplotlib import pyplot as plt

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

def loetleFailid(path=".", laiend=None):
    #for subdir, dirs, files in os.walk('./'):
    #    for file in files:
    #        print(file)

    sisu = os.listdir(path)
    leidubFail = False
    if laiend == None:
        for x in sisu:
            print(x)
    else:
        for x in sisu:
            if x.endswith(laiend):
                leidubFail = True
                break
    if leidubFail:
        for x in sisu:
            if x.endswith(laiend):
                print(x)

def kuvaPilt(fail):
    image = Image.open(fail)
    image.show()
    

#kuvaPilt("wut.png")


