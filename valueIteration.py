import dungeon
import numpy as np

class valueIteration:

  def __init__(self, game, gamma, maxIterations):
    # Initialize game, hyperparameters, and value map
    self.game = game
    self.gamma = gamma
    self.maxIterations = maxIterations
    self.initValueMap()

  def initValueMap(self):
    self.valueMap = []
    for row in range(len(self.game.map)):
      self.valueMap.append([])
      for char in self.game.map[row]:
        # Assign starting value of -inf for walls
        if char == 'W':
          self.valueMap[row].append(float('-inf'))
        # Assign starting value of 0 otherwise
        else:
          self.valueMap[row].append(float(0))

  def didConverge(self):
    for row in range(len(self.valueMap)):
      for col in range(len(self.valueMap[row])):
        # If the value matrix has a change of greater than 0.0001, it did not converge
        if abs(self.valueMap[row][col] - self.prev_valueMap[row][col]) > 0.0001:
          return False
    # Otherwise, it did converge
    return True

  def train(self):
    # Save old value map
    self.prev_valueMap = [row[:] for row in self.valueMap]

    for row in range(len(self.prev_valueMap)):
      for col in range(len(self.prev_valueMap[row])):
        if self.prev_valueMap[row][col] == float('-inf') or self.game.map[row][col] == 'E':
          continue
        # Calculate reward of tile
        reward = self.game.getPotentialReward(row, col)
        # Potential values for tile is the reward + gamma * adjacent tile value
        potentialValues = [reward, reward, reward, reward]
        potentialValues[0] += self.gamma * self.prev_valueMap[row - 1][col]
        potentialValues[1] += self.gamma * self.prev_valueMap[row][col + 1]
        potentialValues[2] += self.gamma * self.prev_valueMap[row + 1][col]
        potentialValues[3] += self.gamma * self.prev_valueMap[row][col - 1]

        # Choose the max potential value
        self.valueMap[row][col] = max(potentialValues)

    # Return whether or not the value map has converged
    return self.didConverge()

  def playGame(self):
    # Train for the game map
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

      # Make the highest value choice
      bestChoice = np.argmax(choices)
      
      # Execute the choice and determine if the map has been altered (only happens with gold and traps)
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

      # If the map has been altered, retrain on the new map
      if resetValueMap:
        self.initValueMap()
        while not self.train():
          pass
        self.printValueMap()

    # Print and return final score
    print('Final Score: ' + str(self.game.score))
    return self.game.score
      

  def printValueMap(self):
    # Print each value in the value map
    for row in self.valueMap:
      for value in row:
        prettyValue = "{:.2f}".format(value)
        print(prettyValue, end='\t')
      print()
    print()