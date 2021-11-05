import os
def kuvaFailiSisu(fail):
    f = open(fail, "r+", encoding="UTF-8")
    for data in f:
        print(data)
    f.close()

def lisaFail(fail):
    f = open(fail, "a+", encoding="UTF-8")
    f.close()

def kustutaFail(fail):
    f = open(fail, "w+", encoding="UTF-8")

def loetleFailid():
    #for subdir, dirs, files in os.walk('./'):
    #    for file in files:
    #        print(file)
    sisu = os.listdir(".")
    for x in sisu:
        print(x)



loetleFailid()