# Python-Wordle-Solver
Python based console application for solving wordle puzzles.

To download and use the program, you'll only need to download 'WordleSolver.exe'

This was my first time using python, so the code is likely inefficient, but my aim was to make it functional.

The program starts with a list of all possible 5 letter words, which have been sorted from 'best' to 'worst' guess using criteria available in 'wordsort.py'. With each guess, the user inputs the colours of the tiles and the program removes any invalid guesses from the list and displays the top 5 'best' guesses as suggestions for the next guess. This repeats until a solution to the puzzle is found.
