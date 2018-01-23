# GameofLife : http://www.conwaylife.com/w/index.php?title=Conway%27s_Game_of_Life

1. Input the row and column of a hypothetical grid.
Eg: row: 1, col: 0
    row: 1, col: 1
    row: 1, col: 2

This builds the following world: [[0,0,0],
                                  [1,1,1],
                                  [0,0,0]]
                                 
2. Enter 'q' in order to start the simulation of the world.

3. Rules of the game: 

Live cells are represented by the number 1.

a. Any live cell with fewer than two live neighbours dies (referred to as underpopulation or exposure[1]).
b. Any live cell with more than three live neighbours dies (referred to as overpopulation or overcrowding).
c. Any live cell with two or three live neighbours lives, unchanged, to the next generation.
d. Any dead cell with exactly three live neighbours will come to life.

See up to 10 generations of the world.
