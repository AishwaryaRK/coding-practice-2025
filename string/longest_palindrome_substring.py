def longestPalindrome(s: str) -> str:
    # if s == "":
    #     return ""
    max_len = 0
    longest_palindrome_substring = ""

    for i, c in enumerate(s):
        # odd case
        l = i
        r = i
        while l in range(len(s)) and r in range(len(s)) and s[l] == s[r]:
            len_substring = (r - l) + 1
            if len_substring > max_len:
                max_len = len_substring
                longest_palindrome_substring = s[l:r + 1]
            l -= 1
            r += 1

        # even case
        l = i
        r = i + 1
        while l in range(len(s)) and r in range(len(s)) and s[l] == s[r]:
            len_substring = (r - l) + 1
            if len_substring > max_len:
                max_len = len_substring
                longest_palindrome_substring = s[l:r + 1]
            l -= 1
            r += 1

    return longest_palindrome_substring


print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("a"))
print(longestPalindrome("abc"))
