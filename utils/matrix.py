UNREACHABLE = 0
REACHABLE = 1
START = 2
END = 3


def get_possible_neighbors(x, y):
    return (
        (x - 1, y),  # left
        (x + 1, y),  # right
        (x, y - 1),  # above
        (x, y + 1),  # under
    )


def is_adjacency_correct(matrix, x, y):
    if matrix[x][y] is not REACHABLE:
        return True

    possible_neighbors = get_possible_neighbors(x, y)
    neighbors = 0

    for nx, ny in possible_neighbors:
        if not(0 <= nx < len(matrix)) or not (0 <= ny < len(matrix[nx])):
            continue

        if matrix[nx][ny] is not UNREACHABLE:
            neighbors += 1

        if neighbors > 1:
            return True

    return False


def get_reachable_neighbors(matrix, visited, x, y):
    possible_neighbors = get_possible_neighbors(x, y)
    return (
        (nx, ny)
        for nx, ny in possible_neighbors
        if (
            0 <= nx < len(matrix) and 0 <= ny < len(matrix[nx]) and  # position is within limits
            matrix[nx][ny] is not UNREACHABLE and  # The neighbor is reachable
            not visited[nx][ny]  # The neighbor was not already visited from another path
        )
    )
