from copy import copy
from utils.matrix import END
from utils.matrix import get_reachable_neighbors
from utils.matrix import is_adjacency_correct
from utils.matrix import START


# Algorithm based on BFS
def find_shortest_path(matrix):
    queue = []
    visited = []

    has_start = False
    has_end = False

    # Find Starting point and validate the matrix
    for x, row in enumerate(matrix):
        visited.append([False for __ in range(len(row))])
        for y, value in enumerate(row):
            # Make sure that we have neighbors if the configuration says so
            assert is_adjacency_correct(matrix, x, y), (
                "There is a gap in the path, a position marked as 1 leads nowhere"
            )

            if value is START:
                # Uncomment below if you want to enforce only one starting point but this algo supports it
                # assert not has_start, "You can't have multiple start points."
                has_start = True
                queue.append(([], (x, y)))

            if value is END:
                # Uncomment below if you want to enforce only one ending point but this algo supports it
                # assert not has_end, "You can't have multiple end points."
                has_end = True

    assert has_start and has_end, "The Matrix needs a start point and an end point"

    while queue:
        path, current_position = queue.pop(0)
        path = copy(path)  # Make a copy so that when we diverge we don't append to the same initial path
        path.append(current_position)
        current_x, current_y = current_position

        if matrix[current_x][current_y] is END:
            return path

        visited[current_x][current_y] = True

        for n in get_reachable_neighbors(matrix, visited, current_x, current_y):
            queue.append((path, n))

    assert False, "No path was found between the start and end."
