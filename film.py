def kuvaFailiSisu(fail):
    f = open(fail, "r+", encoding="UTF-8")
    for data in f:
        if len(data) <= 1:
            continue
        else:   
            rida = data.strip()
            print(rida)
    f.close()

def lisaFail(fail):
    f = open(fail, "a+", encoding="UTF-8")
    f.close()

def kustutaFail(fail):
    f = open(fail, "w+", encoding="UTF-8")

def loetleFailid():
    pass