import os
from RockPaperScissors import RockPaperScissors

shapes = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}

if __name__ == '__main__':
  with open(os.path.dirname(__file__) + "/inputs/inputDay02.txt") as _file:
    totalScore = 0
    for line in _file:
      actions = line.split(" ")
      totalScore += RockPaperScissors.pointTotal(shapes[actions[0]], shapes[(actions[1].strip())])

print(f"Total Score: {totalScore}")
