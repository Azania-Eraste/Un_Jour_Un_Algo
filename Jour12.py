alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mod = 26
caractère = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'



def letter_to_number(letter: str) -> int|str:
    """Convertit une lettre (A-Z) en nombre (0-25)."""

    if letter in alphabet:
        return alphabet.index(letter.upper())
        
    return letter

def number_to_letter(number: int, is_upper: bool) -> str:
    """Convertit un nombre en lettre (avec réduction modulo 26)."""

    if isinstance(number,int):
        return alphabet[number % mod].lower() if not is_upper else alphabet[number % mod]  
    return number


def to_numbers(text: str) -> list[tuple[int, bool]]:
    """
    Convertit une chaîne en liste de nombres.
    """
    
    return [(letter_to_number(c.upper()), c.isupper()) for c in text]

def to_letters(nums: list[tuple[int, bool]]) -> str:
    """Convertit une liste de nombres en chaîne de lettres."""
    return ''.join(number_to_letter(n, b) for n , b in nums)

def Cesare_encrypt(chaine : str, k : int):
    """
    Chiffrement Cesare.
    - On conserve uniquement les lettres A-Z.
    """

    liste_chaine = []
    
    for i, is_upper in to_numbers(chaine):

        if isinstance(i,int):
            liste_chaine.append((i + k, is_upper))
        else :
            liste_chaine.append((i, is_upper))
    chaine = to_letters(liste_chaine)

    return chaine

def cesare_decrypt(chaine : str, k : int):
    """
    Déchiffrement Cesare.
    - On conserve uniquement les lettres A-Z.
    """

    liste_chaine = []
    
    for i, is_upper in to_numbers(chaine):

        if isinstance(i,int):
            liste_chaine.append((i - k, is_upper))
        else :
            liste_chaine.append((i, is_upper))
    chaine = to_letters(liste_chaine)

    return chaine

if __name__ == "__main__":
    s1 = "aaabbbccdaa"
    s2 = "abcdD"
    s3 = "wwwwaaadeaxxxxxx"
    s4 = "fzzzzzll lhhfhlkfezlfklzej"
    s5 = "rruuruuruipozpapppazoz"
    s7 = "Emmanuel Tahi"
    s8 = "Dev!"

    print(Cesare_encrypt(s1,2))  
    print(cesare_decrypt(Cesare_encrypt(s1,2),2))  
    print(Cesare_encrypt(s2,5))  
    print(Cesare_encrypt(s3,-2))  
    print(Cesare_encrypt(s4,8))  
    print(Cesare_encrypt(s7,153))  
    print(Cesare_encrypt(s8,-3))  


    

   
