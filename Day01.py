import os
from Elf import Elf

if __name__ == '__main__':
  elves = []

  with open(os.path.dirname(__file__) + "/inputs/inputDay01.txt") as _file:

    calories = []
    elfCount = 1
    for line in _file:
      if len(line.strip()) == 0:
        elves.append(Elf(elfCount, calories, sum(calories)))

        calories = []
        elfCount += 1
      else:
        calories.append(int(line))

elves.sort(key=lambda x: x.totalCalories)
print(f"{elves[-1]}")

best3 = 0
for elf in elves[-3:]:
  best3 += elf.totalCalories
print(f"Best 3: {best3}")
