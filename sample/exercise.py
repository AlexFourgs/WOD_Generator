"""
"""

from sample.enums.difficulty import Difficulty
from equipment import Equipment

class Exercise():

    def __init__(self, name: str, difficulty: Difficulty, muscle_worked: list, equipement: Equipment = None, benefit: str = "") -> None:
        self.name = name
        self.difficulty = difficulty
        self.muscle_worked = muscle_worked
        self.equipment = equipement
        self.benefit = benefit
