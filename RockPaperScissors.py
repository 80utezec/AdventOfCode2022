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
