
def trouver_paire(liste : list , cible : int) -> list :

    paires = []
    vus = set()

    for n in liste : 
        
        deuxieme_elt_paire = cible - n
        paire = tuple(sorted((n, deuxieme_elt_paire)))

        if paire not in vus :
            for i in range(len(liste)) :
                if liste[i] == deuxieme_elt_paire and liste.index(n) != i :
                    vus.add(paire)
                    paires.append(paire)

    return paires


if __name__ == "__main__" :
    

    print(trouver_paire([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))
    print(trouver_paire([1, 3, 3, 7, 5, 6, 8, 5, 9], 12))
    print(trouver_paire([1, 8, 3, 2, 5, 5, 7, 1, 9], 15))
