
def compresser_chaine_RLE(chaine : str) -> str:
   
    count = 1
    compresse_chaine = ""
    chaine = chaine.replace(" ", "")
    if not chaine:
       return ""

    for i in range(1, len(chaine)):

        if chaine[i] == chaine[i - 1]:
            count += 1 
        else: 
            compresse_chaine += f"{chaine[i - 1]}{count} "
            count = 1

    compresse_chaine += f"{chaine[i]}{count} "  

    return compresse_chaine

if __name__ == "__main__":
    s1 = "aaabbbccdaa"
    s2 = "abcd"
    s3 = "wwwwaaadeaxxxxxx"
    s4 = "fzzzzzlllhhfhlkfezlfklzej"
    s5 = "rruuruuruipozpapppazoz"
    s7 = "Emmanuel Tahi"

    print(compresser_chaine_RLE(s1))  
    print(compresser_chaine_RLE(s2))  
    print(compresser_chaine_RLE(s3))  
    print(compresser_chaine_RLE(s4))  
    print(compresser_chaine_RLE(s5))  
    print(compresser_chaine_RLE(s7))  