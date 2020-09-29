from basicsearch_lib02.tileboard import TileBoard
from basicsearch_lib02.searchrep import Problem


class NPuzzle(Problem):
    """
    NPuzzle - Problem representation for an N-tile puzzle
    Provides implementations for Problem actions specific to N tile puzzles.
    """

    def __init__(self, n, force_state=None, **kwargs):
        """"__init__(n, force_state, **kwargs)
        
        NPuzzle constructor.  Creates an initial TileBoard of size n.
        If force_state is not None, the puzzle is initialized to the
        specified state instead of being generated randomly.
        
        The parent's class constructor is then called with the TileBoard
        instance any any remaining arguments captured in **kwargs.        
        
        """
        # Note on **kwargs:
        # **kwargs is Python construct that captures any remaining arguments 
        # into a dictionary.  The dictionary can be accessed like any other 
        # dictionary, e.g. kwargs[“keyname”], or passed to another function 
        # as if each entry was a keyword argument:
        #    e.g. foobar(arg1, arg2, …, argn, **kwargs).

        self.board = TileBoard(n, force_state=force_state)
        super().__init__(self.board, goals=self.board.goals, **kwargs)

        # raise NotImplemented

    def actions(self, state):
        """actions(state) - find a set of actions applicable to specified state"""
        delta = {'UP': [-1, 0], 'DOWN': [1, 0], 'LEFT': [0, -1], 'RIGHT': [0, 1]}
        possible_actions = list(delta.values())
        index_blank_square = state.state_tuple().index(None)

        i = state.boardsize
        if index_blank_square % i == 0:
            possible_actions.remove(delta['LEFT'])
        if index_blank_square < i:
            possible_actions.remove(delta['UP'])
        if index_blank_square % i == i - 1:
            possible_actions.remove(delta['RIGHT'])
        if index_blank_square > i*i - i -1:
            possible_actions.remove(delta['DOWN'])

        return possible_actions

    def result(self, state, action):
        """result(state, action)- apply action to state and return new state"""
        return state.move(action)

    def goal_test(self, state):
        """goal_test(state) - Is state a goal?"""
        # return state == self.goals

        param = state.state_tuple()
        return super().goal_test(param)
        # raise NotImplemented
