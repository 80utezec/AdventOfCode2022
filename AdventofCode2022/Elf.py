class Elf:
  def __init__(self, number, calories, totalCalories) -> None:
    self.number = number
    self.calories = calories
    self.totalCalories = totalCalories

  def __repr__(self) -> str:
    return "Elf" + str(self.number) + " has a total of " + str(self.totalCalories)
