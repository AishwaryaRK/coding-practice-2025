# https://leetcode.com/problems/minimum-window-substring/description/
import collections
import copy


def minWindow1(s: str, t: str) -> str:
    freq_t = collections.defaultdict(int)
    for c in t:
        freq_t[c] += 1
    freq_s = copy.copy(freq_t)

    min_window = ""
    all_chars_t_count = len(freq_t)
    i = j = 0

    while j < len(s) and i <= j:
        c = s[j]
        if c in freq_t:
            freq_s[c] -= 1
            if freq_s[c] == 0:
                all_chars_t_count -= 1
            if all_chars_t_count == 0:
                while all_chars_t_count == 0:
                    c = s[i]
                    if c in freq_t:
                        freq_s[c] += 1
                        if freq_s[c] > 0:
                            all_chars_t_count += 1
                    i += 1

                window = s[i - 1:j + 1]
                if min_window == "":
                    min_window = window
                elif len(window) < len(min_window):
                    min_window = window

        j += 1

    return min_window


print(minWindow1(s="ADOBECODEBANC", t="ABC"))
print(minWindow1(s="bba", t="ab"))
