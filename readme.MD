# EECS 738 Project 4: Treasure Hunters Inc.

### Submission by Benjamin Wyss

Implementing Value Iteration and Monte Carlo Reinforcement Learning Policies to Play a Map Traversal Game

## The Map Traversal Game

The goal of the map traversal game is to move from the starting location to the exit location within a 2-dimensional grid while accumulating the highest score possible. Every move that the player makes penalizes their score, and the maps additionally contain score-boosting gold pickups and score-dropping traps. A sample map is depicted below:

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

## Ideas

## Process

## Results

## Conclusion
