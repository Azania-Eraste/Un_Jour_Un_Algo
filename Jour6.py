
def compter_voyelles(phrase: str) -> int: 
    phrase = phrase.replace(" ", "").tolower()
    voyelles = set("aeiouyâêèùéîôûäëïöüÿ")

    compteur = 0
    for lettre in phrase:
        if lettre in voyelles:
            compteur += 1
    return compteur

if __name__ == '__main__' :

    phrase1 = "Bonjour le monde"
    phrase2 = "Python est génial"
    phrase3 = "L'intelligence artificielle"
    
    print(f"Le nombre de voyelles dans la phrase '{phrase1}' est : {compter_voyelles(phrase1)}")
    print(f"Le nombre de voyelles dans la phrase '{phrase2}' est : {compter_voyelles(phrase2)}")
    print(f"Le nombre de voyelles dans la phrase '{phrase3}' est : {compter_voyelles(phrase3)}")