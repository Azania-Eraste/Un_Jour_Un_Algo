
def LongestReapeatingSubstring(s: str) -> str:
    n = len(s)
    longest_subs = ""

    for i in range(n - 1,0, -1):
        deja_vu = set()
        for j in range(n - i + 1):
            substring = s[j:j + i]
            
            if substring in deja_vu:
                longest_subs = substring
                return f'La chaine la plus repetee est: {longest_subs}'
            deja_vu.add(substring)
            
    return 'Aucune chaine repetee trouvee.'

if __name__ == "__main__":
    print(LongestReapeatingSubstring("abcabcbb"))  # Output: "abc"
    print(LongestReapeatingSubstring("bbbbb"))     # Output: "b"
    print(LongestReapeatingSubstring("pwwkew"))    # Output: "w"
    print(LongestReapeatingSubstring("abcd"))      # Output: ""
    print(LongestReapeatingSubstring("aabcaabdaab"))  # Output: "aab"