import cvxpy as cp
import numpy as np
from constants import *


def main():
    nodes = [6, 63]
    travelingSalesman(nodes)
    return


def travelingSalesman(nodes: list, isOrdered: bool = False):
    if not nodes:
        return

    n = len(nodes)

    x = cp.Variable((n, n), boolean=True)
    t = cp.Variable(n, integer=True)
    # Distances
    costs = shortestPath(nodes)
    c = np.zeros((n, n))
    for edge, dist in costs.items():
        i = nodes.index(edge[0])
        j = nodes.index(edge[1])
        if isOrdered and i == 0 and j == n - 1:
            c[i, j] = 0
            c[j, i] = 0
        else:
            c[i, j] = dist[0]
            c[j, i] = dist[0]

    """
    Constraints
    """
    constraints = []

    for i in range(n):
        indices = np.hstack((np.arange(0, i), np.arange(i + 1, n)))
        constraints.append(sum(x[i, indices]) == 1)

    for j in range(n):
        indices = np.hstack((np.arange(0, j), np.arange(j + 1, n)))
        constraints.append(sum(x[indices, j]) == 1)

    for i in range(1, n):
        for j in range(1, n):
            constraints.append(t[i] - t[j] + n*x[i, j] <= n - 1)
    """
    Objective Function Definition
    """
    obj_func = cp.sum(cp.multiply(c, x))
    problem = cp.Problem(cp.Minimize(obj_func), constraints)

    problem.solve(solver=cp.GUROBI)
    print(obj_func.value)
    print(x.value)
    startToStopDist = costs[(nodes[0], nodes[1])]
    print(startToStopDist)
    return (obj_func.value, x.value)


def shortestPath(nodes: list) -> dict:
    n = len(edges.keys())
    new_edges = {}
    d = getDistances(n)
    for st in range(len(nodes) - 1):
        for sp in range(st + 1, len(nodes)):
            start = nodes[st] - 1
            stop = nodes[sp] - 1
            """
            Variables
            """
            x = cp.Variable((n, n), boolean=True)

            """
            Constraints
            """
            constraints = []
            for i in range(n):
                s1 = s2 = 0
                v = 0
                if i == start:
                    v = 1
                elif i == stop:
                    v = -1
                for j in range(n):
                    if i != j:
                        s1 += x[i, j]
                        s2 += x[j, i]
                constraints.append(s1 - s2 == v)

            """
            Objective Function Definition
            """
            obj_func = cp.Minimize(cp.sum(cp.multiply(d, x)))
            problem = cp.Problem(obj_func, constraints)
            
            problem.solve(solver=cp.GUROBI)
            new_edges[(start + 1, stop + 1)] = (obj_func.value, printAdjacencyMatrix(x.value, start + 1, stop + 1))
    return new_edges


def getDistances(n: int):
    d = np.full((n, n), 9999999.0)
    for edge, cost in edges.items():
        i, j = edge[0], edge[1]
        dist, flow = cost[0], cost[1]
        d[i - 1, j - 1] = dist * flow
        d[j - 1, i - 1] = dist * flow
    return d


def printAdjacencyMatrix(matrix, start: int = 0, stop: int = 0) -> list:
    stops = [start]
    while stops[-1] != stop:
        next = np.where(matrix[stops[-1]-1]==1)[0][0] + 1
        stops.append(next)
    return stops


if __name__ == '__main__':
    main()
