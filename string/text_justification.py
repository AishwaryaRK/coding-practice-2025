from typing import List


def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    result = []
    line = []
    char_cnt = 0
    word_cnt = 0
    i = 0
    while i < len(words):
        word = words[i]
        if char_cnt + 1 + len(word) <= maxWidth:
            if line:
                line.append(" ")
                char_cnt += 1
            line.append(word)
            char_cnt += len(word)
            word_cnt += 1
            i += 1
        else:
            spaces = maxWidth - char_cnt
            if word_cnt == 1:
                line.append(" " * spaces)
            else:
                gap = spaces // (word_cnt - 1)
                remainder_spaces = spaces % (word_cnt - 1)
                end = len(line) - 1
                if gap == 0:
                    gap = 1
                    remainder_spaces = 0
                    end = spaces * 2
                for j in range(1, end, 2):
                    if j == 1:
                        # print(gap)
                        # print(remainder_spaces)
                        # print(line[j - 1])
                        line[j] += " " * (gap + remainder_spaces)
                    else:
                        line[j] += " " * gap
            result.append("".join(line))
            line = []
            char_cnt = 0
            word_cnt = 0
        if i == len(words):
            line.append(" " * (maxWidth - char_cnt))
            result.append("".join(line))
            break
    return result


# print(fullJustify(words=["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16))
# print(fullJustify(words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16))
print(fullJustify(
    words=["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
           "Art", "is", "everything", "else", "we", "do"], maxWidth=20))
