class Equipment:
    equipment_id = 0

    def __init__(self, name):
        Equipment.equipment_id += 1
        self.name = name
        self.id = Equipment.equipment_id

    @staticmethod
    def get_next_id():
        return Equipment.equipment_id + 1

    def __repr__(self):
        return f'Equipment <{self.id}> {self.name}'
