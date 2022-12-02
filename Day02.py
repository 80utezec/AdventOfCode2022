import os
from RockPaperScissors import RockPaperScissors

shapes = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
actionsToTake = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}

if __name__ == '__main__':
  with open(os.path.dirname(__file__) + "/inputs/inputDay02.txt") as _file:
    totalScore = 0
    actionsList = []
    for line in _file:
      actionsList.append(line.split(" "))

    # Task 01
    for actions in actionsList:
      totalScore += RockPaperScissors.pointTotal(shapes[actions[0]], shapes[(actions[1].strip())])
    print(f"Total Score Task01: {totalScore}")

    # Task 02
    totalScore = 0
    for actions in actionsList:
      points = RockPaperScissors.winLoseDraw(shapes[actions[0]], actionsToTake[(actions[1].strip())])
      totalScore += points
    print(f"Total Score Task02: {totalScore}")
