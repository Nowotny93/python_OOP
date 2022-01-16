class dictionary_iter:

    def __init__(self, object):
        self.end = len(object)
        self.idx = 0
        self.dict_keys = list(object.keys())
        self.dict_values = list(object.values())

    def __iter__(self):

        return self

    def __next__(self):
        while self.end > 0:
            self.end -= 1
            i = self.idx
            self.idx += 1
            return (self.dict_keys[i], self.dict_values[i])
        else:
            raise StopIteration()

result = dictionry_iter({1: "1", 2: "2"})
for x in result:
    print(x)


