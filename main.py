import dungeon

for i in range(0, 5):
  mapFile = open('maps/map' + str(i) + '.txt')
  game = dungeon.dungeon(mapFile)

  if i == 2:
    game.printMap()
    game.up()
    game.left()
    game.down()
    game.down()
    game.right()
    game.right()
    game.up()
    game.right()
    game.up()
    game.printMap()
    print(game.score)