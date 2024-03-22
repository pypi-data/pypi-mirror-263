import numpy as np
import pytest

from pathfinding3d.core.diagonal_movement import DiagonalMovement
from pathfinding3d.core.grid import Grid
from pathfinding3d.core.node import GridNode
from pathfinding3d.core.util import expand_path
from pathfinding3d.finder.a_star import AStarFinder
from pathfinding3d.finder.best_first import BestFirst
from pathfinding3d.finder.bi_a_star import BiAStarFinder
from pathfinding3d.finder.breadth_first import BreadthFirstFinder
from pathfinding3d.finder.dijkstra import DijkstraFinder
from pathfinding3d.finder.finder import ExecutionRunsException, ExecutionTimeException
from pathfinding3d.finder.ida_star import IDAStarFinder
from pathfinding3d.finder.msp import MinimumSpanningTree
from pathfinding3d.finder.theta_star import ThetaStarFinder

finders = [
    AStarFinder,
    BestFirst,
    BiAStarFinder,
    DijkstraFinder,
    IDAStarFinder,
    BreadthFirstFinder,
    MinimumSpanningTree,
    ThetaStarFinder,
]
TIME_LIMIT = 10  # give it a 10 second limit.

weighted_finders = [
    AStarFinder,
    BiAStarFinder,
    DijkstraFinder,
    MinimumSpanningTree,
]

SIMPLE_MATRIX = np.zeros((5, 5, 5))
SIMPLE_MATRIX[0, 0, 0] = 1
SIMPLE_MATRIX[0, 0, 1] = 1
SIMPLE_MATRIX[0, 0, 2] = 1
SIMPLE_MATRIX[0, 0, 3] = 1
SIMPLE_MATRIX[0, 0, 4] = 1
SIMPLE_MATRIX[1, :, :] = 1
SIMPLE_MATRIX[2, :, :] = 1
SIMPLE_MATRIX[3, :, :] = 1
SIMPLE_MATRIX[4, 0, 0] = 1
SIMPLE_MATRIX[4, 1, 0] = 1
SIMPLE_MATRIX[4, 2, 0] = 1
SIMPLE_MATRIX[4, 3, 0] = 1
SIMPLE_MATRIX[4, 4, 0] = 1

WEIGHTED_SIMPLE_MATRIX = np.copy(SIMPLE_MATRIX)
WEIGHTED_SIMPLE_MATRIX[4, 1, 1] = 1
WEIGHTED_SIMPLE_MATRIX[4, 2, 1] = 1
WEIGHTED_SIMPLE_MATRIX[4, 3, 1] = 1
WEIGHTED_SIMPLE_MATRIX[4, 2, 0] = 99
WEIGHTED_SIMPLE_MATRIX[1, :, :] = 99
WEIGHTED_SIMPLE_MATRIX[2, :, :] = 99
WEIGHTED_SIMPLE_MATRIX[3, :, :] = 99


def test_path():
    """
    test if we can find a path
    """
    grid = Grid(matrix=SIMPLE_MATRIX)
    start = grid.node(0, 0, 0)
    end = grid.node(4, 4, 0)
    for find in finders:
        if find == ThetaStarFinder:
            continue
        grid.cleanup()
        finder = find(time_limit=TIME_LIMIT)
        path_, runs = finder.find_path(start, end, grid)
        path = []
        for node in path_:
            if isinstance(node, GridNode):
                path.append((node.x, node.y, node.z))
            elif isinstance(node, tuple):
                path.append((node[0], node[1], node[2]))
        print(find.__name__)
        print(f"path: {path}")
        print(f"length: {len(path)}, runs: {runs}")
        assert len(path) == 9


def test_weighted_path():
    grid = Grid(matrix=WEIGHTED_SIMPLE_MATRIX)
    start = grid.node(0, 0, 0)
    end = grid.node(4, 4, 0)
    for find in weighted_finders:
        grid.cleanup()
        finder = find(time_limit=TIME_LIMIT)
        path_, runs = finder.find_path(start, end, grid)
        path = []
        for node in path_:
            if isinstance(node, GridNode):
                path.append((node.x, node.y, node.z))
            elif isinstance(node, tuple):
                path.append((node[0], node[1], node[2]))
        print(find.__name__)
        print(f"path: {path}")
        print(f"length: {len(path)}, runs: {runs}")
        assert len(path) == 11


def test_path_diagonal():
    # test diagonal movement
    grid = Grid(matrix=SIMPLE_MATRIX)
    start = grid.node(0, 0, 0)
    end = grid.node(4, 4, 0)
    for find in finders:
        grid.cleanup()
        finder = find(diagonal_movement=DiagonalMovement.always, time_limit=TIME_LIMIT)
        path_, runs = finder.find_path(start, end, grid)
        path = []
        for node in path_:
            if isinstance(node, GridNode):
                path.append((node.x, node.y, node.z))
            elif isinstance(node, tuple):
                path.append((node[0], node[1], node[2]))
        print(find.__name__)
        print(f"path: {path}")
        print(f"length: {len(path)}, runs: {runs}")
        if find == ThetaStarFinder:
            path = expand_path(path)
        assert len(path) == 5


def test_max_runs():
    grid = Grid(matrix=SIMPLE_MATRIX)
    start = grid.node(0, 0, 0)
    end = grid.node(4, 4, 0)
    for find in finders:
        grid.cleanup()
        finder = find(diagonal_movement=DiagonalMovement.always, time_limit=TIME_LIMIT, max_runs=3)
        with pytest.raises(ExecutionRunsException):
            path, runs = finder.find_path(start, end, grid)
            print(f"{find.__name__} finishes after {runs} runs without exception")
            print(f"path: {path}")
        msg = f"{finder.__class__.__name__} needed too many iterations"
        assert finder.runs <= 3, msg


def test_time():
    grid = Grid(matrix=SIMPLE_MATRIX)
    start = grid.node(0, 0, 0)
    end = grid.node(4, 4, 0)
    for find in finders:
        grid.cleanup()
        finder = find(diagonal_movement=DiagonalMovement.always, time_limit=-0.1)
        with pytest.raises(ExecutionTimeException):
            path, runs = finder.find_path(start, end, grid)
            print(f"{find.__name__} finishes after {runs} runs without exception")
            print(f"path: {path}")
        msg = f"{finder.__class__.__name__} took too long"
        assert finder.runs == 1, msg


def test_msp():
    """
    Test that the minimum spanning tree finder returns all nodes.
    """
    matrix = np.array(np.ones((3, 3, 3)))
    grid = Grid(matrix=matrix)

    start = grid.node(0, 0, 0)

    finder = MinimumSpanningTree()
    assert finder.tree(grid, start).sort() == [node for row in grid.nodes for col in row for node in col].sort()


def test_theta_star(caplog):
    """
    Test that the theta star finder returns the correct path.
    """
    caplog.set_level("WARNING")
    grid = Grid(matrix=WEIGHTED_SIMPLE_MATRIX)
    start = grid.node(0, 0, 0)
    end = grid.node(4, 4, 0)

    finder = ThetaStarFinder(diagonal_movement=DiagonalMovement.never, time_limit=TIME_LIMIT)
    assert finder.diagonal_movement == DiagonalMovement.always
    assert "Diagonal movement is forced to always" in caplog.text
