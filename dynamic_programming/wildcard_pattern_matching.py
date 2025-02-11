def isMatch(s: str, p: str) -> bool:
    s_index = p_index = 0
    star_index = -1
    s_star_index = -1
    while s_index < len(s):
        if p_index < len(p) and (s[s_index] == p[p_index] or p[p_index] == '?'):
            s_index += 1
            p_index += 1
        elif p_index < len(p) and p[p_index] == '*':
            star_index = p_index
            s_star_index = s_index
            p_index += 1
        else:
            if star_index == -1:
                return False
            else:
                s_index = s_star_index + 1
                s_star_index += 1
                p_index = star_index + 1
    if p_index < len(p):
        l = len(p) - p_index
        if p[p_index:] != '*' * l:
            return False
    return True


print(isMatch("aa", "??***"))
print(isMatch("a","a**"))
print(isMatch("abcabczzzde", "*abc???de*"))
print(isMatch("aaaa", "***a"))
