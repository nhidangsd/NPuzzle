"""
driver for graph search problem

"""

from statistics import (mean, stdev)  # Only available in Python 3.4 and newer

from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from basicsearch_lib02.timer import Timer
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
import collections


def driver():
    result = {'BFS': {'moves': [], 'explored': [], 'time': []},
              'DFS': {'moves': [], 'explored': [], 'time': []},
              'AS': {'moves': [], 'explored': [], 'time': []}}

    for t in range(2):
        for i in range(2, 3):
            problem = NPuzzle(i * i - 1)
            print('Init State')
            print(problem.initial)
            print('Goal States', problem.goals)
            print('__________________')
            for strategie in (BreadthFirst, DepthFirst, Manhattan):
                problem.g = strategie.g
                problem.h = strategie.h
                print(f'Result for {strategie}:')
                moves, exploredNodes, time = graph_search(problem, verbose=True)
                if strategie is BreadthFirst:
                    result['BFS']['moves'].append(len(moves))
                    result['BFS']['explored'].append(exploredNodes)
                    result['BFS']['time'].append(time)
                if strategie is DepthFirst:
                    result['DFS']['moves'].append(len(moves))
                    result['DFS']['explored'].append(exploredNodes)
                    result['DFS']['time'].append(time)
                if strategie is Manhattan:
                    result['AS']['moves'].append(len(moves))
                    result['AS']['explored'].append(exploredNodes)
                    result['AS']['time'].append(time)

                print('~~~~~~~~~~~~~~~')
    for strategie in result.keys():
        print('Mean')
        print(f'For {strategie} - moves is {mean(result[strategie]["moves"])}')
        print(f'For {strategie} - explores is {mean(result[strategie]["explored"])}')
        print(f'For {strategie} - times is {mean(result[strategie]["time"])}')
        print('\n\nStdev')
        print(f'For {strategie} - moves is {stdev(result[strategie]["moves"])}')
        print(f'For {strategie} - explores is {stdev(result[strategie]["explored"])}')
        print(f'For {strategie} - times is {stdev(result[strategie]["time"])}')
        print('\n\n\n\n\n')


# To do:  Run driver() if this is the entry module
if __name__ == "__main__":
    driver()
