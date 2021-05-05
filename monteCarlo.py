import dungeon
import numpy as np

class monteCarlo:

  def __init__(self, game, gamma, maxRuns, firstVisit=False):
    # Initialize game, hyperparameters, and maps used to calculate value map
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
        # Assign return map of inf, visit map of -1, and value map of -inf for walls
        if char == 'W':
          self.returnMap[row].append(float('inf'))
          self.visitMap[row].append(float(-1))
          self.valueMap[row].append(float('-inf'))
        # Assign each map values of 0 otherwise
        else:
          self.returnMap[row].append(float(0))
          self.visitMap[row].append(float(0))
          self.valueMap[row].append(float(0))

  def calculateValueMap(self):
    for row in range(len(self.valueMap)):
      for col in range(len(self.valueMap[row])):
        # Replace divide by 0 values with -inf
        if self.visitMap[row][col] == 0:
          self.valueMap[row][col] = float('-inf')
        # Otherwise value = total return / number of visits
        else:
          self.valueMap[row][col] = self.returnMap[row][col] / self.visitMap[row][col]

  def train(self):
    # for number of maxRuns, use random traversals to play the game
    for i in range(self.maxRuns):
      visits = []
      while self.game.map[self.game.playerRow][self.game.playerCol] != 'E':
        # Make a random move choice
        choices = self.game.getPossibleMoves()
        choice = np.random.choice(choices)
        
        oldScore = self.game.score

        # Execute the random move
        if choice == 'up':
          self.game.up()
        elif choice == 'right':
          self.game.right()
        elif choice == 'down':
          self.game.down()
        elif choice == 'left':
          self.game.left()
        
        # Determine the reward of the random move
        newScore = self.game.score
        reward = newScore - oldScore

        # If first visit only mode is enabled and the tile has already been visited, continue to next random move
        if self.firstVisit and (self.game.playerRow, self.game.playerCol) in visits:
          continue

        # Otherwise, mark the visit
        visits.append((self.game.playerRow, self.game.playerCol))
        self.visitMap[self.game.playerRow][self.game.playerCol] += 1

        # And update the total return of each visited tile
        gammaPower = 0
        for (visitRow, visitCol) in reversed(visits):
          ret = reward * (self.gamma ** gammaPower)
          self.returnMap[visitRow][visitCol] += reward
          gammaPower += 1

      # Reset the game after termination
      self.game.reset()
    
    # Calculate and print the value map
    self.calculateValueMap()
    self.printValueMap()

  def playGame(self):
    # Train on the game map
    self.train()
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

      oldScore = self.game.score
      
      # Execute the choice
      if bestChoice == 0:
        self.game.up()
      elif bestChoice == 1:
        self.game.right()
      elif bestChoice == 2:
        self.game.down()
      elif bestChoice == 3:
        self.game.left()

      # Determine the move reward
      newScore = self.game.score
      reward = newScore - oldScore

      # Update the value map to prevent infinite loops
      if reward == self.game.goldVal:
        self.valueMap[self.game.playerRow][self.game.playerCol] -= reward
      else:
        self.valueMap[self.game.playerRow][self.game.playerCol] += reward

      self.game.printMap()

    # Print and return final score
    print('Final Score: ' + str(self.game.score))
    return self.game.score
      

  def printValueMap(self):
    # Print each value in the value map
    for row in self.valueMap:
      for value in row:
        prettyValue = "{:.0f}".format(value)
        print(prettyValue, end='\t')
      print()
    print()