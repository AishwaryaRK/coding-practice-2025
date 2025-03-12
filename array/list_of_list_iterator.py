class Iterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.pointer = 0
        self.offset = -1
        while len(self.nested_list[self.pointer]) == 0:
            self.pointer += 1

    def next(self):
        if self.offset + 1 < len(self.nested_list[self.pointer]):
            self.offset += 1
            return self.nested_list[self.pointer][self.offset]
        else:
            self.pointer += 1
            while self.pointer < len(self.nested_list) and len(self.nested_list[self.pointer]) == 0:
                self.pointer += 1
            self.offset = 0
            return self.nested_list[self.pointer][self.offset]

    def has_next(self):
        if len(self.nested_list[self.pointer]) > 0 and self.offset + 1 < len(self.nested_list[self.pointer]):
            return True
        p = self.pointer
        p += 1
        while p < len(self.nested_list) and len(self.nested_list[p]) == 0:
            p += 1
        if p < len(self.nested_list):
            return True
        return False


i = Iterator([[], [1, 2, 3], [4, 5], [], [], [6], [7, 8], [], [9], [10], []])
while i.has_next():
    print(i.next())
