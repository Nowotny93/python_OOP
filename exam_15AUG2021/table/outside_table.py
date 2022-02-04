from python_oop_exams.project_15AUG2021 import Table

class OutsideTable(Table):

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if value < 1 or value > 50:
            raise ValueError("Outside table's number must be between 1 and 50 inclusive!")
        self.__table_number = value
