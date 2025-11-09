

def mot_le_plus_long(phrase :str) -> tuple :

    split = phrase.split(" ")
    longueur = 0
    mot_long = ""
    mot = ()

    for elt in split:

        if len(elt) > longueur :
            longueur = len(elt)
            mot_long = elt

    mot = (mot_long, longueur)
    return mot

if __name__ == '__main__' :

    res = mot_le_plus_long("je teste ma fonction")
    print("Le mot le plus long est :", res[0], "et sa longueur est :", res[1])
    res = mot_le_plus_long("Le chat est sur le toit")
    print("Le mot le plus long est :", res[0], "et sa longueur est :", res[1])
    res = mot_le_plus_long("Python est un langage de programmation")
    print("Le mot le plus long est :", res[0], "et sa longueur est :", res[1])
    res = mot_le_plus_long("L'intelligence artificielle est fascinante")
    print("Le mot le plus long est :", res[0], "et sa longueur est :", res[1])
