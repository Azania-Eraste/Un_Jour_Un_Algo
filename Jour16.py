
def findKthSmallest(arr: list, k: int) -> int:
    """
    trouve le plus petit élément d'une liste

    :paramètre arr: liste des entiers
    :paramètre k: la position de l'element  (k - 1)
    :retourne: le K-ieme element de la liste
    """
    if k < 1 or k > len(arr):
        raise ValueError("k doit être inferieur ou égal à la taille de la liste et supérieur à 0.")

    for i in range(k):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]    
     

    return arr[k - 1]



if __name__ == "__main__":
    liste = [7, 10, 4, 3, 20, 15]
    k = 3
    print(f"Le {k}-ième plus petit élément est : {findKthSmallest(liste, k)}")  # Output: 7