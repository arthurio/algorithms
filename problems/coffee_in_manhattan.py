import math


def o_n_2(matrix, people):
    ''' Go through all the positions on the matrix and compute:
        - distance (Int): Total distance to all the positions containing people
        - delta (Int): Distance between the people the further away and the closest ones
    Args:
        matrix list(list): 2-dimension grid of all available positions
        people list(tuple): List of position tuples representing people at intersection
    Return:
        position tuple(x, y): return the position of the best spot to open a coffee shop.
    '''
    distances = {}

    for x, row in enumerate(matrix):
        for y, col in enumerate(row):
            distance = 0
            max_distance = None
            min_distance = math.pow(len(matrix), 2)
            for px, py in people:
                current_distance = abs(x - px) + abs(y - py)
                distance += current_distance
                max_distance = max(max_distance, current_distance)
                min_distance = min(min_distance, current_distance)

            distances[(x, y)] = (
                # total distance, no need for avg as it's the same pool for all possibilities
                distance,
                # if 2 positions get the same total distance, pick the more centered one
                max_distance - min_distance
            )

    return min(distances, key=lambda x: distances[x])


def median(sorted_array):
    length = len(sorted_array)
    half = length / 2
    if length % 2 == 0:
        return int(math.floor((sorted_array[half - 1] + sorted_array[half]) / 2))
    else:
        return sorted_array[half]


def o_n_log_n(matrix, people):
    xs = []
    ys = []

    # o(n)
    for x, y in people:
        xs.append(x)
        ys.append(y)

    # o(n * log n)
    xs.sort()
    ys.sort()

    # o(1)
    return (median(xs), median(ys))
