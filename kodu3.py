import film

print("""
=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===
""")

def töötleKäsk(tähis, järjend):
    if tähis == "E":
        return False
    elif tähis == "K" or tähis == "k":
        print("Võimalikud filmid on:")
        temp_list = film.loetleFilmid(järjend[0])
        for i in temp_list:
            print(i)
            
    elif tähis == "L" or tähis == "l":
        filmi_nimi = ""
        for i in range(1, len(järjend)-1):
            filmi_nimi += järjend[i] + " "
        filmi_nimi += järjend[len(järjend)-1]
        print("saadud film: " + filmi_nimi)
        film.lisaFilm(filmi_nimi, järjend[0])
        print("Film lisatud!\n")
    elif tähis == "V" or tähis == "v":
        filmi_nimi = ""
        for i in range(len(järjend)-1):
            filmi_nimi += järjend[i] + " "
        filmi_nimi += järjend[len(järjend)-1]
        print("saadud film: " + filmi_nimi)
        
        film.kustutaFilm(filmi_nimi)
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
    else:
        print("Ei teinud midagi\n")
    return True

while True:
    ans = input("> ")
    tootle = ans.split(" ")
    tahis = tootle[0]
    ylejaanud = tootle[1:]
    tingimus = töötleKäsk(tahis, ylejaanud)
    if not tingimus:
        break

    