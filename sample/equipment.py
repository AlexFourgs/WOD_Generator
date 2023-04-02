
from sample.enums.unit import Unit

class Equipment():

    def __init__(self, name: str, weight: int, unit: Unit = Unit.POUNDS) -> None:
        self.name = name
        self.weight = weight
        self.unit = unit
