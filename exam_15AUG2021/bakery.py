from python_oop_exams.project_15AUG2021 import Bread
from python_oop_exams.project_15AUG2021.baked_food.cake import Cake
from python_oop_exams.project_15AUG2021.drink import Tea
from python_oop_exams.project_15AUG2021.drink import Water
from python_oop_exams.project_15AUG2021.table.inside_table import InsideTable
from python_oop_exams.project_15AUG2021.table.outside_table import OutsideTable


class Bakery:

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0
        self.food_names = set()
        self.drink_names = set()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('Name cannot be empty string or white space!')
        self.__name = value

    def add_food(self, food_type, name, price):

        for f in self.food_menu:
            if f.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")

        valid_types = ["Bread", "Cake"]
        if food_type == valid_types[0]:
            food = Bread(name, price)
        else:
            food = Cake(name, price)

        self.food_menu.append(food)
        self.food_names.add(food.name)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):

        for d in self.drinks_menu:
            if d.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        valid_types = ["Tea", "Water"]
        if drink_type == valid_types[0]:
            drink = Tea(name, portion, brand)
        else:
            drink = Water(name, portion, brand)

        self.drinks_menu.append(drink)
        self.drink_names.add(drink.name)
        return f"Added {name} ({drink_type}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):

        for t in self.tables_repository:
            if t.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        valid_types = ["InsideTable", "OutsideTable"]
        if table_type == valid_types[0]:
            table = InsideTable(table_number, capacity)
        else:
            table = OutsideTable(table_number, capacity)

        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):

        needed_table = self.get_table(number_of_people)
        if needed_table is None:
            raise Exception(f"No available table for {number_of_people} people")
        needed_table.reserve(number_of_people)
        return f"Table {needed_table.table_number} has been reserved for {number_of_people} people"

    def get_table(self, number_of_people):

        try:
            table = [t for t in self.tables_repository if not t.is_reserved and t.capacity >= number_of_people][0]
        except IndexError:
            table = None
        return table

    def __get_table_by_number(self, table_number):
        tables = [t for t in self.tables_repository if t.table_number == table_number]
        return tables[0] if tables else None

    def __get_food_by_name(self, n):
        food = [f for f in self.food_menu if f.name == n]
        return food[0] if food else None

    def __get_drink_by_name(self, n):
        drink = [d for d in self.drinks_menu if d.name == n]
        return drink[0] if drink else None

    def order_food(self, table_number, *args):

        table = self.__get_table_by_number(table_number)

        if not table:
            return f"Could not find table {table_number}"

        food_names_in_menu = [name for name in args if name in self.food_names]
        food_names_not_in_menu = [name for name in args if name not in self.food_names]

        foods = [self.__get_food_by_name(food_name) for food_name in food_names_in_menu]
        [table.order_food(f) for f in foods]

        ordered_foods_str = '\n'.join(repr(f) for f in foods)
        missing_foods_str = '\n'.join(food_names_not_in_menu)
        return f'''Table {table_number} ordered:
{ordered_foods_str}
{self.name} does not have in the menu:
{missing_foods_str}'''

    def order_drink(self, table_number, *args):

        table = self.__get_table_by_number(table_number)

        if not table:
            return f'Could not find table {table_number}'

        drink_names_in_menu = [name for name in args if name in self.drink_names]
        drink_names_not_in_menu = [name for name in args if name not in self.drink_names]

        drinks = [self.__get_drink_by_name(drink_name) for drink_name in drink_names_in_menu]
        [table.order_drink(d) for d in drinks]

        ordered_str = '\n'.join(repr(d) for d in drinks)
        missing_str = '\n'.join(drink_names_not_in_menu)
        return f'''Table {table_number} ordered:
{ordered_str}
{self.name} does not have in the menu:
{missing_str}'''

    def leave_table(self, table_number):

        table = self.__get_table_by_number(table_number)
        table_bill = table.get_bill()
        self.total_income += table_bill
        table.clear()
        return f'''Table: {table_number}
Bill: {table_bill:.2f}'''

    def get_free_tables_info(self):
        table_infos = [t.free_table_info() for t in self.tables_repository if not t.is_reserved]
        return '\n'.join(table_infos)

    def get_total_income(self):
        return f'Total income: {self.total_income:.2f}lv'
