import dungeon
import valueIteration
import monteCarlo

# Initialize hyperparameters for each policy and map (values determined by trial and error)
viOptimalGammas = [0.9, 1, 0.65, 1, 0.8]
mcOptimalGammas = [0.6, 1, 0.9, 1, 0.8] 
mcOptimalFirstVisits = [False, False, False, False, True]

viFinalScores = []
mcFinalScores = []

for i in range(0, 5):
  # Load game from map
  mapFile = open('maps/map' + str(i) + '.txt')
  game = dungeon.dungeon(mapFile)

  print('\nMap ' + str(i+1) + '\n')

  # Play game with value iteration
  print('Value Iteration\n')
  vi = valueIteration.valueIteration(game, viOptimalGammas[i], 100)
  score = vi.playGame()
  viFinalScores.append(score)

  # Play game with monte carlo
  print('\nMonte Carlo\n')
  mc = monteCarlo.monteCarlo(game, mcOptimalGammas[i], 1000, mcOptimalFirstVisits[i])
  score = mc.playGame()
  mcFinalScores.append(score)

# print final scores
print('\nFinal Scores of Value Iteration Policy:\t' + str(viFinalScores))
print('Final Scores of Monte Carlo Policy:\t' + str(mcFinalScores))