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

    for i in range(3, 4):
        # for strategie in (BreadthFirst, DepthFirst, Manhattan):
        #     problem = NPuzzle(i*i-1, g=strategie.g, h=strategie.h)
        #     state = problem.initial
        #
        #     print('State')
        #     print(state)
        #     print('State tuple', state.state_tuple())
        #     print('Goals', problem.goals)
        #     solved = problem.goal_test(state)
        #
        #     while not solved:
        #         actions = problem.actions(state)
        #         print('graph search', graph_search(problem, verbose=True))
        #         state = problem.result(state, actions[0])
        #         solved = problem.goal_test(state)
        problem = NPuzzle(i * i - 1, g=BreadthFirst.g, h=BreadthFirst.h)
        state = problem.initial

        print('Init State\n', state)
        print('State tuple', state.state_tuple())
        print('Goals', problem.goals)
        solved = problem.goal_test(state)
        a,b,c = graph_search(problem, verbose=True)
        print('__________________')
        print("Path to Solution\n", a)
        print('num explored', b)
        print('time',c)
        # while not solved:
        #     actions = problem.actions(state)
        #     print('actions:', actions)
        #     graph_search(problem, verbose=True)
        #     state = problem.result(state, actions[0])
        #     solved = problem.goal_test(state)


# To do:  Run driver() if this is the entry module
if __name__ == "__main__":
    driver()