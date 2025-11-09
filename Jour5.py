
def est_anagramme(mot1 : str, mot2 : str) -> bool :

    from collections import Counter

    mot1 = mot1.lower()
    mot2 = mot2.lower()

    if len(mot1) != len(mot2) :
        return False


    if Counter(mot1) != Counter(mot2) :
        return False
        
        
    return True


if __name__ == '__main__' :

    mot1 = "ecouter"
    mot2 = "recoute"
    mot3 = "chien"
    mot4 = "poche"
    mot5 = "Kader"
    mot6 = "DerKa"

    print(f"Est-ce que '{mot1}' et '{mot2}' sont des anagrammes ? : {est_anagramme(mot1, mot2)}")

    print(f"Est-ce que '{mot3}' et '{mot4}' sont des anagrammes ? : {est_anagramme(mot3, mot4)}")

    print(f"Est-ce que '{mot5}' et '{mot6}' sont des anagrammes ? : {est_anagramme(mot5, mot6)}")