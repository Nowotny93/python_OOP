from copy import deepcopy


class CustomList:
    def __init__(self, *args):
        self.__values = list(args)

    def append(self, value):
        self.__values.append(value)

    def remove(self, index):
        try:
            return self.__values.pop(index)
        except IndexError:
            raise IndexError("Invalid index")

    def get(self, index):
        try:
            return self.__values[index]
        except IndexError:
            raise IndexError("Invalid index")

    def extend(self, object):
        try:
            iter(object)
            self.__values.extend(object)
        except TypeError:
            self.__values.append(object)

        return deepcopy(self.__values)

    def insert(self, index, value):
        if index >= len(self.__values) or index < 0:
            raise IndexError("Invalid index")
        self.__values.insert(index, value)
        return self.__values

    def pop(self):
        try:
            return self.__values.pop()
        except IndexError:
            raise IndexError("No elements in the list")

    def clear(self):
        self.__values = []

    def index(self, val):
        try:
            return self.__values.index(val)
        except ValueError:
            raise ValueError("Element is not in the list")

    def count(self, val):
        return self.__values.count(val)

    def reverse(self):
        return self.__values[::-1]

    def copy(self):
        return deepcopy(self.__values)

    def size(self):
        return len(self.__values)

    def add_first(self, val):
        self.__values.insert(0, val)

    def dictionize(self):
        res = {}
        for index in range(0, len(self.__values), 2):
            if index == len(self.__values) - 1:
                res.update({self.__values[index]: ' '})
            else:
                res.update({self.__values[index]: self.__values[index+1]})
        return res

    def move(self, amount):
        if amount > len(self.__values) or amount < 0:
            raise ValueError("Invalid amount")
        self.__values = self.__values[amount:] + self.__values[:amount]

    def sum(self):

        result = 0
        for el in self.__values:
            if isinstance(el, int) or isinstance(el, float):
                result += el
            elif hasattr(el, '__len__'):
                result += len(el)
            else:
                raise CustomListSumException(
                    f"Please provide a len method to custom objects if you want to sum elements.\n")
        return result

    def overbound(self):
        max_number = float('-inf')
        element = None
        for el in self.__values:
            if not isinstance(el, int) and not isinstance(el, float):
                num = len(el)
            else:
                num = el
            if max_number < num:
                max_number = num
                element = el
        return self.index(element)

    def underbound(self):
        min_number = float('inf')
        element = None
        for el in self.__values:
            if not isinstance(el, int) and not isinstance(el, float):
                num = len(el)
            else:
                num = el
            if min_number > num:
                min_number = num
                element = el
        return self.index(element)
