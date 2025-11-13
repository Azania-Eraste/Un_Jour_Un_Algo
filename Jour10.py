

def frequence(chaine: str) -> dict:
    freq = {}
    for char in chaine:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def freq_max(chaine: str) -> int:
    freq = frequence(chaine)
    max_freq = max(freq.values())
    return max_freq

def reorganiser_chaine(chaine: str) -> str:

    max_freq = freq_max(chaine)
    if max_freq > (len(chaine) + 1) // 2:
        return "Impossible : trop de répétitions"
    
    freq = frequence(chaine)

    items = []
    for c in freq:
        items.append((c, freq[c]))



    for i in range(len(items)):
        max_i = i
        for j in range(i + 1, len(items)):
            if items[j][1] > items[max_i][1]:
                max_i = j
        items[i], items[max_i] = items[max_i], items[i]




    res = [""] * len(chaine)

    index = 0

    for caractere, count in items:
        for _ in range(count):
            res[index] = caractere
            index += 2
            if index >= len(chaine):
                index = 1

    return "".join(res)


if __name__ == "__main__":
    s1 = "aaab"
    s2 = "aabbcc"
    s3 = "aaaaabc"
    s4 = "a"
    s5 = "ab"
    s6 = "aaabc"
    s7 = "aaabbc"

    res = reorganiser_chaine(s1)
    print(f'chaine entrée : {s1} -> chaine reorganisée : {res}')  
    res = reorganiser_chaine(s2)
    print(f'chaine entrée : {s2} -> chaine reorganisée : {res}')  
    res = reorganiser_chaine(s3)
    print(f'chaine entrée : {s3} -> chaine reorganisée : {res}')
    res = reorganiser_chaine(s4)
    print(f'chaine entrée : {s4} -> chaine reorganisée : {res}')
    res = reorganiser_chaine(s5)
    print(f'chaine entrée : {s5} -> chaine reorganisée : {res}')  
    res = reorganiser_chaine(s6)
    print(f'chaine entrée : {s6} -> chaine reorganisée : {res}')    
    res = reorganiser_chaine(s7)
    print(f'chaine entrée : {s7} -> chaine reorganisée : {res}')  

