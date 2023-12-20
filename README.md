# XO_ai
a tic tac toe playing ai using minimax algorithm
## tic tac toe
### history
An early variation of the game was played in the Roman Empire, around the 1st century B.C. It was called "terni lapilli," which means "three pebbles at a time." The game's grid markings have been found chalked all over Roman ruins. Evidence of the game was also found in ancient Egyptian ruins.

The first print reference to "noughts and crosses," the British name for the game, appeared in 1864. The first print reference to a game called "tick-tack-toe" occurred in 1884 but referred to a children's game played on a slate. 

### gameplay
 The goal of tic-tac-toe is to be the first player to get three in a row on a 3-by-3 grid or four in a row in a 4-by-4 grid. 

To start, one player draws a board, creating a grid of squares, usually 3-by-3 or 4-by-4.

In a 3-by-3 grid game, the player who is playing "X" always goes first. Players alternate placing Xs and Os on the board until either player has three in a row, horizontally, vertically, or diagonally or until all squares on the grid are filled. If a player is able to draw three Xs or three Os in a row, then that player wins. If all squares are filled and neither player has made a complete row of Xs or Os, then the game is a draw.

One of the game's best strategies involves creating a "fork," which is placing your mark in such a way that you have the opportunity to win two ways on your next turn. Your opponent can only block one, thereby, you can win after that.

The gameplay is the same if you are playing on a 4-by-4 grid. The "X" player goes first. And, players alternate placing Xs and Os on the board until a row is completed horizontally, vertically, or diagonally, or all 16 squares are filled. If all 16 squares are filled and neither player has four in a row, the game is a draw. 

### other variants

 Tic-tac-toe can be also be played on a 5-by-5 grid with each player trying to get five in a row.

The game can also be played on larger grids, such as 10-by-10 or even 20-by-20. For any grid of 6-by-6 or greater, it might be best to make your goal to get five in a row. This turns the basic game of tic-tac-toe into a much more complex game with similarities to the board game Pente, meaning "five" in Greek. Similarly, the goal of Pente is for a player to score five marks in a row. 



## Usage:

to get the code run the following command
```bash
git clone https://github.com/parsoli83/XO_ai.git
```

use python3 to run the code

```bash
python3 xo.py
```

## about the algorithm
### minimax
this AI uses minimax algorithm to evaluate the best move in each term. minimax is an algorithm based on maximizing the chance of our win and minimization of the chance of loss. This is achieved with computing the score of each possible move and comparing them is a recursive way.
Minimax is a kind of backtracking algorithm that is used in decision making and game theory to find the optimal move for a player, assuming that your opponent also plays optimally. It is widely used in two player turn-based games such as Tic-Tac-Toe, Backgammon, Mancala, Chess, etc.
In Minimax the two players are called maximizer and minimizer. The maximizer tries to get the highest score possible while the minimizer tries to do the opposite and get the lowest score possible.
Every board state has a value associated with it. In a given state if the maximizer has upper hand then, the score of the board will tend to be some positive value. If the minimizer has the upper hand in that board state then it will tend to be some negative value. The values of the board are calculated by some heuristics which are unique for every type of game.

Time complexity : O(b^d) b is the branching factor and d is count of depth or ply of graph or tree.

Space Complexity : O(bd) where b is branching factor into d is maximum depth of tree similar to DFS.


### alpha-beta pruning
this project can also get optimized by using this algorithm

Alpha–beta pruning is a search algorithm that seeks to decrease the number of nodes that are evaluated by the minimax algorithm in its search tree. It is an adversarial search algorithm used commonly for machine playing of two-player combinatorial games (Tic-tac-toe, Chess, Connect 4, etc.)

## CS50X
this project is made as my final project of the CS50X course 