import os

alphaMap = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
            'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
            'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39,
            'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

if __name__ == '__main__':
  inputLines = []
  with open(os.path.dirname(__file__) + "/inputs/inputDay03.txt") as _file:
    for line in _file:
      inputLines.append(line)

  # Task 01:
  priority = 0
  for line in inputLines:
    firstHalf = list(line[:len(line)//2])
    secondHalf = list(line[len(line)//2:])
    sameElement = list(set(firstHalf).intersection(secondHalf))[0]
    priority += (alphaMap[sameElement])
  print(f"Task01: {priority}")

  # Task 02:
  priority = 0
  lines = []
  for lineno, line in enumerate(inputLines):
    lines.append(line.strip())
    if (lineno+1) % 3 == 0:
      sameElement = list(set(lines[0]).intersection(lines[1]).intersection(lines[2]))[0]
      priority += (alphaMap[sameElement])
      lines = []
  print(f"Task02: {priority}")
