

def overlap(interval1 : list, interval2 : list) -> bool:

    """ Verifier si deux intervalles se chevauchent.
        Parametres:
        
            interval1 (list): Une liste contenant deux entiers representant le debut et la fin du premier intervalle.
            interval2 (list): Une liste contenant deux entiers representant le debut et la fin du deuxieme intervalle.
        Retour:
            bool: True si les intervalles se chevauchent, False sinon.
    """

    if interval1[0] > interval2[1] or interval2[0] > interval1[1]:
        return False
    return True


if __name__ == "__main__":
    # Exemples de test
    print(overlap([1, 5], [4, 6]))  # True
    print(overlap([1, 3], [5, 6]))  # False
    print(overlap([2, 7], [5, 10])) # True
    print(overlap([8, 12], [1, 5])) # False