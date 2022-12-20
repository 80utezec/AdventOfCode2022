import os

if __name__ == '__main__':
  inputLines = []
  with open(os.path.dirname(__file__) + "/inputs/inputDay04.txt") as _file:
    for line in _file:
      inputLines.append(line.strip())

  # Task 01:
  totalPairs = 0
  for line in inputLines:
    elf1 = line.split(",")[0].split("-")
    elf2 = line.split(",")[1].split("-")
    if ((int(elf1[0]) <= int(elf2[0])) and (int(elf1[1]) >= int(elf2[1]))) or ((int(elf1[0]) >= int(elf2[0])) and (int(elf1[1]) <= int(elf2[1]))):
      # print(f"{elf1} and {elf2}")
      totalPairs += 1
  print(f"Task01: {totalPairs}")

  # Task 02:
  totalPairs = 0
  for line in inputLines:
    elf1 = line.split(",")[0].split("-")
    elf2 = line.split(",")[1].split("-")
    if (((int(elf2[0]) <= int(elf1[1])) or (int(elf2[1]) <= int(elf1[0])))):
      print(f"{elf1} and {elf2}")
      totalPairs += 1
  print(f"Task02: {totalPairs}")
