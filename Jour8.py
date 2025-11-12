

def trouver_min_max(liste: list) -> tuple:

    if liste is None or len(liste) == 0 or all(x == liste[0] for x in liste):
        return None
    
    indice_min = -1
    indice_max = -1
    val_min = liste[0]
    val_max = liste[0]

    for i in range(1, len(liste)):
        if liste[i] > val_max:
            val_max = liste[i]
            indice_max = i
        elif liste[i] < val_min:
            val_min = liste[i]
            indice_min = i
    return {'min_et_max' : (val_min, val_max), 'indices' : (indice_min, indice_max)}


def afficher_liste(liste: list) -> None:
    
    res = trouver_min_max(liste)
    if res is None:
        print("La liste ne contient pas de minimum et de maximum distincts.")
    else:
        print(f"Le minimum est {res['min_et_max'][0]} à l'indice {res['indices'][0]}, "
                f"le maximum est {res['min_et_max'][1]} à l'indice {res['indices'][1]}.")
            


if __name__ == "__main__":

    l = [3, 1, 4, 4, 2,5, 5, 2]
    l2 = [7, 7, 7]
    l3 = [4,3,8,2,9,5,9,1]
    l4 = [7, 3, 5, 3, 9, 3, 6]

    afficher_liste(l)
    afficher_liste(l2)
    afficher_liste(l3)
    afficher_liste(l4)
