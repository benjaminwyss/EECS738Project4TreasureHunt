class dungeon:

  def __init__(self, mapFile, startingScore=100, trapVal=-100, goldVal=100, moveVal=-5):
    self.mapFile = mapFile
    self.score = startingScore
    self.startingScore = startingScore
    self.trapVal = trapVal
    self.goldVal = goldVal
    self.moveVal = moveVal
    
    self.map = []

    # Build the map from the mapFile
    row = 0
    for line in mapFile:
      self.map.append([])
      col = 0
      line = line.rstrip('\n')
      for char in line:
        self.map[row].append(char)
        # Set the player's starting position
        if char == 'S':
          self.playerRow = row
          self.playerCol = col
        col += 1
      row += 1

  def reset(self):
    self.score = self.startingScore
    # Rebuild the map from the mapFile
    self.mapFile.seek(0)
    self.map = []

    row = 0
    for line in self.mapFile:
      self.map.append([])
      col = 0
      line = line.rstrip('\n')
      for char in line:
        self.map[row].append(char)
        if char == 'S':
          self.playerRow = row
          self.playerCol = col
        col += 1
      row += 1

  def getPossibleMoves(self):
    # Possible moves are any non-wall move
    possibleMoves = []
    if self.map[self.playerRow - 1][self.playerCol] != 'W':
      possibleMoves.append('up')
    if self.map[self.playerRow][self.playerCol + 1] != 'W':
      possibleMoves.append('right')
    if self.map[self.playerRow + 1][self.playerCol] != 'W':
      possibleMoves.append('down')
    if self.map[self.playerRow][self.playerCol - 1] != 'W':
      possibleMoves.append('left')

    return possibleMoves

  def getPotentialReward(self, row, col):
    char = self.map[row][col]

    # Determine the potential reward from the map character at the given row and column
    if char == 'W':
      return float('-inf')
    elif char == 'G':
      return float(self.goldVal)
    elif char == 'T':
      return float(self.trapVal)
    else:
      return float(self.moveVal)

  def up(self):
    # Determine the map character of the attempted move
    nextChar = self.map[self.playerRow - 1][self.playerCol]
    # Can't move through walls
    if nextChar == 'W':
      print('Illegal Move Attempted. Cannot Move Up')
      return False
    
    # Update player position
    self.playerRow -= 1

    # Update player score
    if nextChar == 'S':
      self.score += self.moveVal
    elif nextChar == '-':
      self.score += self.moveVal
    elif nextChar == 'E':
      self.score += self.moveVal
      # Return true if the player wins
      return True
    elif nextChar == 'T':
      self.score += self.trapVal
      self.map[self.playerRow][self.playerCol] = '-'
    elif nextChar == 'G':
      self.score += self.goldVal
      self.map[self.playerRow][self.playerCol] = '-'

    # Return False if the game is not finished
    return False

  def right(self):
    # Determine the map character of the attempted move
    nextChar = self.map[self.playerRow][self.playerCol + 1]
    # Can't move through walls
    if nextChar == 'W':
      print('Illegal Move Attempted. Cannot Move Right')
      return False
    
    # Update player position
    self.playerCol += 1

    if nextChar == 'S':
      self.score += self.moveVal
    elif nextChar == '-':
      self.score += self.moveVal
    elif nextChar == 'E':
      self.score += self.moveVal
      # Return true if the player wins
      return True
    elif nextChar == 'T':
      self.score += self.trapVal
      self.map[self.playerRow][self.playerCol] = '-'
    elif nextChar == 'G':
      self.score += self.goldVal
      self.map[self.playerRow][self.playerCol] = '-'

    # Return False if the game is not finished
    return False

  def down(self):
    # Determine the map character of the attempted move
    nextChar = self.map[self.playerRow + 1][self.playerCol]
    # Can't move through walls
    if nextChar == 'W':
      print('Illegal Move Attempted. Cannot Move Down')
      return False
    
    # Update player position
    self.playerRow += 1

    if nextChar == 'S':
      self.score += self.moveVal
    elif nextChar == '-':
      self.score += self.moveVal
    elif nextChar == 'E':
      self.score += self.moveVal
      # Return true if the player wins
      return True
    elif nextChar == 'T':
      self.score += self.trapVal
      self.map[self.playerRow][self.playerCol] = '-'
    elif nextChar == 'G':
      self.score += self.goldVal
      self.map[self.playerRow][self.playerCol] = '-'

    # Return False if the game is not finished
    return False

  def left(self):
    # Determine the map character of the attempted move
    nextChar = self.map[self.playerRow][self.playerCol - 1]
    # Can't move through walls
    if nextChar == 'W':
      print('Illegal Move Attempted. Cannot Move Left')
      return False
    
    # Update player position
    self.playerCol -= 1

    if nextChar == 'S':
      self.score += self.moveVal
    elif nextChar == '-':
      self.score += self.moveVal
    elif nextChar == 'E':
      self.score += self.moveVal
      # Return true if the player wins
      return True
    elif nextChar == 'T':
      self.score += self.trapVal
      self.map[self.playerRow][self.playerCol] = '-'
    elif nextChar == 'G':
      self.score += self.goldVal
      self.map[self.playerRow][self.playerCol] = '-'

    # Return False if the game is not finished
    return False

  def printMap(self):
    # Print each character in the game map
    row = 0
    for line in self.map:
      col = 0
      for char in line:
        # Print a * where the player is located
        if row == self.playerRow and col == self.playerCol:
          print('*', end='')
        else:
          print(char, end='')
        col += 1
      row += 1
      print()
    print()