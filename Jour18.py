
def FusionnedSortedLists(list1, list2):
    """
    Fusionne deux listes triées en une seule liste triée.

    Paramètres:
        list1 (list): Première liste triée.
        list2 (list): Deuxième liste triée.

    Retourne:
        list: Liste fusionnée et triée.
    """
    merged_list = []
    i, j = 0, 0

    # Parcourir les deux listes et ajouter les éléments les plus petits à la liste fusionnée
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Ajouter les éléments restants de list1, s'il y en a
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # Ajouter les éléments restants de list2, s'il y en a
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

if __name__ == "__main__":


    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8]
    result = FusionnedSortedLists(list1, list2)
    print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]