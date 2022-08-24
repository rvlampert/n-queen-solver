# n-queen-solver

A N-queen puzzle solver, using AI genetic algorithms

## Objective

Build a artificial inteligence capable of solve the n_queen puzzle game

## How to run

Create a virtual environment, use ```make install-dependencies``` command to install the python dependencies, then use ```make run <n>``` to run the program

## Board

The board is represented by a list with the position of the queen in each column, for example: `[1,4,2,3]` means that there is one queen at the first line and first column, a queen at the forth line and secound column and etc

## Variables

- N = Board size
- g = Generations
- n = Number of individuals
- k = Tournament size
- m = Mutation probability
- e = If there will be elitism or not