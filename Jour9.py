
def compresser_chaine(chaine : str) -> str:
   
    compresse_chaine = ""
    chaine = chaine.replace(" ", "")
    if not chaine:
       return ""

    for i in range(1, len(chaine)):
        if chaine[i] in compresse_chaine:
            continue
        count = chaine.count(chaine[i])    
        compresse_chaine += f"{chaine[i]}{count} "   

    return compresse_chaine

if __name__ == "__main__":
    s1 = "aaabbbccdaa"
    s2 = "abcd"
    s3 = "wwwwaaadexxxxxx"
    s4 = "azania Kouadio"
    s5 = "Martin matin"
    s7 = "Emmanuel Tahi"

    print(compresser_chaine(s1))  
    print(compresser_chaine(s2))  
    print(compresser_chaine(s3))  
    print(compresser_chaine(s4))  
    print(compresser_chaine(s5))  
    print(compresser_chaine(s7))  