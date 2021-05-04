import dungeon
import valueIteration
import monteCarlo

viOptimalGammas = [0.9, 1, 0.65, 1, 0.8]
mcOptimalGammas = [0.6, 1, 0.9, 1, 0.8] 
mcOptimalFirstVisits = [False, False, False, False, True]
viFinalScores = []
mcFinalScores = []

for i in range(0, 5):
  mapFile = open('maps/map' + str(i) + '.txt')
  game = dungeon.dungeon(mapFile)

  vi = valueIteration.valueIteration(game, viOptimalGammas[i], 100)
  score = vi.playGame()
  viFinalScores.append(score)

  mc = monteCarlo.monteCarlo(game, mcOptimalGammas[i], 1000, mcOptimalFirstVisits[i])
  score = mc.playGame()
  mcFinalScores.append(score)

print('\nFinal Scores of Value Iteration Policy:\t' + str(viFinalScores))
print('Final Scores of Monte Carlo Policy:\t' + str(mcFinalScores))