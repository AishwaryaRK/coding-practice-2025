def reverseBits(n: int) -> int:
    reverse_n = 0
    for i in range(32):  # 32 bit int
        # last_ith_bit = n & (1 << i)
        bit = (n >> i) & 1
        reverse_n = reverse_n | (bit << (31 - i))
    return reverse_n


print(reverseBits(13)) #32 bit int
# 1101 -> 1011 (11)
