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

    # Create a hashtable to store all explored states as state_tuple
    exploredStates = Explored()

    # Create a PriorityQueue to store all current states
    frontier = PriorityQueue()
    # Initialize the frontier
    firstNode = Node(problem, problem.initial)
    frontier.append(firstNode)

    # Loop until the solution is found or the state space is exhausted
    while frontier:

        # Remove the 1st node in frontier
        node = frontier.pop()

        # print('result', problem.goal_test(node))

        # Check if this node is the goals
        # Else expand this node, add children to frontier
        if problem.goal_test(node.state):
            if verbose:
                print(f'Solution in {len(exploredStates.exploredStates)} moves')
            alpha = node.path()
            beta = len(exploredStates.exploredStates)
            charlie = timer.elapsed()
            return (alpha, beta, charlie)

        # Add this node to explored states if not exists yet:
        if not exploredStates.exists(node.state.state_tuple()):
            exploredStates.add(node.state.state_tuple())

        for child in node.expand(problem):
            child_tuple = child.state.state_tuple()
            if not exploredStates.exists(child_tuple) and not frontier.__contains__(child):
                frontier.append(child)
    return None
    # if verbose:
    #     total_moves_to_solution = len(node.path())
    #     print(f'Solution in { total_moves_to_solution} moves')
    #     print('Initial state')
    #     print(board)
    #     i = 0
    #     while not board.solved():
    #         i += 1
    #         actions = board.get_actions()[0]
    #         print(f'Move {i} - [{actions}]')
    #         print(board.move(actions))
