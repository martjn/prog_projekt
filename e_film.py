def loetleFilmid(genre):
    movies = []
    f = open("filmid.txt", encoding="UTF-8")
    for line in f:
        line = line.strip("\n")
        if line.endswith(genre):
            movies.append(line.replace(" - " + genre, ""))
    f.close()
    return movies
    
def lisaFilm(name, genre):
    f = open("filmid.txt", encoding="UTF-8")
    data = f.read()
    f.close()
    
    f = open("filmid.txt", "w", encoding="UTF-8")
    f.write(data + "\n" + name + " - " + genre)
    f.close()
    
def kustutaFilm(name):
    f = open("filmid.txt", encoding="UTF-8")
    text = ""
    for line in f:
        if name in line:
            line = ""
        text += line
    f.close()
    
    f = open("filmid.txt", "w", encoding="UTF-8")
    f.write(text)
    f.close()
