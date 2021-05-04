import dungeon
import numpy as np

class valueIteration:

  def __init__(self, game, gamma, maxIterations):
    self.game = game
    self.gamma = gamma
    self.maxIterations = maxIterations
    self.initValueMap()

  def initValueMap(self):
    self.valueMap = []
    for row in range(len(self.game.map)):
      self.valueMap.append([])
      for char in self.game.map[row]:
        if char == 'W':
          self.valueMap[row].append(float('-inf'))
        else:
          self.valueMap[row].append(float(0))

  def didConverge(self):
    for row in range(len(self.valueMap)):
      for col in range(len(self.valueMap[row])):
        if abs(self.valueMap[row][col] - self.prev_valueMap[row][col]) > 0.0001:
          return False
    return True

  def train(self):
    self.prev_valueMap = [row[:] for row in self.valueMap]

    for row in range(len(self.prev_valueMap)):
      for col in range(len(self.prev_valueMap[row])):
        if self.prev_valueMap[row][col] == float('-inf') or self.game.map[row][col] == 'E':
          continue
        reward = self.game.getPotentialReward(row, col)
        potentialValues = [reward, reward, reward, reward]
        potentialValues[0] += self.gamma * self.prev_valueMap[row - 1][col]
        potentialValues[1] += self.gamma * self.prev_valueMap[row][col + 1]
        potentialValues[2] += self.gamma * self.prev_valueMap[row + 1][col]
        potentialValues[3] += self.gamma * self.prev_valueMap[row][col - 1]

        self.valueMap[row][col] = max(potentialValues)

    return self.didConverge()

  def playGame(self):
    while not self.train():
      pass
    self.game.printMap()
    self.printValueMap()
    
    while self.game.map[self.game.playerRow][self.game.playerCol] != 'E':
      choices = []
      choices.append(self.valueMap[self.game.playerRow - 1][self.game.playerCol])
      choices.append(self.valueMap[self.game.playerRow][self.game.playerCol + 1])
      choices.append(self.valueMap[self.game.playerRow + 1][self.game.playerCol])
      choices.append(self.valueMap[self.game.playerRow][self.game.playerCol - 1])

      bestChoice = np.argmax(choices)
      
      resetValueMap = False
      if bestChoice == 0:
        if self.game.map[self.game.playerRow - 1][self.game.playerCol] in ['G', 'T']:
          resetValueMap = True
        self.game.up()
      elif bestChoice == 1:
        if self.game.map[self.game.playerRow][self.game.playerCol + 1] in ['G', 'T']:
          resetValueMap = True
        self.game.right()
      elif bestChoice == 2:
        if self.game.map[self.game.playerRow + 1][self.game.playerCol] in ['G', 'T']:
          resetValueMap = True
        self.game.down()
      elif bestChoice == 3:
        if self.game.map[self.game.playerRow][self.game.playerCol - 1] in ['G', 'T']:
          resetValueMap = True
        self.game.left()

      self.game.printMap()

      if resetValueMap:
        self.initValueMap()
        while not self.train():
          pass
        self.printValueMap()

    print('Final Score: ' + str(self.game.score))
    return self.game.score
      

  def printValueMap(self):
    for row in self.valueMap:
      for value in row:
        prettyValue = "{:.2f}".format(value)
        print(prettyValue, end='\t')
      print()
    print()