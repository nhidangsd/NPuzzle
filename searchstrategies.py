"""
searchstrategies

Module to provide implementations of g and h for various search strategies.
In each case, the functions are class methods as we don't need an instance
of the class.  

If you are unfamiliar with Python class methods, Python uses a function
decorator (indicated by an @ to indicate that the next method is a class
method).  Example:

class SomeClass:
    @classmethod
    def foobar(cls, arg1, arg2):
        "foobar(arg1, arg2) - does ..."
        
        code... class variables are accessed as cls.var (if needed)
        return computed value

A caller would import SomeClass and then call, e.g. :  
    SomeClass.foobar("hola","amigos")

Contains g and h functions for:
BreadFirst - breadth first search
DepthFirst - depth first search
Manhattan - city block heuristic search.  To restrict the complexity of
    this, you only need handle heuristics for puzzles with a single solution
    where the blank is in the center, e.g.:
        123
        4 5
        678
    When multiple solutions are allowed, the heuristic becomes a little more
    complex as the city block distance must be estimated to each possible solution
    state. 
"""


class BreadthFirst:
    "BreadthFirst - breadth first search"

    @classmethod
    def g(cls, parentnode, action, childnode):
        """"g - cost from initial state to childnode
        constrained such that the last edge of the search space
        moves from parentnode to childnode via the specified action
        """

        return parentnode.depth + 1

    @classmethod
    def h(cls, searchnode):
        """h - heuristic value"""
        return 0


# To complete:
# Write two more classes, DepthFirst and Manhattan
# that support appropriate g/h with the same signatures for the class functions


class DepthFirst:
    """DepthFirst - Depth first search"""

    @classmethod
    def g(cls, parentnode, action, childnode):
        """"g - cost from initial state to childnode
        constrained such that the last edge of the search space
        moves from parentnode to childnode via the specified action
        """
        return 0

    @classmethod
    def h(cls, searchnode):
        """h - heuristic value"""
        return -searchnode.depth


class Manhattan:
    """Manhattan - Manhattan search"""

    @classmethod
    def g(cls, parentnode, action, childnode):
        """"g - cost from initial state to childnode
        constrained such that the last edge of the search space
        moves from parentnode to childnode via the specified action
        """

        return childnode.depth * 2

    @classmethod
    def h(cls, searchnode):
        """h - heuristic value"""
        # Current_state - A tuple contains the current state retrieving from searchnode
        current_state = searchnode.state.state_tuple()
        # Goal_state - A tuple contains one of the goal state in the goal lists
        goal_states = searchnode.problem.goals
        # Dimension of the puzzle
        puzzle_size = searchnode.problem.initial.boardsize
        # Initialize heuristic value to 0
        h = 0
        h_list = []
        for goal_state in goal_states:
            for x in current_state:
                # Look up row, column value for x in the current_state and goal_state:
                # current_row, current_column = cls.find_Row_and_Column(x, current_row, puzzle_size)
                current_row = current_state.index(x) // puzzle_size
                current_column = current_state.index(x) % puzzle_size
                goal_row = goal_state.index(x) // puzzle_size
                goal_column = goal_state.index(x) % puzzle_size

                h += abs(goal_row - current_row) + abs(goal_column - current_column)
                h_list.append(h)

        return min(h_list)
