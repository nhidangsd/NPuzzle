"""
problemsearch - Functions for searching.
"""

from basicsearch_lib02.searchrep import (Node, print_nodes)
from basicsearch_lib02.queues import PriorityQueue
from basicsearch_lib02.timer import Timer
from basicsearch_lib02.tileboard import TileBoard
from explored import Explored


def graph_search(problem, verbose=False, debug=False):
    """graph_search(problem, verbose, debug) - Given a problem representation
    (instance of basicsearch_lib02.representation.Problem or derived class),
    attempt to solve the problem.
    
    If debug is True, debugging information will be displayed.
    
    if verbose is True, the following information will be displayed:
        
        Number of moves to solution
        List of moves and resulting puzzle states
        Example:
        
            Solution in 25 moves        
            Initial state
                  0        1        2    
            0     4        8        7    
            1     5        .        2    
            2     3        6        1    
            Move 1 -  [0, -1]
                  0        1        2    
            0     4        8        7    
            1     .        5        2    
            2     3        6        1    
            Move 2 -  [1, 0]
                  0        1        2    
            0     4        8        7    
            1     3        5        2    
            2     .        6        1    
            
            ... more moves ...
            
                  0        1        2    
            0     1        3        5    
            1     4        2        .    
            2     6        7        8    
            Move 22 -  [-1, 0]
                  0        1        2    
            0     1        3        .    
            1     4        2        5    
            2     6        7        8    
            Move 23 -  [0, -1]
                  0        1        2    
            0     1        .        3    
            1     4        2        5    
            2     6        7        8    
            Move 24 -  [1, 0]
                  0        1        2    
            0     1        2        3    
            1     4        .        5    
            2     6        7        8    
        
        If no solution were found (not possible with the puzzles we
        are using), we would display:
        
            No solution found
    
    Returns a tuple (path, nodes_explored, elapsed_s) where:
    path - list of actions to solve the problem or None if no solution was found
    nodes_explored - Number of nodes explored (dequeued from frontier)
    elapsed_s is the elapsed wall clock time performing the search
    """
    # Start the timer:
    timer = Timer()

    # Create a hashtable to store all explored states
    exploredStates = Explored()
    # Create a PriorityQueue to store all current states
    frontier = PriorityQueue(f=lambda node: node.g + node.h)
    # Initialize the frontier with the first Node
    frontier.append(Node(problem, problem.initial))

    # Loop until the solution is found or the state space is exhausted
    while frontier.__len__() != 0:

        # Pop a node from the frontier
        node = frontier.pop()

        if problem.goal_test(node.state):
            alpha = node.path()
            actions = node.solution()

            # If verbose is True, display all moves
            if verbose:
                print(f'Solution in {len(actions)} moves')
                for i in range(len(actions)):
                    print(f'Move {i + 1} - {actions[i]}')
                    print(alpha[i + 1].state, end='\n\n')

            # Return a Tuple contains:
            # - List of actions to solve the problem,
            # - Number of nodes explored,
            # - elapsed_s in seconds
            return alpha, len(exploredStates.exploredStates), timer.elapsed_s()

        else:
            # Explore the children of current node
            for child in node.expand(problem):

                child_tuple = child.state.state_tuple()

                # if we haven't explored this child yet
                # Load it into frontier and explore set
                if not exploredStates.exists(child_tuple):
                    exploredStates.add(child_tuple)
                    frontier.append(child)

    # If no solution found, return None
    return None
