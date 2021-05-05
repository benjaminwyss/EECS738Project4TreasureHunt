# EECS 738 Project 4: Treasure Hunters Inc.

### Submission by Benjamin Wyss

Implementing Value Iteration and Monte Carlo Reinforcement Learning Policies to Play a Map Traversal Game

## The Map Traversal Game

The goal of the map traversal game is to move from the starting location to the exit location within a 2-dimensional grid while accumulating the highest score possible. Every move that the player makes penalizes their score, and the maps additionally contain single-use score-boosting gold pickups and score-dropping traps. A sample map is depicted below:

![Image of a Map](images/map0.PNG)

Map Legend:

\- : Passages that the player can walk through  
W : Walls that the player cannot walk through  
S : Starting location  
E : Exit location  
G : Gold that boosts score  
T : Trap that damages score

Additional maps are located in the [maps](maps) folder.

Scoring:

The game's starting score, gold score, trap penalty, and move penalty are all configurable when instantiating a member of the [dungeon.py](dungeon.py) class, but they have the following default values:

Starting Score : +100  
Gold Score : +100  
Trap Penalty : -100  
Move Penalty : -5

## Process

Value Iteration and Monte Carlo reinforcement learning techniques should be able to learn the map traversal game programatically and execute their determined optimal policies to maximize final scores in each game map.

Value Iteration is implemented in [valueIteration.py](valueIteration.py). Training a value iteration policy to play the map traversal game involves determining a steady-state value matrix representing the expected score value of each tile in a given map. This process iterates over each map tile until the value matrix converges, updating each tile's expected value based on the score achieved by moving to the tile and the maximum expected value of adjacent tiles. After training on a map, the value iteration policy can be used to play the map traversal game by making each choice that yields the maximum possible expected value. One challenge in using this policy is that it does not account for changes to the map that occur when picking up gold or triggering a trap. This challenge is overcome by simply retraining the value matrix whenever a change to the map occurs.

Monte Carlo is implemented in [monteCarlo.py](monteCarlo.py). Training a Monte Carlo policy to play the map traversal game involves executing large amounts of random traversals of a given map and tracking an expected score value matrix related to the score of each move in each random traversal. Each move's score is also used to update the values of previous moves in a random traversal so that the policy learns to move towards score-boosting moves and away form score-dropping moves. Just like value iteration, playing the map traversal game with the monte carlo policy involves making each choice that yields the maximum possible expected value. To combat the monte carlo policy's tendency to repeat loops of moves that do not progress the map traversal game in any meaningful way, the value matrix is also updated as the game is played.

## Results

## Conclusion
