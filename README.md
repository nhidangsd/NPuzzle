# NPuzzle Graph Search
A generic graph search routine that can be used to conduct breadth-first, depth-first,
and A* search by varying the parameters given to it.

- To install this project in your local machine, go to a directory you want to save this project and run: 

  $ git clone https://github.com/nhidangsd/NPuzzle.git
  
- To go inside the installed project, run:

  $ cd NPuzzle
  
- To run this project, run:

  $ python3 tiledriver.py
  
  
  NOTE: 
  - The driver will create 31 different trials of an 8-puzzle and test all search strategies such as Breadth-first, Depth-first,
and A* on each version of 8-puzzle created. 
  - Upon completion, for each strategie used, the program will display a summary table that indicates the mean (average) and standard
deviation of the following measurements:
 
      • length of plan (number of steps to solution)
      
      • number of nodes expanded
      
      • elapsed time in seconds.
      
  - For debugging purpose, please set variable 'verbose' when calling the graph_search() on line 60 in tiledriver.py to see each moves that the puzzle make when perform the search.
