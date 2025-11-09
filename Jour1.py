

def second_plus_grand (elt : list) -> int | None: 
    
    if not elt or len(elt) < 2 or all(x == elt[0] for x in elt):
        return None
    temps = None
    premier = max(elt)


    elt = [x for x in elt if x != premier]


    for l in elt:
        
        if temps is None or l > temps:
            temps = l

    
    return temps

if __name__ == "__main__":

    l = [3, 1, 4, 4, 5, 5, 2]
    l2 = [7, 7, 7]
    l3 = [4,3,8,2,9,5,9,1]

    print(second_plus_grand(l))
    print(second_plus_grand(l2))
    print(second_plus_grand(l3))