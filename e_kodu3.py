import film

def töötleKäsk(cmd, args):
    if cmd == "E":
        return false
    elif cmd == "K":
        movies = film.loetleFilmid(args)
        for line in movies:
            print(line)
    elif cmd == "L":
        args = args.split(" ", 1)
        film.lisaFilm(args[1], args[0])
    elif cmd == "V":
        film.kustutaFilm(args)
        
    return True
            
while True:
    try:
        commands = input().split(" ", 1)
        töötleKäsk(commands[0], commands[1])
    except:
        break
