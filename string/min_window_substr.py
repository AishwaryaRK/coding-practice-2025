# https://leetcode.com/problems/minimum-window-substring/description/
import collections
import math
import copy


def minWindow(s: str, t: str) -> str:
    min_window = ""

    freq_t = collections.defaultdict(int)
    for c in t:
        freq_t[c] += 1

    freq_s = copy.copy(freq_t)
    freq_s_multi = collections.defaultdict(int)
    i = j = 0
    while i < len(s) and j < len(s):
        c = s[j]
        if c in freq_t:
            freq_s[c] -= 1
            f = freq_s[c]
            if f <= 0:
                del freq_s[c]
            if f < 0 and min_window!="":
                freq_s_multi[c] += 1
            if f < 0 and min_window != "":
                while s[i] != c:
                    ch = s[i]
                    if ch in freq_t:
                        freq_s[ch] += 1
                    i += 1
                i += 1
                if freq_t[c] - 1 > 0:
                    freq_s[c] = freq_t[c] - 1
            if not freq_s:
                while (s[i] not in freq_t or s[i] in freq_s_multi) and i < j:
                    ch = s[i]
                    if ch in freq_s_multi:
                        freq_s_multi[ch] -= 1
                        if freq_s_multi[ch] == 0:
                            del freq_s_multi[ch]
                    i += 1

                window = s[i:j + 1]
                if min_window == "":
                    min_window = window
                elif len(window) < len(min_window):
                    min_window = window
        j += 1

    return min_window


print(minWindow(s="ADOBECODEBANC", t="ABC"))
print(minWindow(s="bba", t="ab"))
