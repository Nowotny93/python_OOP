from python_oop_exams.project_16AUG2020 import Software


class LightSoftware(Software):

    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, "Light", int(capacity_consumption * 1.5), int(memory_consumption * 0.5))
