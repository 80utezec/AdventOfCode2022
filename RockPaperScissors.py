shapesValues = {'rock': 1, 'paper': 2, 'scissors': 3}


class RockPaperScissors():
  def pointTotal(computerAction, playerAction):
    shapeValue = shapesValues[playerAction]

    if playerAction == computerAction:
      return 3 + shapeValue
    elif playerAction == "rock":
      if computerAction == "scissors":
        return 6 + shapeValue
      else:
        return 0 + shapeValue
    elif playerAction == "paper":
      if computerAction == "rock":
        return 6 + shapeValue
      else:
        return 0 + shapeValue
    elif playerAction == "scissors":
      if computerAction == "paper":
        return 6 + shapeValue
      else:
        return 0 + shapeValue

  def winLoseDraw(computerAction, playerDecision):
    if playerDecision == "draw":
      return RockPaperScissors.pointTotal(computerAction, computerAction)
    elif playerDecision == "win":
      if computerAction == "rock":
        return RockPaperScissors.pointTotal(computerAction, "paper")
      elif computerAction == "paper":
        return RockPaperScissors.pointTotal(computerAction, "scissors")
      else:
        return RockPaperScissors.pointTotal(computerAction, "rock")
    else:
      if computerAction == "rock":
        return RockPaperScissors.pointTotal(computerAction, "scissors")
      elif computerAction == "paper":
        return RockPaperScissors.pointTotal(computerAction, "rock")
      else:
        return RockPaperScissors.pointTotal(computerAction, "paper")
