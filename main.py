import dungeon
import valueIteration

optimalGammas = [0.9, 1, 0.65, 1, 0.8]
finalScores = []

for i in range(0, 5):
  mapFile = open('maps/map' + str(i) + '.txt')
  game = dungeon.dungeon(mapFile)

  vi = valueIteration.valueIteration(game, optimalGammas[i], 100)
  score = vi.playGame()
  finalScores.append(score)

print('\nFinal Scores of Value Iteration Policy: ' + str(finalScores))