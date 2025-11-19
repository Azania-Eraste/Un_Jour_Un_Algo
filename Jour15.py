
def LongestPalindromeSubstring(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""

    start, max_length = 0, 1

    for i in range(n):
        # Odd length palindromes
        left, right = i, i
        while left >= 0 and right < n and s[left] == s[right]:
            current_length = right - left + 1
            if current_length > max_length:
                start = left
                max_length = current_length
            left -= 1
            right += 1

        # Even length palindromes
        left, right = i, i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            current_length = right - left + 1
            if current_length > max_length:
                start = left
                max_length = current_length
            left -= 1
            right += 1

    return s[start:start + max_length]


if __name__ == "__main__":
    print(LongestPalindromeSubstring("babad"))  # Output: "bab" or "aba"
    print(LongestPalindromeSubstring("cbbd"))   # Output: "bb"
    print(LongestPalindromeSubstring("a"))      # Output: "a"
    print(LongestPalindromeSubstring("ac"))     # Output: "a" or "c"
    print(LongestPalindromeSubstring("racecar")) # Output: "racecar"