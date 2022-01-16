class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.counter = 0

    def __iter__(self):

        return self

    def __next__(self):

        while self.count > 0:
            i = self.counter
            self.counter += self.step
            self.count -= 1
            return i
        else:
            raise StopIteration()

numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)