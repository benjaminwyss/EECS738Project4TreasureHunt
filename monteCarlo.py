import dungeon
import numpy as np

class monteCarlo:

  def __init__(self, game, gamma, maxRuns, firstVisit=False):
    self.game = game
    self.gamma = gamma
    self.maxRuns = maxRuns
    self.firstVisit = firstVisit
    self.initMaps()

  def initMaps(self):
    self.valueMap = []
    self.visitMap = []
    self.returnMap = []
    for row in range(len(self.game.map)):
      self.valueMap.append([])
      self.visitMap.append([])
      self.returnMap.append([])
      for char in self.game.map[row]:
        if char == 'W':
          self.returnMap[row].append(float('inf'))
          self.visitMap[row].append(float(-1))
          self.valueMap[row].append(float('-inf'))
        else:
          self.returnMap[row].append(float(0))
          self.visitMap[row].append(float(0))
          self.valueMap[row].append(float(0))

  def calculateValueMap(self):
    for row in range(len(self.valueMap)):
      for col in range(len(self.valueMap[row])):
        if self.visitMap[row][col] == 0:
          self.valueMap[row][col] = float('-inf')
        else:
          self.valueMap[row][col] = self.returnMap[row][col] / self.visitMap[row][col]

  def train(self):
    for i in range(self.maxRuns):
      visits = []
      while self.game.map[self.game.playerRow][self.game.playerCol] != 'E':
        choices = self.game.getPossibleMoves()
        choice = np.random.choice(choices)
        
        oldScore = self.game.score

        if choice == 'up':
          self.game.up()
        elif choice == 'right':
          self.game.right()
        elif choice == 'down':
          self.game.down()
        elif choice == 'left':
          self.game.left()
        
        newScore = self.game.score
        reward = newScore - oldScore

        if self.firstVisit and (self.game.playerRow, self.game.playerCol) in visits:
          continue

        visits.append((self.game.playerRow, self.game.playerCol))
        self.visitMap[self.game.playerRow][self.game.playerCol] += 1

        gammaPower = 0
        for (visitRow, visitCol) in reversed(visits):
          ret = reward * (self.gamma ** gammaPower)
          self.returnMap[visitRow][visitCol] += reward
          gammaPower += 1

      self.game.reset()
    
    self.calculateValueMap()
    self.printValueMap()

  def playGame(self):
    self.train()
    self.game.printMap()
    self.printValueMap()
    
    while self.game.map[self.game.playerRow][self.game.playerCol] != 'E':
      choices = []
      choices.append(self.valueMap[self.game.playerRow - 1][self.game.playerCol])
      choices.append(self.valueMap[self.game.playerRow][self.game.playerCol + 1])
      choices.append(self.valueMap[self.game.playerRow + 1][self.game.playerCol])
      choices.append(self.valueMap[self.game.playerRow][self.game.playerCol - 1])

      bestChoice = np.argmax(choices)

      oldScore = self.game.score
      
      if bestChoice == 0:
        self.game.up()
      elif bestChoice == 1:
        self.game.right()
      elif bestChoice == 2:
        self.game.down()
      elif bestChoice == 3:
        self.game.left()

      newScore = self.game.score
      reward = newScore - oldScore

      if reward == self.game.goldVal:
        self.valueMap[self.game.playerRow][self.game.playerCol] -= reward
      else:
        self.valueMap[self.game.playerRow][self.game.playerCol] += reward

      self.game.printMap()

    print('Final Score: ' + str(self.game.score))
    return self.game.score
      

  def printValueMap(self):
    for row in self.valueMap:
      for value in row:
        prettyValue = "{:.0f}".format(value)
        print(prettyValue, end='\t')
      print()
    print()