# Python Exercise 5 - Modules, Documentation, Algorithms 

All required files are already included in this repository.
Your submissions will automatically be graded when pushed.

You may run the grader locally upfront via

```
python -m pytest [--help]
```

If desired, the "old style" grader can also be accessed via

```
python exercise_5.py [--help]
```

This homework is to be prepared in teams. Properly document the files you hand
in to receive full credit. Each module (file) and function needs a docstring.
The purpose of each function needs to be summarized as a single sentence and
then, if required, your intent and the behavior of the function can be
described in more detail.

Furthermore, provide doctests for all functions but `main()`. Each of the
modules needs to include a `main()` function which calls the other functions
and prints appropriate output to `stdout`.
`main()` itself must be called by the ifmain pattern at the end of the file.


## 1. Reading VRPTW instances (2 points)
Input files for vehicle routing problems generally include a depot and some
customers. Both the depot and the customers are referred to as nodes. Storing
vrptw instances as JSON files makes the meaning of the data easier to
understand and eases the task of parsing such files. Have a look at one
possible example: [r101.json](R101.json).

Implement a function `read_json(filename: str)` that takes the name of a
[JSON](https://en.wikipedia.org/wiki/JSON) file and returns all data as a
dictionary. In this dictionary, the value containing the customers should be
a list of dictionaries (just like in the input file). Keep the input files'
dictionary keys.

Name the module: `vrptw_reader.py` 

## 2. Distance matrix (1 point)
Write a function called `calc_distance_matrix(node_list)` that returns a matrix
of euclidean distances between all given nodes. The first index to the matrix
must refer to the row, the second to the column. All nodes' ids must correspond
to the row/column relevant to that node. The expected argument is a list that
contains all nodes as dictionaries (the depot and all customers). The function
needs to assert that the lowest id is 0, that all ids are unique and that they
are consecutive (0, 1, 2, ...). Feel free to write any number of additional
functions (as you deem appropriate) to help you getting this task done.

Add the function to the module: `vrptw_reader.py`

## 3. Polar coordinates (1 points)
Write a function called `calc_polar_coordinates(depot, node_list)` that
returns a list with
[polar coordinates](https://en.wikipedia.org/wiki/Polar_coordinate_system)
of the depot and all nodes with respect to the depot. This first entry has to
be the depot having the coordinates (0, 0) followed by all nodes in the same
order as in the input list. For every list entry use the named tuple Node
consisting of the node id and the polar coordinates saved as a named tuple
`PolarCoordinate`.

Now implement the function `order(p)` having as argument the output of the
function `calc_polar_coordinates(.)` and returning a list of nodes ordered by
the angle "phi".
Again, feel free to write any number of additional functions. 

Add the function to the module: `vrptw_reader.py`

## 4. Simple VRP solver (5 points)
Implement the counterclockwise sweep algorithm for the VRP. This algorithm
considers the particular customers one after another ordered by their polar
coordinates and
- proceeds the route if neither the truck capacity nor the truck range is
  exceeded and
- begins a new route otherwise.
     
Each route starts and ends at the depot and is serviced by a single truck. Each
customer must be on exactly one route. None of the trucks is allowed to exceed
its capacity or range. The capacity and the customer's demands use the same
units. The range uses the same distance units as the distance matrix.

Represent a route as a simple list of customer dictionaries. Write a function
`solve_vrp(.)` that takes a dictionary with all required data as returned by
the function in the first task. `solve_vrp(.)` must return a list of routes
(that is, a list of node lists (depot - customers - depot) where each node still is a dictionary).
Pay extra attention to the source code documentation of this function (the
code can only say what you do, not why you do it).

Write an additional function `print_routes(.)` that takes a list of routes
with customer dictionaries and prints the routes to `stdout`. The output
format must be one route (truck) per line with all the customer ids on the
route. The output should resemble the following 
```
[0,  28,  12,  79,   3,  24,  80,   0]
[0,  11,  19,  49,  48,   0]
...
```
and end with a final newline. Use as many additional functions as you deem
useful.

Name the program file: `vrp_solver.py`
