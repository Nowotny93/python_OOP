from python_oop_exams.project_16AUG2020.hardware import Hardware


class PowerHardware(Hardware):

    def __init__(self, name, capacity, memory):
        super().__init__(name, "Power", int(capacity * 0.25), int(memory * 1.75))
