import collections


def differ_by_one_char(words):
    trie = collections.defaultdict(dict)
    reverse_trie = collections.defaultdict(dict)

    def get_prefix_length(t, word):
        prefix_count = 0
        prefix_found = False
        for i, w in enumerate(word):
            if w not in t:
                t[w] = {}
                prefix_found = True
            elif not prefix_found:
                prefix_count += 1
            t = t[w]
            if i == len(word) - 1:
                t[None] = True
        return prefix_count

    for word in words:
        prefix_len = get_prefix_length(trie, word)
        suffix_len = get_prefix_length(reverse_trie, word[::-1])
        if prefix_len + suffix_len + 1 == len(word):
            return True

    return False


print(differ_by_one_char(["abc", "xyz", "abd"]))
print(differ_by_one_char(["abc", "def", "xyz"]))
print(differ_by_one_char(["abcd", "bbbb", "abxd", "cccc"]))