# Oval Optimization -- ISE 3230 Final Project Code Repository

## Introduction
The oval on Ohio State’s campus is a sea of walking paths without symmetry, rhyme, or reason. The paths shoot out at weird angles and cover the ground with a seemingly random scatter of routes. With 131 line segments and 65 intersections, there are tons of possible paths to take between any two buildings. Additionally, some paths are more crowded than others between class times, leading to faster or slower walking speeds. With 13 popular classroom buildings located along the oval, we thought the Ohio State community could use some support with navigating this web. 

As a result, we set out to create an algorithm that when given any number of buildings along the oval, will return the path to visit each building at least once that takes the shortest amount of time.
This algorithm is split into two parts: the first being a linear programming formulation of shortest path and the second being a Miller-Tucker-Zemlin formulation of the traveling salesman problem. The shortest path algorithm is a helper to the traveling salesman since the traveling salesman only considers destinations and not intermediate vertice


## File Overview
- tsp.py: containts program main algorithmic code along with other helper methods
- constants.py: contains data pertaining to the oval path lengths, numbered nodes, and some other auxiliary constants
- "Oval with lengths and numbered nodes".png: Picture that maps the numbered nodes to places on the actual oval and names sites along the oval

## How to run
### Requirements
- Python 3.4+
- CVXPY
- Liscensed Gurobi Problem Solver

### Intructions
- Download both tsp.py and constants.py into the same directory
- In main() of tsp.py, change nodes in output based on desired stops. There is an option for ordering stops as a boolean parameter to the travelingSalesman problem.
