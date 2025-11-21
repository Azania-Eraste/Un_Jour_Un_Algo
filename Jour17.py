

def LongestIncreasingSubsequence(arr) -> list:
    """
    Trouve la longueur de la plus longue sous-séquence croissante dans une liste d'entiers.

    :param arr: liste des entiers
    :return: longueur de la plus longue sous-séquence croissante
    """
    n = len(arr)
    if n == 0:
        return 0

    lis = [] 
    deja_vu = set()
        

    for i in range(1, n):
        for j in range(0, i):
           
            if arr[i] > arr[j] and arr[i] not in deja_vu and arr[j] not in deja_vu:
                if lis == [] :
                   
                    lis.append(arr[j])
                    lis.append(arr[i])
                    deja_vu.add(arr[i])
                    deja_vu.add(arr[j])
                    
                elif  lis[-1] < arr[i]:
                    lis.append(arr[i])
                    deja_vu.add(arr[i])
                    continue
            

    return lis

if __name__ == "__main__":

    arr1 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    arr2 = [3, 10, 2, 1, 20]
    arr3 = [3, 2]
    arr4 = [50, 3, 10, 7, 40, 80]
    
    print(LongestIncreasingSubsequence(arr1))  # Output: 6
    print(LongestIncreasingSubsequence(arr2))  # Output: 3
    print(LongestIncreasingSubsequence(arr3))  # Output: 1
    print(LongestIncreasingSubsequence(arr4))  # Output: 4