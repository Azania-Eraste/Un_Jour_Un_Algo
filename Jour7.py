
def est_premier(n : int) -> bool:

    if n <=1 :
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def liste_premiers(n : int) -> list:
    premiers = []
    for i in range(2, n + 1):
        if est_premier(i):
            premiers.append(i)
    return premiers

def premiers_jusqua_n(n : int) -> None:
    premiers = liste_premiers(n)
    print(f"Les nombres premiers jusqu'à {n} sont : {premiers}")    

if __name__ == "__main__":
    n = int(input("Entrez un nombre entier n : "))
    
    if est_premier(n):
        print(f"{n} est un nombre premier.")
    else:
        print(f"{n} n'est pas un nombre premier.")
    premiers_jusqua_n(n)