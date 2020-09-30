"""
driver for graph search problem

"""
"""
We the undersigned promise that we have in good faith attempted to follow the principles of pair programming. Although
we were free to discuss ideas with others, the implementation is our own. We have shared a common workspace and taken 
turns at the keyboard for the majority of the work that we are submitting.

Pair Programmer 1 
NHI DANG
09/29/2020
Pair Programmer 2
BRANDON RENDON 
09/29/2020
"""

from statistics import (mean, stdev)  # Only available in Python 3.4 and newer

from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from basicsearch_lib02.timer import Timer
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
import collections


def driver():
    timer = Timer()
    # result dictionary will contain the result for all strategies
    results = {'BFS': {'Total_steps': [], 'Total_explored_nodes': [], 'Time_in_seconds': []},
               'DFS': {'Total_steps': [], 'Total_explored_nodes': [], 'Time_in_seconds': []},
               'AS': {'Total_steps': [], 'Total_explored_nodes': [], 'Time_in_seconds': []}}

    # Strategies
    strategies = {'BFS': BreadthFirst, 'DFS': DepthFirst, 'AS': Manhattan}

    # Create a puzzle 31 times
    for t in range(31):

        # Create an 8-puzzle (3x3) and perform the search
        for i in range(3, 4):
            problem = NPuzzle(i * i - 1)
            print(f'\t<Problem number {t + 1}>')
            print('Init State')
            print(problem.initial)
            print('Goal States', problem.goals)
            print('___________________________________\n')

            # Test each strategies on the same puzzle:
            for key in strategies:
                # Assign the g and h method corresponding to the current strategie
                problem.g = strategies[key].g
                problem.h = strategies[key].h

                # Execute the search using the current strategie
                # Set verbose to True if we want to see each move
                moves, exploredNodes, time = graph_search(problem, verbose=False)

                results[key]['Total_steps'].append(len(moves))
                results[key]['Total_explored_nodes'].append(exploredNodes)
                results[key]['Time_in_seconds'].append(time)

    # Print out the Mean and STDev for all strategies used
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~SUMMARY TABLE~~~~~~~~~~~~~~~~~\n')
    for strategie_key in results:
        items = results[strategie_key]
        print(f'* Result for strategie: | {strategie_key} | *\n')
        for item_key in items:
            print(f'- {item_key}: ')
            print(f'\t+ Mean: {mean(items[item_key])}')
            print(f'\t+ STDev: {stdev(items[item_key])}')
        print('___________________________________________')
    print(f'\nTotal time to run 31 trials: {timer.elapsed()}')


# To do:  Run driver() if this is the entry module
if __name__ == "__main__":
    driver()
