def loetleFilmid(žanr):
    f = open("filmid.txt", "r+", encoding="UTF-8")
    filmid = []
    zanrid = []
    for data in f:
        if len(data) <= 1:
            continue
        else:   
            rida = data.strip().split(" - ")
            t_film = rida[0]
            t_zanr = rida[1]
            
        filmid.append(t_film)
        zanrid.append(t_zanr)
    templist = []
    for i in range(len(filmid)):
        if zanrid[i] == žanr:
            templist.append(filmid[i])
    f.close()
    return templist

def lisaFilm(nimi, žanr):
    f = open("filmid.txt", "a+", encoding="UTF-8")
    f.write("\n" + nimi + " - " + žanr)
    f.close()

def kustutaFilm(nimi):
    f = open("filmid.txt", "r+", encoding="UTF-8")
    filmid = []
    zanrid = []
    for data in f:
        if len(data) <= 1:
            continue
        else:   
            rida = data.strip().split(" - ")
            t_film = rida[0]
            t_zanr = rida[1]
            
        filmid.append(t_film)
        zanrid.append(t_zanr)
    curr_data = []
    for i in range(len(filmid)):
        curr_data.append(filmid[i] + " - " + zanrid[i])
 
    for i in range(len(filmid)):
        if nimi == filmid[i]:
            curr_data.pop(i)
    f.seek(0)
    f.truncate()
    for i in range(len(curr_data) -1):
        f.write(curr_data[i] + "\n")

    if not len(curr_data)-1 == -1:
        f.write(curr_data[-1])
    f.close()
kustutaFilm("Vee puudutus")