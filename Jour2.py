
def est_palindrome(texte : str) -> bool :

    texte = "".join(c for c in texte.lower() if c.isalnum())
    print(texte)
    for i in range(len(texte) // 2):
        if texte[i] != texte[len(texte) - 1 - i]:
            print(texte[i], texte[len(texte) - 1 - i])
            return False
    return True


if __name__ == "__main__":
    s1 = "Esope reste ici et se repose"
    s2 = "Bonjour le monde"
    s3 = "Engage le jeu que je le gagne"

    print(est_palindrome(s1))
    print(est_palindrome(s2))
    print(est_palindrome(s3))