class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.idx = 0

    def __iter__(self):

        return self

    def __next__(self):

        while self.number > 0:
            i = self.idx
            self.idx += 1
            self.number -= 1
            if len(self.sequence) == i:
                self.idx = 0
                i = self.idx
                self.idx += 1
            return self.sequence[i]
        else:
            raise StopIteration()

result = sequence_repeat("I love Python", 3)
for item in result:
    print(item, end ="")